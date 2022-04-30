import datetime
import os
import shelve
import time
import threading
import sys
import importlib
import webbrowser
import hpyculator
import tempfile
from functools import partial#偏函数真好用
import pyperclip
#import jpype
#import pprint

#日志导入
import logging
# 检查存放日志文件的文件夹是否存在
LOG_FILE_PATH=os.path.join(os.getcwd(), 'Log')
if os.path.exists(LOG_FILE_PATH):
    pass
else:
    os.makedirs(LOG_FILE_PATH)
logging.basicConfig(filename=os.path.join(LOG_FILE_PATH,'log.txt'),level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)#禁用日志
logging.debug('Start of program')

#文档导入
import Doc
import Version

#pyside6导入
from PySide6.QtWidgets import QApplication, QMainWindow
# PySide6-uic demo.ui -o ui_demo.py
# from ui_demo import Ui_Demo
from SettingWindow import SettingApplication

from ui.MainWindow import Ui_MainWindow
from ui.Signal import main_window_signal

# 主类
class Application(QMainWindow):
    # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
    def __init__(self):
        # setting_file - 配置文件ShelfFile对象
        logging.debug('主类初始化')
        super().__init__()
        self.ui = Ui_MainWindow()  # UI类的实例化()
        self.ui.setupUi(self)
        self.band()#信号和槽的绑定

        self.main_window_signal=main_window_signal#更方便的使用自定义事件

        self.setWindowTitle("各类数组计算程序%s-Howie皓子制作" % Version.VERSION)#设置标题


        # 初始化设置目录
        self.SETTING_DIR_PATH = str(os.path.join(os.getcwd(), 'Setting'))
        logging.debug(f'设置文件保存位置:{self.SETTING_DIR_PATH}')
        # 初始化设置文件位置
        self.SETTING_FILE_PATH = str(os.path.join(self.SETTING_DIR_PATH, 'hpyculator_setting'))

        # 检查存放设置文件的文件夹是否存在
        if os.path.exists(self.SETTING_DIR_PATH):
            pass
        else:
            os.makedirs(self.SETTING_DIR_PATH)

        # 读取设置文件
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:
            try:
                self.ui.save_check.setChecked(setting_file['save_check'])  # 根据数据设置选项状态
            except Exception:
                setting_file['save_check'] = self.ui.save_check.isChecked()
            try:
                self.ui.output_optimization_check.setChecked(setting_file['output_optimization'])  # 根据数据设置选项状态
            except Exception:
                setting_file['output_optimization'] = True
                self.ui.output_optimization_check.setChecked(True)
            try:
                self.ui.output_lock_maximums_check.setChecked(setting_file['output_lock_maximums'])  # 根据数据设置选项状态
            except Exception:
                setting_file['output_lock_maximums'] = True
                self.ui.output_lock_maximums_check.setChecked(True)

            # 初始化文件输出目录
            try:
                self.OUTPUT_DIR_PATH = setting_file['save_location']
            except Exception:
                self.OUTPUT_DIR_PATH = str(os.path.join(os.getcwd(), 'Output'))
                setting_file['save_location'] = self.OUTPUT_DIR_PATH
            logging.debug(f'输出文件保存位置:{self.OUTPUT_DIR_PATH}')

        # 检查输出文件夹是否存在
        if os.path.exists(self.OUTPUT_DIR_PATH):
            pass
        else:
            os.makedirs(self.OUTPUT_DIR_PATH)

        # 初始化模块目录
        self.PLUGIN_DIR_PATH=str(os.path.join(os.getcwd(),'Plugin'))
        logging.debug(f'插件保存位置:{self.PLUGIN_DIR_PATH}')

        # 检查模块文件夹是否存在
        if os.path.exists(self.PLUGIN_DIR_PATH):
            pass
        else:
            os.makedirs(self.PLUGIN_DIR_PATH)



        #载入模块
        self.plugin_files_name=[]#Plugin目录下读取到的文件
        self.plugin_files_name_folder= []#Plugin目录下读取到的有__init__.py的文件夹
        self.can_choose_number = []#选择列表，储存着所有的选项名
        self.plugin_files_name_py=[]#储存着
        self.plugin_filename_option_name_map = {}#选项名和实际文件名的映射表
        self.readPlugin(self.PLUGIN_DIR_PATH)#读

        # 从所有读取的文件中挑选出.py为后缀的文件
        try:
            for i_list in self.plugin_files_name:
                if (i_list[0].split("."))[-1] == "py":
                    if not self.plugin_files_name_py:  # 第一遍空列表才写入
                        self.plugin_files_name_py = i_list
        #这行bug很多，小心
        except Exception as e:
            pass

        #加载插件
        try:
            self.init_plugin_singerfile()#导入单文件插件
        except Exception as e:
            logging.debug(f'init_plugin_singerfile outside Exception:{e}')

        try:
            self.init_plugin_folder()#导入文件插件
        except Exception as e:
            logging.debug(f'init_plugin_folder outside Exception:{e}')


        self.ui.choices_list_box.addItems(self.can_choose_number)#选项名添加到ui上

        self.is_thread_runing = False#防止两个计算线程同时进行

        # 关于gui显示内容的初始化
        self.ui.output_box.setPlainText(Doc.START_SHOW)  # 开启的展示

    def band(self):
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)

        #my_signal.setProgressBar.connect(self.set_progress_bar)

        #my_signal.setResult.connect(self.set_result)
        def appendOutPut(msg: str):
            self.ui.output_box.appendPlainText(msg)

        def clearOutPut():
            self.ui.output_box.clear()

        def setOutPut(msg: str):
            self.ui.output_box.setPlainText(msg)
        main_window_signal.appendOutPutBox.connect(appendOutPut)

        main_window_signal.setOutPutBox.connect(setOutPut)

        main_window_signal.clearOutPutBox.connect(clearOutPut)

    def init_plugin_singerfile(self):
        self.plugin_files_name_py_nopy = self.plugin_files_name_py[:]
        for index,value in enumerate(self.plugin_files_name_py_nopy):  # 去掉.py后缀
            self.plugin_files_name_py_nopy[index] = value[:-3]
        logging.debug(f"去掉.py后缀的文件名 {self.plugin_files_name_py_nopy}")
        for name in self.plugin_files_name_py_nopy:
            exec(f"self.{name}=importlib.import_module('.{name}', package='Plugin')")
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            try:
                exec(
                    f"self.can_choose_number.append(self.{name}.PLUGIN_METADATA['option_name'])")  # 读取模块元数据，添加gui选项
                exec(
                    f"self.plugin_filename_option_name_map[self.{name}.PLUGIN_METADATA['option_name']]=self.{name}.PLUGIN_METADATA['id']")
            except Exception as e:
                logging.debug(f'init_plugin_singerfile inside Exception:{e}')

    def init_plugin_folder(self):
        logging.debug(f"读取到的文件夹插件:{self.plugin_files_name_folder}")
        for name in self.plugin_files_name_folder:
            exec(f"self.{name}=importlib.import_module('.{name}.__init__', package='Plugin')")
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            try:
                exec(
                    f"self.can_choose_number.append(self.{name}.PLUGIN_METADATA['option_name'])")  # 读取模块元数据，添加gui选项
                exec(
                    f"self.plugin_filename_option_name_map[self.{name}.PLUGIN_METADATA['option_name']]=self.{name}.PLUGIN_METADATA['id']")
            except Exception as e:
                logging.debug(f'init_plugin_folder inside Exception:{e}')

    #读取指定目录下插件 #需重构
    def readPlugin(self,path):
        for root, dir, file in os.walk(path):
            self.plugin_files_name.append(file)
            # print("root:"+str(root))
            # print("root[:11]"+str(root)[:11])
            # print("root[:9]" + str(root)[:9])
            # print("root[,]"+str(str(root).split("\\")))
            # print("dir:"+str(dir))
            # print("file:"+str(file))
            # print("------")
            root_list=str(root).split("\\")
            #print(root_list)
            if root_list[-2]=='Plugin':
                #root[,]['C:', 'Users', 'Howie-MacBookPro', 'Documents', 'ProgramDevelopment', 'hpyculator', 'src', 'Plugin', 'Prime_Palindromes_fix']
                if '__init__.py' in file:
                    self.plugin_files_name_folder.append(root_list[-1])

    #初始化计算，绑定计算按钮，启动计算线程
    def startEvent(self):
        # self.input_box_s_input - 储存输入框的内容
        # self.time_before_calculate,self.time_after_calculate - 临时储存时间，计录 计算时间
        # self.result_process  - 储存计算结果 （用于for循环,就是个i
        # self.result_last  - 储存计算结果

        if str(self.ui.input_box.toPlainText()) == "update_log":  # update_log检测
            self.ui.output_box.setPlainText(Doc.UPDATE_LOG)
            return
        #if str(self.ui.input_box.toPlainText()) == "停止":  # u停止检测
            #main_window_signal.appendOutPutBox.emit("当前计算线程已停止")
            #self.is_thread_runing = False
            #return
        #if str(self.ui.input_box.toPlainText()) == "stop":  # stop检测
            #main_window_signal.appendOutPutBox.emit("当前计算线程已停止")
            #self.is_thread_runing = False
            #return
        if self.ui.choices_list_box.currentItem() is None:  # 是否选择检测
            self.ui.output_box.setPlainText("\n\n" +
                         """
不选要算什么我咋知道要算啥子嘞

请在左侧选择运算核心
          ↓
← ← ←""")
            return
        if self.ui.input_box.toPlainText() == "":  # 是否输入检测
            self.ui.output_box.setPlainText("""                                                  ↑
                                                  ↑上面的就是输入框了
不输要算什么我咋知道要算啥子嘞     ↑
         → → → → → → → → → →  ↑
         ↑
请在上面的框输入需要被处理的数据

如果忘记了输入格式，只要再次选择运算核心就会显示了（· ω ·）""")
            return

        if self.input_mode == 'string':
            self.input_box_s_input = self.ui.input_box.toPlainText()  # 取得输入框的数字
        elif self.input_mode == 'float':
            self.input_box_s_input = float(self.ui.input_box.toPlainText())  # 取得输入框的数字
        elif self.input_mode == 'num':
            self.input_box_s_input = int(self.ui.input_box.toPlainText())  # 取得输入框的数字
        elif self.input_mode == '0':
            self.input_box_s_input = self.ui.input_box.toPlainText()  # 取得输入框的数字
        elif self.input_mode == '1':
            self.input_box_s_input = int(self.ui.input_box.toPlainText())  # 取得输入框的数字

        #以上是计算前工作
        calculate_thread=threading.Thread(target=self.startCalculate)#启动计算线程
        calculate_thread.start()


    #计算线程
    def startCalculate(self):
        if not self.is_thread_runing:
            try:
                main_window_signal.clearOutPutBox.emit()  # 清空输出框
                main_window_signal.setOutPutBox.emit("计算程序正在运行中，所需时间较长，请耐心等待")
                if self.ui.test_check.isChecked():
                    self.whatNeedCalculateWithTest()
                    # 以下是计算后工作
                    main_window_signal.appendOutPutBox.emit(f"\n\n本次测试花费了{self.time_after_calculate - self.time_before_calculate:.6f}秒\n")  # 输出本次计算时间
                else:
                    if self.ui.save_check.isChecked():  # 检测保存按钮的状态判断是否保存
                        self.whatNeedCalculateWithSave()
                        # 以下是计算后工作
                        main_window_signal.clearOutPutBox.emit()  # 清空输出框
                        main_window_signal.appendOutPutBox.emit(f"\n本次计算+保存花费了{self.time_after_calculate - self.time_before_calculate:.6f}秒\n")  # 输出本次计算时间
                        main_window_signal.appendOutPutBox.emit("\n计算结果已保存在 " + os.path.join(self.OUTPUT_DIR_PATH,f"{self.name_text_file}.txt"))
                        main_window_signal.appendOutPutBox.emit("\n")
                    else:  # 选择不保存才输出结果
                        if self.ui.output_optimization_check.isChecked():
                            self.whatNeedCalculateWithOutputOptimization()
                            # 以下是计算后工作
                            main_window_signal.appendOutPutBox.emit(f"\n\n本次计算+输出花费了{self.time_after_calculate - self.time_before_calculate:.6f}秒\n")  # 输出本次计算时间
                            main_window_signal.appendOutPutBox.emit("已启用输出优化")
                        else:
                            self.whatNeedCalculate()
                            # 以下是计算后工作
                            main_window_signal.appendOutPutBox.emit(f"\n\n本次计算+输出花费了{self.time_after_calculate - self.time_before_calculate:.6f}秒\n")  # 输出本次计算时间
            except Exception as e:
                main_window_signal.clearOutPutBox.emit()  # 清空输出框
                main_window_signal.setOutPutBox.emit(str(e))
                main_window_signal.appendOutPutBox.emit("\n\n插件发生错误，请检查输入格式")

            self.is_thread_runing = False
        else:
            main_window_signal.appendOutPutBox.emit("\n运算程序正在进行中，请勿反复点击计算按钮！\n")  # 清空输出框

    def whatNeedCalculate(self):
        self.is_thread_runing = True

        self.time_before_calculate = time.perf_counter()  # 储存开始时间

        if self.output_mode == '0':
            exec(f"self.result = str(self.{self.Selection}.main(self.input_box_s_input))")
            main_window_signal.setOutPutBox.emit(str(self.result) + "\n")  # 结果为str，直接输出
        elif self.output_mode == '2': # 算一行输出一行，但是没有换行
            main_window_signal.clearOutPutBox.emit()  # 清空输出框
            exec(f"self.result=self.{self.Selection}.main(self.input_box_s_input)")
            for result_process in self.result:  # 计算
                main_window_signal.appendOutPutBox.emit(str(result_process))  # 算一行输出一行
        elif self.output_mode == '1': # 算一行输出一行
            main_window_signal.clearOutPutBox.emit()  # 清空输出框
            exec(f"self.result=self.{self.Selection}.main(self.input_box_s_input)")
            for result_process in self.result:  # 计算 啊，定义就在上一行，hoyc你是看不到吗？
                main_window_signal.appendOutPutBox.emit(str(result_process) + "\\n")  # 算一行输出一行
        elif self.output_mode == '4':
            main_window_signal.clearOutPutBox.emit() # 清空输出框
            exec(f"self.{self.Selection}.main(self.input_box_s_input,self,'output')")
        else:
            main_window_signal.clearOutPutBox.emit() # 清空输出框
            exec(f"self.{self.Selection}.main(self.input_box_s_input,self)")
        self.time_after_calculate = time.perf_counter()  # 储存结束时间

    def whatNeedCalculateWithSave(self):  # 选择检测+计算
        # self.name_text_file - 储存保存到哪个文件里
        # now - 保存datetime类型的当前时间
        self.is_thread_runing = True

        now = datetime.datetime.now()  # 保存当前时间，用于文件名

        if self.save_mode == '1':
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') + '  ' + str(self.input_box_s_input).replace('.',
                                                                                                                 '_') + "的" + self.save_name
        else:
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') +'  '+ self.save_name + str(self.input_box_s_input) + self.quantifier

        #save = open(os.path.join(os.path.abspath(self.save_location_input_box.GetValue()),self.name_text_file + ".txt"), "w", encoding="utf-8")
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:
            self.OUTPUT_DIR_PATH = setting_file['save_location']
        save = open(os.path.join(self.OUTPUT_DIR_PATH,f"{self.name_text_file}.txt"), "w",encoding="utf-8")
        self.time_before_calculate = time.perf_counter()  # 储存开始时间

        try:
            if self.output_mode == '0':  # 分布输出和一次输出
                exec(f"self.result = self.{self.Selection}.main(self.input_box_s_input)")
                save.write(str(self.result) + "\n")
            elif self.output_mode == '2':  # 算一行输出一行，但是没有换行
                exec(f"self.result=self.{self.Selection}.main(self.input_box_s_input)")
                for result_process in self.result:  # 计算
                    save.write(str(result_process))
                    save.flush()  # 算出来就存进去
            elif self.output_mode == '1':  # 算一行输出一行，但是没有换行
                exec(f"self.result=self.{self.Selection}.main(self.input_box_s_input)")
                for result_process in self.result:  # 计算
                    save.write(str(result_process) + "\\n")
                    save.flush()  # 算出来就存进去
            elif self.output_mode == '4':
                exec(f"self.{self.Selection}.main(self.input_box_s_input,save,'save')")
            else:
                exec(f"self.{self.Selection}.main_save(self.input_box_s_input,save)")
        finally:
            save.close()

        self.time_after_calculate = time.perf_counter()  # 储存结束时间

    def whatNeedCalculateWithOutputOptimization(self):
        # self.name_text_file - 储存保存到哪个文件里
        # now - 保存datetime类型的当前时间
        self.is_thread_runing = True

        now = datetime.datetime.now()  # 保存当前时间，用于文件名

        with tempfile.TemporaryFile('w+t', encoding='utf-8', errors='ignore') as save:
            self.time_before_calculate = time.perf_counter()  # 储存开始时间

            try:
                if self.output_mode == '0':  # 分布输出和一次输出
                    exec(f"self.result = self.{self.Selection}.main(self.input_box_s_input)")
                    save.write(str(self.result) + "\n")
                elif self.output_mode == '2':  # 算一行输出一行，但是没有换行
                    exec(f"self.result=self.{self.Selection}.main(self.input_box_s_input")
                    for result_process in self.result:  # 计算
                        save.write(str(result_process))
                        save.flush()  # 算出来就存进去
                elif self.output_mode == '1':  # 算一行输出一行，但是没有换行
                    exec(f"self.result=self.{self.Selection}.main(self.input_box_s_input")
                    for result_process in self.result:  # 计算
                        save.write(str(result_process) + "\\n")
                        save.flush()  # 算出来就存进去
                elif self.output_mode == '4':
                    exec(f"self.{self.Selection}.main(self.input_box_s_input,save,'save')")
                else:
                    exec(f"self.{self.Selection}.main_save(self.input_box_s_input,save)")
            finally:
                main_window_signal.clearOutPutBox.emit()  # 清空输出框
                save.seek(0)# 将文件指针移到开始处，准备读取文件
                if self.ui.output_lock_maximums_check.isChecked():
                    for times,line in enumerate(self.quickTraverseFile(save)):
                        main_window_signal.appendOutPutBox.emit(line)
                        if times>=128:
                            main_window_signal.appendOutPutBox.emit("\n\n输出上限：检测到输出数据过大，请使用保存到文件防止卡死")
                            break
                else:
                    for line in self.quickTraverseFile(save):
                        main_window_signal.appendOutPutBox.emit(line)

        self.time_after_calculate = time.perf_counter()  # 储存结束时间

    #快读，低占用读取文件
    def quickTraverseFile(self,file,chunk_size=8192):
        for chunk in iter(partial(file.read,chunk_size), ''):#用readline的话，读到换行符就会直接停止读取，不会读取到8192B，会增加读取次数
            yield chunk

    def whatNeedCalculateWithTest(self):
        self.is_thread_runing = True

        try:
            if self.output_mode == '4':
                main_window_signal.clearOutPutBox.emit() # 清空输出框

                self.time_before_calculate = time.perf_counter()  # 储存开始时间
                exec(f"self.{self.Selection}.main(self.input_box_s_input,self,'test')")
                self.time_after_calculate = time.perf_counter()  # 储存结束时间
                if self.ui.output_box.toPlainText() != "":
                    main_window_signal.clearOutPutBox.emit() # 清空输出框
                    main_window_signal.setOutPutBox.emit("发生错误，请检查输入格式，以及插件是否有test模式")
            else:
                main_window_signal.clearOutPutBox.emit() # 清空输出框

                self.time_before_calculate = time.perf_counter()  # 储存开始时间
                exec(f"self.{self.Selection}.main_test(self.input_box_s_input,self)")
                self.time_after_calculate = time.perf_counter()  # 储存结束时间
        except Exception:
            self.time_after_calculate = time.perf_counter()  # 储存结束时间
            main_window_signal.setOutPutBox.emit("发生错误，请检查输入格式，以及插件是否有test模式")

    def chooseNumberEvent(self,item):  # 选择算法事件
        #logging.debug(f'选中的选项名{self.ui.choices_list_box.currentItem().text()}')
        logging.debug(f'选中的选项名{item.text()}')
        self.Selection = self.plugin_filename_option_name_map[item.text()]

        # self.required_parameters = ['input_mode','output_mode','save_name','output_name','save_mode','version']
        # self.optional_parameters=['output_start', 'quantifier', 'author', 'help', 'output_end', 'fullwidth_symbol']
        # self.parameters_list = ['output_start', 'quantifier', 'author', 'help', 'output_end', 'fullwidth_symbol','input_mode','output_mode','save_name','output_name','save_mode','version']
        # self.required_parameters.extend(self.optional_parameters)
        for option_name in ['output_start', 'quantifier', 'author', 'help', 'output_end', 'fullwidth_symbol', 'input_mode','output_mode', 'save_name', 'output_name', 'save_mode', 'version']:
            try:
                exec(f"self.{option_name}=str(self.{self.Selection}.PLUGIN_METADATA['{option_name}'])")
            except Exception:
                exec(f"self.{option_name}=''")
        if self.fullwidth_symbol == '1':
            self.help = self.help.replace(",", "，").replace(".", "。").replace("'", "‘").replace('"', '”').replace('(','（').replace(')', '）')
        self.ui.output_box.setPlainText(f"""\
{self.output_start}
{self.output_name} {self.version}
by {self.author}


使用提示
{self.help}

{self.output_end}""")

    #菜单栏触发函数
    def menuBar(self,triggeres):
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

        def cheakUpdate():
            webbrowser.open("https://github.com/HowieHz/hpyculator/releases")

        def resetSaveLocation():
            with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
                setting_file['save_location'] = os.path.join(os.getcwd(),'Output')

        def openSettingWindow():
            self.setting_window = SettingApplication()
            self.setting_window.show()
            # 读取设置文件
            return

        logging.debug(triggeres.text() + 'is triggeres')
        jump_map = {"终止当前运算": stopCompute,
                    "退出程序": quitEvent,
                    "重置保存路径": resetSaveLocation,
                    "更新日志": showDONE,
                    "更新展望": showTODO,
                    "开屏介绍": showAbout,
                    "检查更新": cheakUpdate,
                    "设置": openSettingWindow}
        jump_map[triggeres.text()]()

    # 当触发保存选项（那个√）事件
    def saveCheckEvent(self):
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
            setting_file['save_check'] = self.ui.save_check.isChecked()
        if self.ui.test_check.isChecked():
            self.ui.test_check.setChecked(False)
        else:
            pass

    # 当触发测试选项
    def testCheckEvent(self):#test开就不报存
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
            if self.ui.save_check.isChecked():
                self.ui.save_check.setChecked(False)
                setting_file['save_check'] = False
            else:
                pass

    # 当触发优化输出选项
    def outputOptimizationCheckEvent(self):
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
            if self.ui.output_optimization_check.isChecked():
                pass
            else:
                self.ui.output_lock_maximums_check.setChecked(False)
                setting_file['output_lock_maximums'] = False
            setting_file['output_optimization'] = self.ui.output_optimization_check.isChecked()

    # 当触发锁内框输出上限选项
    def outputLockMaximumsCheckEvent(self):#锁上限开，就要开优化
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
            if self.ui.output_lock_maximums_check.isChecked():
                self.ui.output_optimization_check.setChecked(True)
                setting_file['output_optimization'] = True
                setting_file['output_lock_maximums'] = self.ui.output_lock_maximums_check.isChecked()#True
            else:
                setting_file['output_lock_maximums'] = self.ui.output_lock_maximums_check.isChecked()#False

    # 搜索框
    def search_text(self): # 搜索框字符修改后触发的事件
        self.search_keyword = self.ui.search_box.toPlainText()
        logging.debug(f"search_keyword:{self.search_keyword}")

        if self.search_keyword=="":
            self.search_cancel()
            return

        try:#清空选择栏
            self.ui.choices_list_box.clear()
        except Exception:
            pass

        for i in self.can_choose_number:#选出符合要求的
            if i.find(self.search_keyword)==-1:#字符串方法，没找到指定子串就-1
                continue
            else:
                self.ui.choices_list_box.addItem(i)

        return

    def search_cancel(self):#取消搜索结果，显示全部插件
        try:
            self.ui.choices_list_box.clear()
        except Exception:
            pass
        self.ui.choices_list_box.addItems(self.can_choose_number)
        return

if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = Application()  # 实例化主窗口

    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出