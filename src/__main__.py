import datetime
import os
import shelve
import time
import wx
import threading
import sys
import importlib
import webbrowser
import hpyculator
import tempfile
from functools import partial#偏函数真好用
#import jpype
#import pprint

import MainWin
import Doc
import Version

class Application(MainWin.MainWindow):  # 主类

    def __init__(self):
        # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
        # setting_file - 配置文件ShelfFile(\皓式程序设置\hpyculator_setting)

        super().__init__()

        if os.path.exists(os.path.abspath(r'.\皓式程序设置')):
            pass
        else:
            os.makedirs(os.path.abspath(r'.\皓式程序设置'))
        if os.path.exists(os.path.abspath(r'.\皓式程序输出')):
            pass
        else:
            os.makedirs(os.path.abspath(r'.\皓式程序输出'))
        if os.path.exists(os.path.abspath(r'.\Plugin')):
            pass
        else:
            os.makedirs(os.path.abspath(r'.\Plugin'))



        #载入模块
        self.plugin_files_name=[]
        self.plugin_files_name_folder= []
        self.can_choose_number = []
        self.plugin_files_name_py=[]
        self.plugin_filename_option_name_map = {}
        self.readPlugin(r'.\Plugin')
        #pprint.pprint("读取到Plugin文件夹下文件:")
        #pprint.pprint(self.plugin_files_name)#读取到Plugin下面的文件
        #pprint.pprint("读取到的文件夹插件:")
        #pprint.pprint(self.plugin_files_name_folder)
        try:
            for i_list in self.plugin_files_name:#从所有读取的文件中挑选出.py为后缀的文件
                if (i_list[0].split("."))[-1] == "py":
                    if not self.plugin_files_name_py:  # 第一遍空列表才写入
                        self.plugin_files_name_py = i_list
        #这行bug很多，小心
        except Exception as e:
            pass

        #pprint.pprint("读取到的.py文件:")
        #pprint.pprint(self.plugin_files_name_py)
        try:
            self.init_plugin_singerfile()#导入单文件插件
        except Exception:
            pass

        try:
            self.init_plugin_folder()#导入文件插件
        except Exception:
            pass

        self.list_box.Append(self.can_choose_number)

        #print("\n\n选项和文件名（ID）映射表:")
        #pprint.pprint(self.plugin_filename_option_name_map)

        # self.events=Events()#实例化Events
        # self.mainWindow()  # 初始化窗口
        self.is_thread_runing = False

        self.save_location_input_box.SetValue(os.path.abspath(".\\皓式程序输出\\"))

        # 关于gui显示内容的初始化
        self.output.SetValue(Doc.START_SHOW)  # 开启的展示

        with shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True) as setting_file:#读取设置文件
            try:
                self.save_check.SetValue(setting_file['save_check'])  # 根据数据设置选项状态
            except Exception:
                setting_file['save_check'] = self.save_check.GetValue()

            try:
                self.save_location_input_box.SetValue(setting_file['save_location'])  # 根据数据设置选项状态
            except Exception:
                setting_file['save_location'] = self.save_location_input_box.GetValue()

            try:
                self.output_optimization_check.SetValue(setting_file['output_optimization'])  # 根据数据设置选项状态
            except Exception:
                setting_file['output_optimization'] = True
                self.output_optimization_check.SetValue(True)
            try:
                self.output_lock_maximums_check.SetValue(setting_file['output_lock_maximums'])  # 根据数据设置选项状态
            except Exception:
                setting_file['output_lock_maximums'] = True
                self.output_lock_maximums_check.SetValue(True)

    def init_plugin_singerfile(self):
        self.plugin_files_name_py_nopy = self.plugin_files_name_py[:]
        for index,value in enumerate(self.plugin_files_name_py_nopy):  # 去掉.py后缀
            self.plugin_files_name_py_nopy[index] = value[:-3]
        #pprint.pprint("去掉.py后缀的文件名")
        #pprint.pprint(self.plugin_files_name_py_nopy)
        for name in self.plugin_files_name_py_nopy:
            exec(f"self.{name}=importlib.import_module('.{name}', package='Plugin')")
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            try:
                exec(
                    f"self.can_choose_number.append(self.{name}.PLUGIN_METADATA['option_name'])")  # 读取模块元数据，添加gui选项
                exec(
                    f"self.plugin_filename_option_name_map[self.{name}.PLUGIN_METADATA['option_name']]=self.{name}.PLUGIN_METADATA['id']")
            except Exception as e:
                print(e)

    def init_plugin_folder(self):
        for name in self.plugin_files_name_folder:
            exec(f"self.{name}=importlib.import_module('.{name}.__init__', package='Plugin')")
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            try:
                exec(
                    f"self.can_choose_number.append(self.{name}.PLUGIN_METADATA['option_name'])")  # 读取模块元数据，添加gui选项
                exec(
                    f"self.plugin_filename_option_name_map[self.{name}.PLUGIN_METADATA['option_name']]=self.{name}.PLUGIN_METADATA['id']")
            except Exception as e:
                print(e)

    def readPlugin(self,path):
        for root, dir, file in os.walk(path):
            self.plugin_files_name.append(file)
            #print("root:"+str(root))
            #print("root[:11]"+str(root)[:11])
            #print("root[,]"+str(str(root).split("\\")))
            #print("dir:"+str(dir))
            #print("file:"+str(file))
            #print("------")
            if str(root)[:9]=='.\\Plugin\\':
                if '__init__.py' in file:
                    self.plugin_files_name_folder.append(str(root).split("\\")[2])


    def startEvent(self, event):
        # self.input_box_s_input - 储存输入框的内容
        # self.time_before_calculate,self.time_after_calculate - 临时储存时间，计录 计算时间
        # self.result_process  - 储存计算结果 （用于for循环,就是个i
        # self.result_last  - 储存计算结果
        with shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True) as setting_file:  # 读取设置文件
            setting_file['save_location'] = str(self.save_location_input_box.GetValue())

        if str(self.input_box.GetValue()) == "update_log":  # update_log检测
            wx.CallAfter(self.setOutPut,Doc.UPDATE_LOG)
            return
        #if str(self.input_box.GetValue()) == "停止":  # u停止检测
            #wx.CallAfter(self.setOutPut,"当前计算线程已停止")
            #self.is_thread_runing = False
            #return
        #if str(self.input_box.GetValue()) == "stop":  # stop检测
            #wx.CallAfter(self.setOutPut,"当前计算线程已停止")
            #self.is_thread_runing = False
            #return
        #print(self.list_box.GetSelection())#选择位置输出
        if self.list_box.GetSelection() == -1:  # 是否选择检测
            wx.CallAfter(self.setOutPut,"\n\n" +
                         """
不选要算什么我咋知道要算啥子嘞
                         
请在左侧选择运算核心
          ↓
← ← ←""")
            return
        if str(self.input_box.GetValue()) == "":  # 是否输入检测
            wx.CallAfter(self.setOutPut,"""                                                  ↑
                                                  ↑上面的就是输入框了
不输要算什么我咋知道要算啥子嘞     ↑
         → → → → → → → → → →  ↑
         ↑
请在上面的框输入需要被处理的数据

如果忘记了输入格式，只要再次选择运算核心就会显示了（· ω ·）""")
            return


        #以上是计算前工作
        calculate_thread=threading.Thread(target=self.startCalculate)
        calculate_thread.start()



    def startCalculate(self):
        if not self.is_thread_runing:
            try:
                wx.CallAfter(self.clearOutPut)  # 清空输出框
                wx.CallAfter(self.outPutToOutPut, "计算程序正在运行中，所需时间较长，请耐心等待")
                if self.test_check.GetValue():
                    self.whatNeedCalculateWithTest()
                    # 以下是计算后工作
                    wx.CallAfter(self.outPutToOutPut,f"\n\n本次测试花费了{self.time_after_calculate - self.time_before_calculate:.6f}秒\n")  # 输出本次计算时间
                else:
                    if self.save_check.GetValue():  # 检测保存按钮的状态判断是否保存
                        self.whatNeedCalculateWithSave()
                        # 以下是计算后工作
                        wx.CallAfter(self.clearOutPut)  # 清空输出框
                        wx.CallAfter(self.outPutToOutPut,f"\n本次计算+保存花费了{self.time_after_calculate - self.time_before_calculate:.6f}秒\n")  # 输出本次计算时间
                        wx.CallAfter(self.outPutToOutPut,"\n计算结果已保存在" + os.path.abspath(".\\皓式程序输出\\") + self.name_text_file + ".txt")
                        wx.CallAfter(self.outPutToOutPut,"\n")
                    else:  # 选择不保存才输出结果
                        if self.output_optimization_check.GetValue():
                            self.whatNeedCalculateWithOutputOptimization()
                            # 以下是计算后工作
                            wx.CallAfter(self.outPutToOutPut, f"\n\n本次计算+输出花费了{self.time_after_calculate - self.time_before_calculate:.6f}秒\n")  # 输出本次计算时间
                            wx.CallAfter(self.outPutToOutPut, "已启用输出优化")
                        else:
                            self.whatNeedCalculate()
                            # 以下是计算后工作
                            wx.CallAfter(self.outPutToOutPut,f"\n\n本次计算+输出花费了{self.time_after_calculate - self.time_before_calculate:.6f}秒\n")  # 输出本次计算时间
            except Exception as e:
                wx.CallAfter(self.clearOutPut)
                wx.CallAfter(self.setOutPut,str(e))
                wx.CallAfter(self.outPutToOutPut,"\n\n插件发生错误，请检查输入格式")

            self.is_thread_runing = False
        else:
            wx.CallAfter(self.outPutToOutPut,"\n运算程序正在进行中，请勿反复点击计算按钮！\n")  # 清空输出框

    def whatNeedCalculate(self):
        module_return = None  # 用来输出的，outputmode2和1的时候有用
        result_last = None  # 用来输出的，outputmode0的时候有用
        self.is_thread_runing = True
        if self.input_mode == 'string':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == 'num':
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == '1':
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        self.time_before_calculate = time.perf_counter()  # 储存开始时间

        if self.output_mode == '0':
            exec(f"result_last = self.{self.Selection}.main(self.input_box_s_input)")
            wx.CallAfter(self.setOutPut, str(result_last) + "\n")  # 结果为str，直接输出
        elif self.output_mode == '2': # 算一行输出一行，但是没有换行
            wx.CallAfter(self.clearOutPut)  # 清空输出框
            exec(f"module_return=self.{self.Selection}.main(self.input_box_s_input")
            for result_process in module_return:  # 计算
                wx.CallAfter(self.outPutToOutPut, str(result_process))  # 算一行输出一行
        elif self.output_mode == '1': # 算一行输出一行
            wx.CallAfter(self.clearOutPut)  # 清空输出框
            exec(f"module_return=self.{self.Selection}.main(self.input_box_s_input")
            for result_process in module_return:  # 计算 啊，定义就在上一行，hoyc你是看不到吗？
                wx.CallAfter(self.outPutToOutPut, str(result_process) + "\\n")  # 算一行输出一行
        elif self.output_mode == '4':
            wx.CallAfter(self.clearOutPut) # 清空输出框
            exec(f"self.{self.Selection}.main(self.input_box_s_input,self,'output')")
        else:
            wx.CallAfter(self.clearOutPut) # 清空输出框
            exec(f"self.{self.Selection}.main(self.input_box_s_input,self)")
        self.time_after_calculate = time.perf_counter()  # 储存结束时间

    def whatNeedCalculateWithSave(self):  # 选择检测+计算
        # self.name_text_file - 储存保存到哪个文件里
        # now - 保存datetime类型的当前时间
        module_return = None  # 用来输出的，outputmode2和1的时候有用
        result_last = None  # 用来输出的，outputmode0的时候有用
        self.is_thread_runing = True
        if self.input_mode == 'string':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == 'num':
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == '1':
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        now = datetime.datetime.now()  # 保存当前时间，用于文件名

        if self.save_mode == '1':
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') + '  ' + str(self.input_box_s_input).replace('.',
                                                                                                                 '_') + "的" + self.save_name
        else:
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') +'  '+ self.save_name + str(self.input_box_s_input) + self.quantifier

        save = open(os.path.join(os.path.abspath(self.save_location_input_box.GetValue()),self.name_text_file + ".txt"), "w", encoding="utf-8")

        self.time_before_calculate = time.perf_counter()  # 储存开始时间

        try:
            if self.output_mode == '0':  # 分布输出和一次输出
                exec(f"result_last = self.{self.Selection}.main(self.input_box_s_input)")
                save.write(str(result_last) + "\n")
            elif self.output_mode == '2':  # 算一行输出一行，但是没有换行
                exec(f"module_return=self.{self.Selection}.main(self.input_box_s_input")
                for result_process in module_return:  # 计算
                    save.write(str(result_process))
                    save.flush()  # 算出来就存进去
            elif self.output_mode == '1':  # 算一行输出一行，但是没有换行
                exec(f"module_return=self.{self.Selection}.main(self.input_box_s_input")
                for result_process in module_return:  # 计算
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
        if self.input_mode == 'string':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == 'num':
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == '1':
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        now = datetime.datetime.now()  # 保存当前时间，用于文件名

        if self.save_mode == '1':
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') + '  ' + str(self.input_box_s_input).replace('.',
                                                                                                                 '_') + "的" + self.save_name
        else:
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') + '  ' + self.save_name + str(
                self.input_box_s_input) + self.quantifier



        with tempfile.TemporaryFile('w+t', encoding='utf-8', errors='ignore') as save:
            self.time_before_calculate = time.perf_counter()  # 储存开始时间

            try:
                if self.output_mode == '0':  # 分布输出和一次输出
                    result_last = None  # 用来输出的，outputmode0的时候有用
                    exec(f"result_last = self.{self.Selection}.main(self.input_box_s_input)")
                    save.write(str(result_last) + "\n")
                elif self.output_mode == '2':  # 算一行输出一行，但是没有换行
                    module_return = None  # 用来输出的，outputmode2和1的时候有用
                    exec(f"module_return=self.{self.Selection}.main(self.input_box_s_input")
                    for result_process in module_return:  # 计算
                        save.write(str(result_process))
                        save.flush()  # 算出来就存进去
                elif self.output_mode == '1':  # 算一行输出一行，但是没有换行
                    module_return = None  # 用来输出的，outputmode2和1的时候有用
                    exec(f"module_return=self.{self.Selection}.main(self.input_box_s_input")
                    for result_process in module_return:  # 计算
                        save.write(str(result_process) + "\\n")
                        save.flush()  # 算出来就存进去
                elif self.output_mode == '4':
                    exec(f"self.{self.Selection}.main(self.input_box_s_input,save,'save')")
                else:
                    exec(f"self.{self.Selection}.main_save(self.input_box_s_input,save)")
            finally:
                wx.CallAfter(self.clearOutPut)  # 清空输出框
                save.seek(0)# 将文件指针移到开始处，准备读取文件
                if self.output_optimization_check.GetValue():
                    for times,line in enumerate(self.quickTraverseFile(save)):
                        wx.CallAfter(self.outPutToOutPut,line)
                        if times>=128:
                            wx.CallAfter(self.outPutToOutPut,"\n\n输出上限：检测到输出数据过大，请使用保存到文件防止卡死")
                            break
                else:
                    for line in self.quickTraverseFile(save):
                        wx.CallAfter(self.outPutToOutPut,line)

        self.time_after_calculate = time.perf_counter()  # 储存结束时间

    def quickTraverseFile(self,file,chunk_size=8192):
        for chunk in iter(partial(file.read,chunk_size), ''):#用readline的话，读到换行符就会直接停止读取，不会读取到8192B，会增加读取次数
            yield chunk

    def whatNeedCalculateWithTest(self):
        self.is_thread_runing = True
        if self.input_mode == 'string':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == 'num':
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        elif self.input_mode == '1':
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        try:
            if self.output_mode == '4':
                wx.CallAfter(self.clearOutPut) # 清空输出框

                self.time_before_calculate = time.perf_counter()  # 储存开始时间
                exec(f"self.{self.Selection}.main(self.input_box_s_input,self,'test')")
                self.time_after_calculate = time.perf_counter()  # 储存结束时间
                if self.output.GetValue() != "":
                    wx.CallAfter(self.clearOutPut) # 清空输出框
                    wx.CallAfter(self.setOutPut,"发生错误，请检查输入格式，以及插件是否有test模式")
            else:
                wx.CallAfter(self.clearOutPut) # 清空输出框

                self.time_before_calculate = time.perf_counter()  # 储存开始时间
                exec(f"self.{self.Selection}.main_test(self.input_box_s_input,self)")
                self.time_after_calculate = time.perf_counter()  # 储存结束时间
        except Exception:
            self.time_after_calculate = time.perf_counter()  # 储存结束时间
            wx.CallAfter(self.setOutPut,"发生错误，请检查输入格式，以及插件是否有test模式")

    def outPutToOutPut(self, msg:str):
        self.output.AppendText(msg)

    def clearOutPut(self):
        self.output.Clear()

    def setOutPut(self, msg:str):
        self.output.SetValue(msg)


    def chooseNumberEvent(self, event):  # 选择算法事件
        self.Selection = self.plugin_filename_option_name_map[
            self.list_box.GetString(self.list_box.GetSelection())]
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
        self.output.SetValue(self.output_start + "\n")
        self.output.AppendText(self.output_name + " " + self.version + "\n")
        self.output.AppendText("by " + self.author + "\n" + "\n")
        self.output.AppendText("使用提示：\n" + self.help + "\n")
        self.output.AppendText(self.output_end)

    def showAbout(self, event):  # 菜单栏 关于作者
        self.output.SetValue(Doc.START_SHOW)

    def showTODO(self, event):  # 菜单栏 更新展望
        self.output.SetValue(Doc.TODO)

    def showDONE(self, event):  # 菜单栏 更新日志
        self.output.SetValue(Doc.UPDATE_LOG)

    def saveCheckEvent(self, event):  # 保存选项（那个√）事件
        with shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True) as setting_file:  # 读取设置文件
            setting_file['save_check'] = self.save_check.GetValue()
        if self.test_check.GetValue():
            self.test_check.SetValue(False)
        else:
            pass

    def testCheckEvent(self,event):#test开就不报存
        with shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True) as setting_file:  # 读取设置文件
            if self.save_check.GetValue():
                self.save_check.SetValue(False)
                setting_file['save_check'] = False
            else:
                pass

    def outputOptimizationCheckEvent(self,event):
        with shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True) as setting_file:  # 读取设置文件
            if self.output_optimization_check.GetValue():
                pass
            else:
                self.output_lock_maximums_check.SetValue(False)
                setting_file['output_lock_maximums'] = False
            setting_file['output_optimization'] = self.output_optimization_check.GetValue()

    def outputLockMaximumsCheckEvent(self, event):#锁上限开，就要开优化
        with shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True) as setting_file:  # 读取设置文件
            if self.output_lock_maximums_check.GetValue():
                self.output_optimization_check.SetValue(True)
                setting_file['output_optimization'] = True
                setting_file['output_lock_maximums'] = self.output_lock_maximums_check.GetValue()#True
            else:
                setting_file['output_lock_maximums'] = self.output_lock_maximums_check.GetValue()#False

    def quit_event(self,event): #菜单栏退出事件
        self.Close(True)
        sys.exit(0)

    def stop_compute(self,event):
        self.Destroy()
        sys.exit(0)

    def cheak_update(self,event):
        webbrowser.open("https://github.com/HowieHz/hpyculator/releases")

    def reset_save_location(self,event):
        self.save_location_input_box.SetValue(os.path.abspath(".\\皓式程序输出\\"))
        with shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True) as setting_file:  # 读取设置文件
            setting_file['save_location'] = str(self.save_location_input_box.GetValue())

    def __del__(self):
        pass

    def search_text(self,event): # 搜索框按回车之后的事件
        self.search_keyword = event.GetString()
        print(self.can_choose_number)
        self.search.ShowCancelButton(True)


        try:#清空选择栏
            for i in range(len(self.can_choose_number)):
                self.list_box.Delete(0)
        except Exception:
            pass

        for i in self.can_choose_number:#选出符合要求的
            if i.find(self.search_keyword)==-1:#字符串方法，没找到指定子串就-1
                continue
            else:
                self.list_box.Append(i)

        return

    def search_cancel(self,event):#取消搜索结果，显示全部插件
        self.search.ShowCancelButton(False)

        try:
            for i in range(len(self.can_choose_number)):
                self.list_box.Delete(0)
        except Exception:
            pass
        self.list_box.Append(self.can_choose_number)
        return


"""
各种量的命名规范
hello_world 变量全部小写，使用下划线连接
helloWorld 函数(def)和方法使用小驼峰式命名法，首单词字母小写，后面单词字母大写
HelloWorld 类名(Class)、文件名(Xswl.txt)使用帕斯卡命名规则(大驼峰式命名法,每一个单词的首字母都采用大写字母)。
HELLO_WORLD 常量(NEVER_GIVE_UP)全部大写，使用下划线连接单词
numba vx jax感觉两个差不多
"""
if __name__ == '__main__':
    # app=wx.PySimpleApp()
    app = wx.App()
    # wx.App(False)
    mainWindow = Application()
    mainWindow.Show(True)
    app.MainLoop()  # 正常_必备_主事件循环
