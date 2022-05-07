import datetime
import os
import shelve
import time
import threading
import sys
# import importlib
import webbrowser
import hpyculator as hpyc
import tempfile
from functools import partial  # 偏函数真好用
from typing import Iterator
# import pyperclip
# import jpype
# import pprint

import Doc  # 文档导入

# pyside6 ui signal导入
from PySide6.QtWidgets import QApplication, QMainWindow
from SettingWindow import SettingApplication
from ui.MainWindow import Ui_MainWindow
from ui.Signal import main_window_signal

import logging  # 日志导入


def pathCheck():
    """
    路径检查

    :return: setting_file_path, output_dir_path
    """

    setting_dir_path = str(os.path.join(os.getcwd(), 'Setting'))  # 初始化设置目录
    setting_file_path = str(os.path.join(setting_dir_path, 'hpyculator_setting'))  # 初始化设置文件位置

    # 检查存放设置文件的文件夹是否存在
    if not os.path.exists(setting_dir_path):
        os.makedirs(setting_dir_path)  # 刚建的文件夹就不用考虑是否要读取设置了
    else:

        with shelve.open(setting_file_path, writeback=True) as setting_file:
            # 从设置文件读取输出目录
            try:
                output_dir_path = setting_file['save_location']
            except KeyError:
                output_dir_path = str(os.path.join(os.getcwd(), 'Output'))
                setting_file['save_location'] = output_dir_path
            logging.debug(f'输出文件保存位置:{output_dir_path}')

    # 检查输出文件夹是否存在
    if os.path.exists(output_dir_path):
        pass
    else:
        os.makedirs(output_dir_path)

    return setting_file_path, output_dir_path


def logCheck(setting_file_path):
    """
    日志检查

    :return: None
    """
    import LogManager  # 日志管理 初始化
    # 检查存放日志文件的文件夹是否存在
    LM = LogManager.LogManager(setting_file_path)
    LM.checkIsEnableLog()
    return None


def pluginCheak():
    """
    加载插件

    :return: plugin_filename_option_name_map, loaded_plugin
    """
    import PluginManager  # 插件管理

    # loaded_plugin: Optional[Dict[str, Callable]] = None  # 存放加载完毕的插件 ID-读取的插件
    # plugin_filename_option_name_map: Optional[Dict[str, str]] = None  # 选项名和实际文件名的映射表
    # selection_list: Optional[list[str]] = None  # 存放选项名列表

    PM = PluginManager.PluginManager()  # 加载插件管理器
    return PM.init_plugin()  # 加载插件


class Application(QMainWindow):
    def __init__(self,
                 setting_file_path,
                 output_dir_path,
                 plugin_filename_option_name_map,
                 loaded_plugin):
        """
        主窗口程序类
        """
        # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
        self.SETTING_FILE_PATH = setting_file_path
        self.OUTPUT_DIR_PATH = output_dir_path
        self.plugin_filename_option_name_map = plugin_filename_option_name_map  # 选项名映射id（文件或文件夹名）
        self.selection_list = plugin_filename_option_name_map.keys()  # 选项名列表
        self.loaded_plugin = loaded_plugin  # id映射插件对象

        logging.debug('主类初始化')
        super().__init__()
        self.ui = Ui_MainWindow()  # UI类的实例化()
        self.ui.setupUi(self)
        self.bindSignalWithSlots()  # 信号和槽的绑定

        self.main_window_signal = main_window_signal  # 更方便地使用自定义事件

        self.setWindowTitle("hpyculator %s -HowieHz制作" % Doc.VERSION)  # 设置标题

        # 读取设置文件-按钮状态和输出目录
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:
            try:
                self.save_settings = setting_file['save_settings']  # 是否保存设置
            except KeyError:
                setting_file['save_settings'] = True  # 默认保存选项状态
                self.save_settings = True

            if self.save_settings:  # 当保存check状态
                try:
                    self.ui.save_check.setChecked(setting_file['save_check'])  # 根据数据设置选项状态
                except KeyError:
                    setting_file['save_check'] = self.ui.save_check.isChecked()
                try:
                    self.ui.output_optimization_check.setChecked(setting_file['output_optimization'])  # 根据数据设置选项状态
                except KeyError:
                    setting_file['output_optimization'] = True
                    self.ui.output_optimization_check.setChecked(True)
                try:
                    self.ui.output_lock_maximums_check.setChecked(setting_file['output_lock_maximums'])  # 根据数据设置选项状态
                except KeyError:
                    setting_file['output_lock_maximums'] = True
                    self.ui.output_lock_maximums_check.setChecked(True)
            else:  # 当不保存check状态
                self.ui.output_optimization_check.setChecked(True)
                self.ui.output_lock_maximums_check.setChecked(True)

        self.is_thread_running: bool = False  # 防止反复启动计算线程

        # 关于gui显示内容的初始化
        self.ui.choices_list_box.addItems(self.plugin_filename_option_name_map.keys())  # 选项名添加到ui上
        self.ui.output_box.setPlainText(Doc.START_SHOW)  # 开启的展示
        self.ui.search_box.setPlaceholderText("输入字符自动进行搜索\n清空搜索框显示全部插件")  # 灰色背景提示字符
        self.ui.search_box.clear()  # 不清空不显示灰色背景
        self.ui.input_box.setFocus()  # 设置焦点

    def bindSignalWithSlots(self):
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)
        # my_signal.setProgressBar.connect(self.set_progress_bar)
        # my_signal.setResult.connect(self.set_result)
        def appendOutPut(msg: str):
            self.ui.output_box.appendPlainText(msg)

        def clearOutPut():
            self.ui.output_box.clear()

        def setOutPut(msg: str):
            self.ui.output_box.setPlainText(msg)

        main_window_signal.appendOutPutBox.connect(appendOutPut)

        main_window_signal.setOutPutBox.connect(setOutPut)

        main_window_signal.clearOutPutBox.connect(clearOutPut)

    def startEvent(self) -> None:
        """
        初始化计算，绑定计算按钮，启动计算线程

        :return: None
        """
        # self.inputbox_data - 储存输入框的内容
        # time_before_calculate - 临时储存时间，计录 计算时间
        # self.result_process  - 储存计算结果 （用于for循环,就是个i
        # self.result_last  - 储存计算结果

        if str(self.ui.input_box.toPlainText()) == "update_log":  # update_log检测
            self.ui.output_box.setPlainText(Doc.UPDATE_LOG)
            return
        if self.ui.choices_list_box.currentItem() is None:  # 是否选择检测
            self.ui.output_box.setPlainText("\n\n" +
                                            """
不选要算什么我咋知道要算啥子嘞

请在左侧选择运算核心
          ↓
← ← ←""")
            return None
        if self.ui.input_box.toPlainText() == "":  # 是否输入检测
            self.ui.output_box.setPlainText("""                                                  ↑
                                                  ↑上面的就是输入框了
不输要算什么我咋知道要算啥子嘞     ↑
         → → → → → → → → → →  ↑
         ↑
请在上面的框输入需要被处理的数据

如果忘记了输入格式，只要再次选择运算核心就会显示了（· ω ·）""")
            return None
        if self.plugin_attribute["input_mode"] == hpyc.STRING:
            self.inputbox_data = str(self.ui.input_box.toPlainText())  # 取得输入框的数字
        elif self.plugin_attribute["input_mode"] == hpyc.FLOAT:
            self.inputbox_data = float(self.ui.input_box.toPlainText())  # 取得输入框的数字
        elif self.plugin_attribute["input_mode"] == hpyc.NUM:
            self.inputbox_data = int(self.ui.input_box.toPlainText())  # 取得输入框的数字
        else:
            self.inputbox_data = 0  # 缺省

        # 以上是计算前工作

        if self.is_thread_running:
            main_window_signal.appendOutPutBox.emit("\n运算程序正在进行中，请勿反复点击计算按钮！\n")  # 清空输出框
        else:
            calculate_thread = threading.Thread(target=self.startCalculate)  # 启动计算线程
            calculate_thread.start()
            self.is_thread_running = True
        return None

    def startCalculate(self):
        """
        计算线程

        :return: None
        """
        time_spent = None

        def whatNeedCalculate():
            nonlocal time_spent

            time_before_calculate = time.perf_counter()  # 储存开始时间

            if self.plugin_attribute["return_mode"] == hpyc.RETURN_ONCE:
                self.result = str(self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data))
                main_window_signal.setOutPutBox.emit(str(self.result) + "\n")  # 结果为str，直接输出
            elif self.plugin_attribute["return_mode"] == hpyc.RETURN_LIST:  # 算一行输出一行
                main_window_signal.clearOutPutBox.emit()  # 清空输出框
                self.result = self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data)
                for result_process in self.result:
                    main_window_signal.appendOutPutBox.emit(str(result_process) + "\\n")  # 算一行输出一行
            elif self.plugin_attribute["return_mode"] == hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                main_window_signal.clearOutPutBox.emit()  # 清空输出框
                self.result = self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data)
                for result_process in self.result:  # 计算
                    main_window_signal.appendOutPutBox.emit(str(result_process))  # 算一行输出一行
            elif self.plugin_attribute["return_mode"] == hpyc.NO_RETURN_SINGLE_FUNCTION:
                main_window_signal.clearOutPutBox.emit()  # 清空输出框
                self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data, self, 'output')
            else:
                main_window_signal.clearOutPutBox.emit()  # 清空输出框
                self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data, self)
            time_spent = time.perf_counter() - time_before_calculate  # 储存结束时间

        def whatNeedCalculateWithSave(filename):  # 选择检测+计算
            # filename - 储存保存到哪个文件里
            nonlocal time_spent

            filestream = open(os.path.join(self.OUTPUT_DIR_PATH, f"{filename}.txt"), "w", encoding="utf-8")
            time_before_calculate = time.perf_counter()  # 储存开始时间

            try:
                if self.plugin_attribute["return_mode"] == hpyc.RETURN_ONCE:  # 分布输出和一次输出
                    self.result = self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data)
                    filestream.write(str(self.result) + "\n")
                elif self.plugin_attribute["return_mode"] == hpyc.RETURN_LIST:  # 算一行输出一行，但是没有换行
                    self.result = self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data)
                    for result_process in self.result:  # 计算
                        filestream.write(str(result_process) + "\\n")
                        filestream.flush()  # 算出来就存进去
                elif self.plugin_attribute["return_mode"] == hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                    self.result = self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data)
                    for result_process in self.result:  # 计算
                        filestream.write(str(result_process))
                        filestream.flush()  # 算出来就存进去
                elif self.plugin_attribute["return_mode"] == hpyc.NO_RETURN_SINGLE_FUNCTION:
                    self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data, filestream, 'save')
                else:
                    self.loaded_plugin[self.user_selection].on_calculate_with_save(self.inputbox_data, filestream)
            finally:
                filestream.close()

            time_spent = time.perf_counter() - time_before_calculate  # 储存结束时间

        def whatNeedCalculateWithOutputOptimization():
            nonlocal time_spent

            with tempfile.TemporaryFile('w+t', encoding='utf-8', errors='ignore') as filestream:
                time_before_calculate = time.perf_counter()  # 储存开始时间

                try:
                    if self.plugin_attribute["return_mode"] == hpyc.RETURN_ONCE:  # 分布输出和一次输出
                        self.result = self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data)
                        filestream.write(str(self.result) + "\n")
                    elif self.plugin_attribute["return_mode"] == hpyc.RETURN_LIST:  # 算一行输出一行，但是没有换行
                        self.result = self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data)
                        for result_process in self.result:  # 计算
                            filestream.write(str(result_process) + "\\n")
                            filestream.flush()  # 算出来就存进去
                    elif self.plugin_attribute["return_mode"] == hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                        self.result = self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data)
                        for result_process in self.result:  # 计算
                            filestream.write(str(result_process))
                            filestream.flush()  # 算出来就存进去
                    elif self.plugin_attribute["return_mode"] == hpyc.NO_RETURN_SINGLE_FUNCTION:
                        self.loaded_plugin[self.user_selection].on_calculate(self.inputbox_data, filestream, 'save')
                    else:
                        self.loaded_plugin[self.user_selection].on_calculate_with_save(self.inputbox_data, filestream)
                finally:
                    main_window_signal.clearOutPutBox.emit()  # 清空输出框
                    filestream.seek(0)  # 将文件指针移到开始处，准备读取文件
                    if self.ui.output_lock_maximums_check.isChecked():
                        for times, line in enumerate(quickTraverseFile(filestream)):
                            main_window_signal.appendOutPutBox.emit(line)
                            if times >= 128:
                                main_window_signal.appendOutPutBox.emit("\n\n输出上限：检测到输出数据过大，请使用保存到文件防止卡死")
                                break
                    else:
                        for line in quickTraverseFile(filestream):
                            main_window_signal.appendOutPutBox.emit(line)

            time_spent = time.perf_counter() - time_before_calculate  # 储存结束时间

        # 快读，低占用读取文件
        def quickTraverseFile(file, chunk_size=8192) -> Iterator:
            for chunk in iter(partial(file.read, chunk_size), ''):  # 用readline的话，读到换行符就会直接停止读取，不会读取到8192B，会增加读取次数
                yield chunk

        try:
            main_window_signal.clearOutPutBox.emit()  # 清空输出框
            main_window_signal.setOutPutBox.emit("计算程序正在运行中，所需时间较长，请耐心等待")
            if self.ui.save_check.isChecked():  # 检测保存按钮的状态判断是否保存
                if self.plugin_attribute["use_quantifier"] == hpyc.ON:
                    filename = datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S') + '  ' + self.plugin_attribute["save_name"] + str(
                        self.inputbox_data) + self.plugin_attribute["quantifier"]
                else:
                    filename = datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S') + '  ' + str(self.inputbox_data).replace('.', '_') + "的" + self.plugin_attribute["save_name"]
                whatNeedCalculateWithSave(filename)
                # 以下是计算后工作
                main_window_signal.clearOutPutBox.emit()  # 清空输出框
                main_window_signal.appendOutPutBox.emit(
                    f"\n本次计算+保存花费了{time_spent:.6f}秒\n")  # 输出本次计算时间
                main_window_signal.appendOutPutBox.emit(
                    "\n计算结果已保存在 " + os.path.join(self.OUTPUT_DIR_PATH, f"{filename}.txt"))
                main_window_signal.appendOutPutBox.emit("\n")
            else:  # 选择不保存才输出结果
                if self.ui.output_optimization_check.isChecked():
                    whatNeedCalculateWithOutputOptimization()
                    # 以下是计算后工作
                    main_window_signal.appendOutPutBox.emit(
                        f"\n\n本次计算+输出花费了{time_spent:.6f}秒\n")  # 输出本次计算时间
                    main_window_signal.appendOutPutBox.emit("已启用输出优化")
                else:
                    whatNeedCalculate()
                    # 以下是计算后工作
                    main_window_signal.appendOutPutBox.emit(
                        f"\n\n本次计算+输出花费了{time_spent:.6f}秒\n")  # 输出本次计算时间
        except Exception as e:
            main_window_signal.clearOutPutBox.emit()  # 清空输出框
            main_window_signal.setOutPutBox.emit(str(e))
            main_window_signal.appendOutPutBox.emit("\n\n插件发生错误，请检查输入格式")

        self.is_thread_running = False

    def userChooseOptionEvent(self, item):
        """
        左侧选择算法之后触发的函数 选择算法事件

        :param item:
        :return: None
        """
        # logging.debug(f'选中的选项名{self.ui.choices_list_box.currentItem().text()}')
        logging.debug(f'选中的选项名{item.text()}')
        self.user_selection = str(self.plugin_filename_option_name_map[item.text()])
        self.plugin_attribute = {}  # 读取的属性

        self.plugin_attribute = self.loadPluginAttribute(self.loaded_plugin, self.user_selection)

        self.ui.output_box.setPlainText(f"""\
{self.plugin_attribute["output_start"]}
{self.plugin_attribute["output_name"]} {self.plugin_attribute["version"]}
by {self.plugin_attribute["author"]}


使用提示
{self.plugin_attribute["help"]}

{self.plugin_attribute["output_end"]}""")

    def loadPluginAttribute(self,
                            loaded_plugin,
                            user_selection):
        """
        读取插件属性

        :return: plugin_attribute
        """
        plugin_attribute={}  #读取好的属性放在这里

        # self.required_parameters = ['input_mode','return_mode','save_name','output_name','use_quantifier','version']
        # self.optional_parameters=['output_start', 'quantifier', 'author', 'help', 'output_end', 'fullwidth_symbol']
        # self.parameters_list = ['output_start', 'quantifier', 'author', 'help', 'output_end', 'fullwidth_symbol','input_mode','return_mode','save_name','output_name','use_quantifier','version']
        # self.required_parameters.extend(self.optional_parameters)
        for option_name in ['output_start', 'quantifier', 'author', 'help', 'output_end', 'fullwidth_symbol',
                            'input_mode', 'return_mode', 'save_name', 'output_name', 'use_quantifier', 'version']:
            try:
                logging.debug(f'load {option_name}')
                plugin_attribute[option_name] = loaded_plugin[user_selection].PLUGIN_METADATA[option_name]
            except Exception as e:
                logging.debug(str(e))
                plugin_attribute[option_name] = hpyc.OFF
        if plugin_attribute["fullwidth_symbol"] == hpyc.ON:
            plugin_attribute["help"] = plugin_attribute["help"].replace(",", "，").replace(".", "。").replace(
                "'", "‘").replace('"', '”').replace('(', '（').replace(')', '）')

        return plugin_attribute

    def menuBar(self, *triggers):
        """
        菜单栏触发函数

        :param triggers:
        :return:
        """

        def showAbout():  # 菜单栏 关于作者
            self.ui.output_box.setPlainText(Doc.START_SHOW)

        def showTODO():  # 菜单栏 更新展望
            self.ui.output_box.setPlainText(Doc.TODO)

        def showDONE():  # 菜单栏 更新日志
            self.ui.output_box.setPlainText(Doc.UPDATE_LOG)

        def quitEvent():  # 菜单栏退出事件
            self.close()
            # sys.exit(0)

        def stopCompute():
            sys.exit(0)

        def checkUpdate():
            webbrowser.open("https://github.com/HowieHz/hpyculator/releases")

        def resetSaveLocation():
            with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
                setting_file['save_location'] = os.path.join(os.getcwd(), 'Output')

        def openSettingWindow():
            self.setting_window = SettingApplication()  # 绑定子窗口
            self.setting_window.exec()
            with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
                self.OUTPUT_DIR_PATH = setting_file['save_location']
                self.save_settings = setting_file['save_settings']
            return

        logging.debug(triggers)
        logging.debug(triggers[0].text() + 'is triggered')
        jump_map = {"终止当前运算": stopCompute,
                    "退出程序": quitEvent,
                    "重置保存路径": resetSaveLocation,
                    "更新日志": showDONE,
                    "更新展望": showTODO,
                    "开屏介绍": showAbout,
                    "检查更新": checkUpdate,
                    "设置": openSettingWindow}
        jump_map[triggers[0].text()]()

    def saveCheckEvent(self):
        """
        当触发保存选项（那个√）事件

        :return: None
        """
        if self.save_settings:  # 保存check设置
            with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
                setting_file['save_check'] = self.ui.save_check.isChecked()

    def outputOptimizationCheckEvent(self):
        """
        当触发优化输出选项

        :return: None
        """
        if self.ui.output_optimization_check.isChecked():
            if self.save_settings:  # 保存check设置
                with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
                    setting_file['output_optimization'] = self.ui.output_optimization_check.isChecked()
        else:
            self.ui.output_lock_maximums_check.setChecked(False)
            if self.save_settings:  # 保存check设置
                with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
                    setting_file['output_lock_maximums'] = False
                    setting_file['output_optimization'] = self.ui.output_optimization_check.isChecked()

    def outputLockMaximumsCheckEvent(self):
        """
        当触发锁内框输出上限选项，开启锁上限需要同时开启输出优化

        :return: None
        """
        if self.ui.output_lock_maximums_check.isChecked():
            self.ui.output_optimization_check.setChecked(True)
            if self.save_settings:  # 保存check设置
                with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
                    setting_file['output_optimization'] = True
                    setting_file['output_lock_maximums'] = self.ui.output_lock_maximums_check.isChecked()  # True
        else:
            if self.save_settings:  # 保存check设置
                with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
                    setting_file['output_lock_maximums'] = self.ui.output_lock_maximums_check.isChecked()  # False

    def searchText(self):
        """
        搜索框字符修改后触发的事件

        :return: None
        """
        search_keyword = self.ui.search_box.toPlainText()
        logging.debug(f"search_keyword:{search_keyword}")

        if search_keyword == "":
            self.searchCancel()
            return None

        self.ui.choices_list_box.clear()  # 清空选择栏

        for i in self.selection_list:  # 选出符合要求的
            if i.find(search_keyword) == -1:  # 字符串方法，没找到指定子串就-1
                continue
            else:
                self.ui.choices_list_box.addItem(i)
        return None

    def searchCancel(self):
        """
        取消搜索结果，显示全部插件

        :return: None
        """
        self.ui.choices_list_box.clear()
        self.ui.choices_list_box.addItems(self.selection_list)
        return None


if __name__ == '__main__':
    GLOBAL_SETTING_FILE_PATH, GLOBAL_OUTPUT_DIR_PATH = pathCheck()  # 路径检查
    logCheck(GLOBAL_SETTING_FILE_PATH)  # 日志检查
    global_plugin_filename_option_name_map, global_loaded_plugin = pluginCheak()  # 插件加载

    app = QApplication([])  # 启动一个应用
    window = Application(GLOBAL_SETTING_FILE_PATH, GLOBAL_OUTPUT_DIR_PATH, global_plugin_filename_option_name_map, global_loaded_plugin)  # 实例化主窗口

    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出
