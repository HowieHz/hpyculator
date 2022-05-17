import os
import shelve
import sys
import webbrowser
import hpyculator as hpyc

from ctypes import cdll
from ctypes.wintypes import HWND

from .. import document as doc

import logging  # 日志导入
from ..plugin_manager import instance_plugin_manager  # 插件管理
from ..calculate_manager import CalculationManager  # 计算管理

# pyside6 ui signal导入
from PySide6.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QGraphicsBlurEffect
from PySide6.QtGui import QTextCursor, QColor, QPainter
from PySide6.QtCore import Qt
from ..ui import Ui_MainWindow
from hpyculator.hpysignal import main_window_signal

# 窗口管理类（用于管理设置的窗口）
from . import SettingWindowApplication


class MainWindowApplication(QMainWindow):
    def __init__(self, setting_file_path, output_dir_path, plugin_option_id_dict):
        """
        主窗口程序类

        :param setting_file_path: 用于修改设置 设置文件路径
        :param output_dir_path:  用于输出结果 输出路径
        :param plugin_option_id_dict:  用于添加左侧选项
        """
        # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
        self.SETTING_FILE_PATH = setting_file_path
        self.OUTPUT_DIR_PATH = output_dir_path
        self.plugin_option_id_dict = plugin_option_id_dict  # 选项名映射id（文件或文件夹名）
        self.selection_list = plugin_option_id_dict.keys()  # 选项名列表
        self.user_selection_id: str = ""  # 用户选择的插件的文件名（id)

        super().__init__()
        self.ui = Ui_MainWindow()  # UI类的实例化()
        self.ui.setupUi(self)  # ui初始化
        self.bindSignalWithSlots()  # 信号和槽的绑定
        self.main_window_signal = main_window_signal  # 更方便地使用自定义事件
        self.setWindowTitle("hpyculator %s" % doc.VERSION)  # 设置标题

        # 读取设置文件-按钮状态和输出目录  check控件初始化
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:
            if "is_save_settings" in setting_file:
                self.is_save_settings = setting_file["is_save_settings"]  # 是否保存设置
                if self.is_save_settings:  # 当保存check状态
                    for sequence in [
                        ("save_check", False, self.ui.save_check),  # 键名 初始化状态 对应check控件
                        (
                            "output_optimization",
                            True,
                            self.ui.output_optimization_check,
                        ),
                        (
                            "output_lock_maximums",
                            True,
                            self.ui.output_lock_maximums_check,
                        ),
                    ]:
                        if sequence[0] in setting_file:
                            sequence[2].setChecked(
                                setting_file[sequence[0]]
                            )  # 根据数据设置选项状态
                        else:
                            setting_file[sequence[0]] = sequence[1]  # 初始化设置文件中对应的项
                            sequence[2].setChecked(sequence[1])  # 初始化控件
                else:  # 当不保存check状态
                    for sequence in [
                        ("save_check", False, self.ui.save_check),  # 键名 初始化状态 对应check控件
                        (
                            "output_optimization",
                            True,
                            self.ui.output_optimization_check,
                        ),
                        (
                            "output_lock_maximums",
                            True,
                            self.ui.output_lock_maximums_check,
                        ),
                    ]:
                        sequence[2].setChecked(sequence[1])  # 初始化控件
            else:
                setting_file["is_save_settings"] = False  # 默认不保存按键状态
                self.is_save_settings = False  # 默认不保存按键状态

        self.is_thread_running = [False]  # 防止反复启动计算线程

        # 关于gui显示内容的初始化
        self.ui.choices_list_box.addItems(
            self.plugin_option_id_dict.keys()
        )  # 选项名添加到ui上
        self.ui.output_box.setPlainText(doc.START_SHOW)  # 开启的展示
        self.ui.search_box.setPlaceholderText("输入字符自动进行搜索\n清空搜索框显示全部插件")  # 灰色背景提示字符
        self.ui.search_box.clear()  # 不清空不显示灰色背景
        self.ui.input_box.setFocus()  # 设置焦点

        # op = QGraphicsOpacityEffect()
        # # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        # op.setOpacity(0.1)
        # self.ui.output_box.setGraphicsEffect(op)
        # self.ui.output_box.setAutoFillBackground(True)
        #
        # op2 = QGraphicsBlurEffect()
        # op2.setBlurRadius(12)
        # self.setGraphicsEffect(op2)




    #     # 去除边框
    #     self.setWindowFlags(Qt.FramelessWindowHint)
    #     # 背景透明
    #     self.setAttribute(Qt.WA_TranslucentBackground)
    # #     # 设置背景色
    # #     # # self.bgColor = QColor(255, 50, 50, 80)  # 可以根据个人需要调节透明度
    #     self.bgColor = QColor(255, 255, 255, 50)  # 可以根据个人需要调节透明度
    # #
    #     # 调用api
    #     hWnd = HWND(int(self.winId()))  # 直接HWND(self.winId())会报错
    #     cdll.LoadLibrary(r'builtin_modules\ui_manager\Aero\aeroDll.dll').setBlur(hWnd)  # dll和脚本放在同一个目录下会报错找不到dll
    #     #出自 https://www.cnblogs.com/zhiyiYo/p/14643855.html
    # #
    # #
    # def paintEvent(self, e):
    #     """ 绘制背景,添加上一层蒙版 """
    #     painter = QPainter(self)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     painter.setPen(Qt.NoPen)
    #     painter.setBrush(self.bgColor)
    #     painter.drawRoundedRect(self.rect(), 20, 20)

    def bindSignalWithSlots(self):
        """
        绑定信号和槽

        :return:
        """
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

        def getOutPut():
            hpyc.setOutPutData(self.ui.output_box.toPlainText())

        def setStartButtonText(msg: str):
            self.ui.start_button.setText(msg)

        def setStartButtonState(state: bool):
            self.ui.start_button.setEnabled(state)

        def setOutPutBoxCursor(where: str):  # 目前只有end
            cursor = self.ui.output_box.textCursor()
            cursor_state_map = {"end": QTextCursor.End}
            cursor.movePosition(cursor_state_map[where])
            # https://doc.qt.io/qtforpython-5/PySide2/QtGui/QTextCursor.html#PySide2.QtGui.PySide2.QtGui.QTextCursor.MoveOperation
            self.ui.output_box.setTextCursor(cursor)

        # 自定义信号绑定函数
        main_window_signal.appendOutPutBox.connect(appendOutPut)
        main_window_signal.setOutPutBox.connect(setOutPut)
        main_window_signal.clearOutPutBox.connect(clearOutPut)
        main_window_signal.getOutPutBox.connect(getOutPut)
        main_window_signal.setStartButtonText.connect(setStartButtonText)
        main_window_signal.setStartButtonState.connect(setStartButtonState)
        main_window_signal.setOutPutBoxCursor.connect(setOutPutBoxCursor)

    def startEvent(
        self,
        test_input=None,
        test_input_mode=None,
        test_calculation_mode=None,
        test_selection_id=None,
        test_output_dir_path=None,
    ) -> None:
        """
        输入检查，启动计算线程

        :param test_input: 测试输入，测试专用
        :param test_input_mode: 测试模式，测试专用
        :param test_calculation_mode: 测试模式，测试专用
        :param test_selection_id: 测试选择id，测试专用
        :param test_output_dir_path: 测试专用，测试目录
        :return:
        """
        # 输入数据
        if test_input:
            input_data = test_input  # 有就录入测试数据
        else:
            input_data = self.ui.input_box.toPlainText()  # 没有就从输入框获取
            # 输入检查
            if input_data == "update_log":  # update_log检测
                self.ui.output_box.setPlainText(doc.UPDATE_LOG)
                return
            if input_data == "":  # 是否输入检测
                self.ui.output_box.setPlainText(
                    """                                                  ↑
                                                  ↑上面的就是输入框了
不输要算什么我咋知道要算啥子嘞     ↑
         → → → → → → → → → →  ↑
         ↑
请在上面的框输入需要被处理的数据

如果忘记了输入格式，只要再次选择运算核心就会显示了（· ω ·）"""
                )
                return

        # 选择的插件id
        if test_selection_id:
            user_selection_id = test_selection_id
        else:
            user_selection_id = (
                self.user_selection_id
            )  # 被用户选择的插件，这个插件的id为user_selection_id
            if self.ui.choices_list_box.currentItem() is None:  # 是否选择检测
                self.ui.output_box.setPlainText(
                    """\n\n
不选要算什么我咋知道要算啥子嘞

请在左侧选择运算核心
          ↓
← ← ←"""
                )
                return

        # 输入转换类型
        if test_input_mode:
            input_mode = test_input_mode  # 有就录入测试数据
        else:
            input_mode = self.selected_plugin_attributes["input_mode"]  # 没有就从属性列表获取

        # 计算运行模式
        if test_calculation_mode:
            calculation_mode = test_calculation_mode  # 有就录入测试数据
        else:
            if self.ui.save_check.isChecked():  # 检测保存按钮的状态判断是否保存
                calculation_mode = "calculate_save"
            else:  # 选择不保存才输出结果
                if self.ui.output_optimization_check.isChecked():
                    if self.ui.output_lock_maximums_check.isChecked():
                        calculation_mode = "calculate_o_l"  # l=limit
                    else:
                        calculation_mode = "calculate_o"
                else:
                    calculation_mode = "calculate"

        if test_output_dir_path:
            output_dir_path = test_output_dir_path
        else:
            output_dir_path = self.OUTPUT_DIR_PATH
        # 以上是计算前工作
        logging.debug("启动计算")
        calculate_manager = CalculationManager()
        calculate_manager.start(
            input_data, input_mode, calculation_mode, user_selection_id, output_dir_path
        )  # 启动计算
        return

    def userChooseOptionEvent(self, item):
        """
        左侧选择算法之后触发的函数 选择算法事件

        :param item:
        :return: None
        """
        # logging.debug(f'选中的选项名{self.ui.choices_list_box.currentItem().text()}')
        logging.debug(f"选中的选项名{item.text()}")
        self.user_selection_id = str(self.plugin_option_id_dict[item.text()])  # 转换成ID
        self.selected_plugin_attributes = (
            selected_plugin_attributes
        ) = instance_plugin_manager.getPluginAttribute(self.user_selection_id)

        self.ui.output_box.setPlainText(
            f"""\
{selected_plugin_attributes["output_start"]}
{selected_plugin_attributes["output_name"]} {selected_plugin_attributes["version"]}
by {selected_plugin_attributes["author"]}


使用提示
{selected_plugin_attributes["help"]}

{selected_plugin_attributes["output_end"]}"""
        )

    def menuBar(self, *triggers):
        """
        菜单栏触发函数

        :param triggers:
        :return:
        """

        def showAbout():  # 菜单栏 关于作者
            self.ui.output_box.setPlainText(doc.START_SHOW)

        def showTODO():  # 菜单栏 更新展望
            self.ui.output_box.setPlainText(doc.TODO)

        def showDONE():  # 菜单栏 更新日志
            self.ui.output_box.setPlainText(doc.UPDATE_LOG)

        def quitEvent():  # 菜单栏退出事件
            self.close()
            # sys.exit(0)

        def checkUpdate():
            webbrowser.open("https://github.com/HowieHz/hpyculator/releases")


        logging.debug(triggers)
        logging.debug(triggers[0].text() + "is triggered")
        jump_map = {
            "更新日志": showDONE,
            "更新展望": showTODO,
            "开屏介绍": showAbout,
            "检查更新": checkUpdate,
        }
        jump_map[triggers[0].text()]()

    def quitEvent(self):
        """
        退出程序

        :return:
        """
        sys.exit(0)

    def openSettingWindowEvent(self):
        """
        打开设置窗口

        :return:
        """
        self.setting_window = SettingWindowApplication()  # 绑定子窗口
        self.setting_window.exec()
        with shelve.open(
                self.SETTING_FILE_PATH, writeback=True
        ) as setting_file:  # 读取设置文件
            self.OUTPUT_DIR_PATH = setting_file["save_location"]
            self.is_save_settings = setting_file["is_save_settings"]

    def saveCheckEvent(self):
        """
        当触发保存选项（那个√）事件

        :return: None
        """
        if self.is_save_settings:  # 保存check设置
            with shelve.open(
                self.SETTING_FILE_PATH, writeback=True
            ) as setting_file:  # 读取设置文件
                setting_file["save_check"] = self.ui.save_check.isChecked()

    def outputOptimizationCheckEvent(self):
        """
        当触发优化输出选项

        :return: None
        """
        if self.ui.output_optimization_check.isChecked():
            if self.is_save_settings:  # 保存check设置
                with shelve.open(
                    self.SETTING_FILE_PATH, writeback=True
                ) as setting_file:  # 读取设置文件
                    setting_file[
                        "output_optimization"
                    ] = self.ui.output_optimization_check.isChecked()
        else:
            self.ui.output_lock_maximums_check.setChecked(False)
            if self.is_save_settings:  # 保存check设置
                with shelve.open(
                    self.SETTING_FILE_PATH, writeback=True
                ) as setting_file:  # 读取设置文件
                    setting_file["output_lock_maximums"] = False
                    setting_file[
                        "output_optimization"
                    ] = self.ui.output_optimization_check.isChecked()

    def outputLockMaximumsCheckEvent(self):
        """
        当触发锁内框输出上限选项，开启锁上限需要同时开启输出优化

        :return: None
        """
        if self.ui.output_lock_maximums_check.isChecked():
            self.ui.output_optimization_check.setChecked(True)
            if self.is_save_settings:  # 保存check设置
                with shelve.open(
                    self.SETTING_FILE_PATH, writeback=True
                ) as setting_file:  # 读取设置文件
                    setting_file["output_optimization"] = True
                    setting_file[
                        "output_lock_maximums"
                    ] = self.ui.output_lock_maximums_check.isChecked()  # True
        else:
            if self.is_save_settings:  # 保存check设置
                with shelve.open(
                    self.SETTING_FILE_PATH, writeback=True
                ) as setting_file:  # 读取设置文件
                    setting_file[
                        "output_lock_maximums"
                    ] = self.ui.output_lock_maximums_check.isChecked()  # False

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
            self.ui.choices_list_box.addItem(i)
        return None

    def searchCancel(self):
        """
        取消搜索结果，显示全部插件

        :return: None
        """
        self.ui.choices_list_box.clear()
        self.ui.choices_list_box.addItems(self.selection_list)
