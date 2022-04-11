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
#import jpype
#import pprint

import MainWin

M_VERSION = "V1.2.5"

TODO = """更新展望(咕咕咕):
1.背景图
2.可自定义文件保存的文件名格式
8.可以分享脚本的平台（qq群也不错
#9.用pyqt重构
10.上线网页版
11.可以读取文件作为输入
"""

UPDATE_LOG = """更新日志:
20220409
V1.2.5
修复了遗留问题
完善了输出优化模式

20220408
V1.2.4
hpyculator模块上传了！现可通过pip下载
重写了内置插件
修改了gui,可自选保存位置

20220408
V1.2.3
修复了多线程的问题
修改了菜单栏

20220407
V1.2.2
修复了内置插件无法正常工作的问题
添加了更新检查按钮(打开浏览器跳转到https://github.com/HowieHz/hpyculator/releases)

20220407
V1.2.1
修复了无插件打不开的bug
修复了退出后还残留后台程序的bug

20220407
V1.2.0
修改gui
增加了搜索框
添加了测试选项，勾选之后程序就会使用test模式

20220405
V1.1.0
增加了对文件插件的支持
增加了很多提示，防止插件卡死程序

V1.0.0
改名为
皓式可编程计算器hpyculator
2022年1月19日添加了规范文档
2022年1月18-19日，重构了程序（从流水线+函数群变成了面向对象的编程）
2022年3月29再次捡起项目，
2022年3月31写完，实现了规范文档，但是掉进了打包的坑，还好第二天爬出来了
2022年4月1日第一个内测版
2022年4月1日添加了多线程支持，添加了更多用户友好类提示，修复了若干个bug，添加了一种输出模式
2022年4月2日修改了内置插件的性能，添加了新的输出模式，并提供了4个函数便于插件作者创作

趣闻:
2022年1月16日时想用PyQt（5/6）代替wxpython（哈哈wxpython不支持python3.10，其他版本又删掉了，被迫的）
由于PyQt（5/6）-tool用pip不能正确安装和考虑到学习成本，所以干脆卸载py310，改回py39（白配置一遍^_^）



来自 各类数组计算程序
2021年6月27日
V1.2
选择保存文件时不再输出
平均数，众数，中位数，方差，标准差的计算可以输入负数和小数了
为了节省体积，换了个图标

V1.1
添加了平均数，众数，中位数，方差，标准差的计算

2020年11月14日
V1.0
多了一个可以切换计算核心的选项
更加模块化，内置模块有杨辉三角计算和斐波那契数列计算
(作者电脑i5-5代低压u，4g内存。无聊算114514行，算了半小时，原本要关了，看任务管理器还在运行，就去睡了一会，起来看到一个1338412kb的文件（约1.28G），哈哈哈，请勿模仿（除非很闲）)



来自杨辉三角计算程序v3.4.2
a3.4.2 修复不能读取配置的问题，优化代码体积
2020年11月8日a3.4.1 创建了两个文件夹专门用来储存设置和输出,扩大1.5倍了默认生成的窗口
2020年11月8日a3.4.0 在输入栏输入update_log点击运算就可以看更新日志了!菜单栏它来了
2020年11月7日a3.3.4 修改保存名的时间
a3.3.3b 走向规范化
2020年11月7日a3.3.3a 遗弃的分支，消除了保存时间
2020年10月17日a3.3.2 删除多余代码优化体积
2020年10月17日a3.3.1 生成在gui里的不再是一行了,砍掉了可以修改算法的选项,删除多余代码优化体积
a3.3.0 被遗忘的版本号
a3.2 改进了算法，增快了运行速度,增加了可以修改算法的选项
2020年10月10日a3.1 将原来的运行并保存按钮修改为是否保存的选项
a3.0 有GUI了!生成的文件不再是一行了

a2.0 添加了保存文件到本目录，添加了计算计时器,防止因为错误信息造成的闪退,节省打包体积

a1.0 最初的经典"""

"""
版本号更新约定（x为更新的版本号）:

大改动，重写(api可能需要更新):                V x.*.*
改进，完成TODO(api可能需要更新):              V *.x.*
修bug，小问题:                              V *.*.x
分支（以及内测版，预览版。此处x为小写字母）:      V *.*.*-x
"""

START_SHOW = ("""皓式可编程计算器hpyculator%s
Howie皓子制作

首先选择你要计算的东西
然后在上方输入框输入你要计算的项数（行数）
之后在左侧选择计算核心

必读:


！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
0.建议保存到文件，这样不会内屏输出导致卡死!!--------重点！！！
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

1.“保存”会将结果保存到程序所在目录下 "\皓式程序输出"
2.设置行(项)数较大请选择保存到文件，算的不久，但是导出很久，可以看看任务管理器，不同插件性能（读写速度和）不同，要看插件作者的水平

交流群694413711 - 此群安静的像一滩死水 -=作者中考完了，消息一般都会会

已在github开源 禁止商用






悄悄说:在输入栏输入update_log之后点击运算就可以看更新日志了""" % M_VERSION)


class Application(MainWin.MainWindow):  # 主类

    def __init__(self):
        # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
        # self.setting - 配置文件ShelfFile(\皓式程序设置\hpyculator_setting)

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
        #self.plugin_files_path=[]
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
            for list in self.plugin_files_name:#从所有读取的文件中挑选出.py为后缀的文件
                if (list[0].split("."))[-1] == "py":
                    if  self.plugin_files_name_py==[]:
                        self.plugin_files_name_py = list
        #这行bug很多，小心
        except Exception:
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
        self.output.SetValue(START_SHOW)  # 开启的展示

        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)#读取设置文件
        try:
            self.save_check.SetValue(self.setting['save_check'])  # 根据数据设置选项状态
        except Exception:
            self.setting['save_check'] = self.save_check.GetValue()

        try:
            self.save_location_input_box.SetValue(self.setting['save_location'])  # 根据数据设置选项状态
        except Exception:
            self.setting['save_location'] = self.save_location_input_box.GetValue()

        try:
            self.output_optimization_check.SetValue(self.setting['output_optimization'])  # 根据数据设置选项状态
        except Exception:
            self.setting['output_optimization'] = True
            self.output_optimization_check.SetValue(self.setting['output_optimization'])
        try:
            self.output_optimization_check.SetValue(self.setting['output_lock_maximums'])  # 根据数据设置选项状态
        except Exception:
            self.setting['output_lock_maximums'] = True
            self.output_optimization_check.SetValue(self.setting['output_optimization'])
        self.setting.close()

    def init_plugin_singerfile(self):
        self.plugin_files_name_py_nopy = self.plugin_files_name_py[:]
        for i in range(0, len(self.plugin_files_name_py_nopy)):  # 去掉.py后缀
            self.plugin_files_name_py_nopy[i] = self.plugin_files_name_py_nopy[i][:-3]
        #pprint.pprint("去掉.py后缀的文件名")
        #pprint.pprint(self.plugin_files_name_py_nopy)
        for name in self.plugin_files_name_py_nopy:
            exec("self." + name + "=importlib.import_module('" + ".{}'".format(name) + ", package='Plugin')")
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            try:
                exec(
                    "self.can_choose_number.append(self." + name + ".PLUGIN_METADATA['option_name'])")  # 读取模块元数据，添加gui选项
                exec(
                    "self.plugin_filename_option_name_map[self." + name + ".PLUGIN_METADATA['option_name']]=self." + name + ".PLUGIN_METADATA['id']")
            except Exception:
                pass

    def init_plugin_folder(self):
        for name in self.plugin_files_name_folder:
            exec("self." + name + "=importlib.import_module('" + ".{}.__init__'".format(name) + ", package='Plugin')")
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            try:
                exec(
                    "self.can_choose_number.append(self." + name + ".PLUGIN_METADATA['option_name'])")  # 读取模块元数据，添加gui选项
                exec(
                    "self.plugin_filename_option_name_map[self." + name + ".PLUGIN_METADATA['option_name']]=self." + name + ".PLUGIN_METADATA['id']")
            except Exception:
                pass

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
        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)
        self.setting['save_location'] = str(self.save_location_input_box.GetValue())
        self.setting.close()

        if str(self.input_box.GetValue()) == "update_log":  # update_log检测
            wx.CallAfter(self.setOutPut,UPDATE_LOG)
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

        self.result_last = []  # 返回一次就输出、保存专用

        #以上是计算前工作
        calculate_thread=threading.Thread(target=self.startCalculate)
        calculate_thread.start()



    def startCalculate(self):
        if self.is_thread_runing == False:
            try:
                wx.CallAfter(self.clearOutPut) # 清空输出框
                wx.CallAfter(self.outPutToOutPut,"计算程序正在运行中，所需时间较长，请耐心等待")
                if self.test_check.GetValue() == True:
                    self.whatNeedCalculateWithTest()
                    # 以下是计算后工作
                    wx.CallAfter(self.outPutToOutPut,
                        "\n\n本次测试花费了%.7f秒\n" % (self.time_after_calculate - self.time_before_calculate))  # 输出本次计算时间
                else:
                    if self.save_check.GetValue() == True:  # 检测保存按钮的状态判断是否保存
                        self.whatNeedCalculateWithSave()
                        # 以下是计算后工作
                        wx.CallAfter(self.clearOutPut) # 清空输出框
                        wx.CallAfter(self.outPutToOutPut,
                            "\n本次计算+保存花费了%.7f秒\n" % (self.time_after_calculate - self.time_before_calculate))  # 输出本次计算时间
                        wx.CallAfter(self.outPutToOutPut,"\n计算结果已保存在" + os.path.abspath(".\\皓式程序输出\\") + self.name_text_file + ".txt")
                        wx.CallAfter(self.outPutToOutPut,"\n")
                    else:  # 选择不保存才输出结果
                        if self.output_optimization_check.GetValue() == True:
                            self.whatNeedCalculateWithOutputOptimization()
                            # 以下是计算后工作
                            wx.CallAfter(self.outPutToOutPut,
                                         "\n\n本次计算+输出花费了%.7f秒\n" % (
                                                     self.time_after_calculate - self.time_before_calculate))  # 输出本次计算时间
                            wx.CallAfter(self.outPutToOutPut,"已启用输出优化")
                        else:
                            self.whatNeedCalculate()
                            # 以下是计算后工作
                            wx.CallAfter(self.outPutToOutPut,
                                "\n\n本次计算+输出花费了%.7f秒\n" % (self.time_after_calculate - self.time_before_calculate))  # 输出本次计算时间
            except Exception as e:
                wx.CallAfter(self.clearOutPut)
                wx.CallAfter(self.setOutPut,str(e))
                wx.CallAfter(self.outPutToOutPut,"\n\n插件发生错误，请检查输入格式")

            self.is_thread_runing = False
        else:
            wx.CallAfter(self.outPutToOutPut,"\n运算程序正在进行中，请勿反复点击计算按钮！\n")  # 清空输出框

    def outPutToOutPut(self, msg:str):
        self.output.AppendText(msg)

    def clearOutPut(self):
        self.output.Clear()

    def setOutPut(self, msg:str):
        self.output.SetValue(msg)

    def whatNeedCalculate(self):
        self.is_thread_runing = True
        if self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        else:
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        self.time_before_calculate = time.time()  # 储存开始时间

        if self.output_mode == '0':
            exec("self.result_last = self." + self.Selection + ".main(self.input_box_s_input)")
            wx.CallAfter(self.setOutPut,str(self.result_last) + "\n")  # 结果为str，直接输出
        elif self.output_mode == '2': # 算一行输出一行，但是没有换行
            wx.CallAfter(self.clearOutPut) # 清空输出框
            exec("for self.result_process in self." + self.Selection + """.main(self.input_box_s_input):  # 计算
        wx.CallAfter(self.outPutToOutPut,str(self.result_process))""")  # 算一行输出一行
        elif self.output_mode == '1': # 算一行输出一行
            wx.CallAfter(self.clearOutPut) # 清空输出框
            exec("for self.result_process in self." + self.Selection + """.main(self.input_box_s_input):  # 计算
    wx.CallAfter(self.outPutToOutPut,str(self.result_process)+"\\n")""")  # 算一行输出一行
        elif self.output_mode == '4':
            wx.CallAfter(self.clearOutPut) # 清空输出框
            exec("self." + self.Selection + ".main(self.input_box_s_input,self,'output')")
        else:
            wx.CallAfter(self.clearOutPut) # 清空输出框
            exec("self." + self.Selection + ".main(self.input_box_s_input,self)")
        self.time_after_calculate = time.time()  # 储存结束时间

    def whatNeedCalculateWithSave(self):  # 选择检测+计算
        # self.name_text_file - 储存保存到哪个文件里
        # now - 保存datetime类型的当前时间
        self.is_thread_runing = True
        if self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        else:
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        now = datetime.datetime.now()  # 保存当前时间，用于文件名

        if self.save_mode == '1':
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') +'  '+ str(self.input_box_s_input).replace('.','_')+"的"+self.save_name
        else:
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') +'  '+ self.save_name + str(self.input_box_s_input) + self.quantifier

        save = open(os.path.join(os.path.abspath(self.save_location_input_box.GetValue()),self.name_text_file + ".txt"), "w", encoding="utf-8")

        self.time_before_calculate = time.time()  # 储存开始时间

        try:
            if self.output_mode == '0':  # 分布输出和一次输出
                exec("self.result_last = self." + self.Selection + ".main(self.input_box_s_input)")
                save.write(str(self.result_last) + "\n")
            elif self.output_mode == '2':  # 算一行输出一行，但是没有换行
                exec("for self.result_process in self." + self.Selection + """.main(self.input_box_s_input):  # 计算
    save.write(str(self.result_process))
    save.flush()
                    """)  # 算出来就存进去
            elif self.output_mode == '1': # 算一行输出一行，但是没有换行
                exec("for self.result_process in self." + self.Selection + """.main(self.input_box_s_input):  # 计算
    save.write(str(self.result_process)+"\\n")
    save.flush()
            """)  # 算出来就存进去
            elif self.output_mode == '4':
                exec("self." + self.Selection + ".main(self.input_box_s_input,save,'save')")
            else:
                exec("self." + self.Selection + ".main_save(self.input_box_s_input,save)")
        finally:
            save.close()

        self.time_after_calculate = time.time()  # 储存结束时间

    def whatNeedCalculateWithOutputOptimization(self):
        # self.name_text_file - 储存保存到哪个文件里
        # now - 保存datetime类型的当前时间
        self.is_thread_runing = True
        if self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        else:
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        now = datetime.datetime.now()  # 保存当前时间，用于文件名

        if self.save_mode == '1':
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') + '  ' + str(self.input_box_s_input).replace('.',
                                                                                                                 '_') + "的" + self.save_name
        else:
            self.name_text_file = now.strftime('%Y_%m_%d %H_%M_%S') + '  ' + self.save_name + str(
                self.input_box_s_input) + self.quantifier



        with tempfile.TemporaryFile('w+t', encoding='utf-8', errors='ignore') as save:
            self.time_before_calculate = time.time()  # 储存开始时间

            try:
                if self.output_mode == '0':  # 分布输出和一次输出
                    exec("self.result_last = self." + self.Selection + ".main(self.input_box_s_input)")
                    save.write(str(self.result_last) + "\n")
                elif self.output_mode == '2':  # 算一行输出一行，但是没有换行
                    exec("for self.result_process in self." + self.Selection + """.main(self.input_box_s_input):  # 计算
                save.write(str(self.result_process))
                save.flush()
                                """)  # 算出来就存进去
                elif self.output_mode == '1':  # 算一行输出一行，但是没有换行
                    exec("for self.result_process in self." + self.Selection + """.main(self.input_box_s_input):  # 计算
                save.write(str(self.result_process)+"\\n")
                save.flush()
                        """)  # 算出来就存进去
                elif self.output_mode == '4':
                    exec("self." + self.Selection + ".main(self.input_box_s_input,save,'save')")
                else:
                    exec("self." + self.Selection + ".main_save(self.input_box_s_input,save)")
            finally:
                wx.CallAfter(self.clearOutPut)  # 清空输出框
                times=0
                save.seek(0)# 将文件指针移到开始处，准备读取文件
                if self.output_optimization_check.GetValue():
                    while True:
                        line = save.readline(2048)
                        times+=1
                        wx.CallAfter(self.outPutToOutPut,line)
                        if line == "":
                            break
                        if times>=256:
                            wx.CallAfter(self.outPutToOutPut,"\n\n输出上限：检测到输出数据过大，请使用保存到文件防止卡死")
                            break
                else:
                    while True:
                        line = save.readline(2048)
                        times+=1
                        wx.CallAfter(self.outPutToOutPut,line)
                        if line == "":
                            break


        self.time_after_calculate = time.time()  # 储存结束时间


    def whatNeedCalculateWithTest(self):
        self.is_thread_runing = True
        if self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        else:
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        try:
            if self.output_mode == '4':
                wx.CallAfter(self.clearOutPut) # 清空输出框

                self.time_before_calculate = time.time()  # 储存开始时间
                exec("self." + self.Selection + ".main(self.input_box_s_input,self,'test')")
                self.time_after_calculate = time.time()  # 储存结束时间
                if self.output.GetValue() != "":
                    wx.CallAfter(self.clearOutPut) # 清空输出框
                    wx.CallAfter(self.setOutPut,"发生错误，请检查输入格式，以及插件是否有test模式")
            else:
                wx.CallAfter(self.clearOutPut) # 清空输出框

                self.time_before_calculate = time.time()  # 储存开始时间
                exec("self." + self.Selection + ".main_test(self.input_box_s_input,self)")
                self.time_after_calculate = time.time()  # 储存结束时间
        except Exception:
            self.time_after_calculate = time.time()  # 储存结束时间
            wx.CallAfter(self.setOutPut,"发生错误，请检查输入格式，以及插件是否有test模式")




    def chooseNumberEvent(self, event):  # 选择算法事件
        self.Selection = self.plugin_filename_option_name_map[
            self.list_box.GetString(self.list_box.GetSelection())]
        self.required_parameters = ['input_mode','output_mode','save_name','output_name','save_mode','version']
        self.optional_parameters = ['output_start', 'quantifier', 'author', 'help', 'output_end', 'fullwidth_symbol','input_mode','output_mode','save_name','output_name','save_mode','version']
        self.required_parameters.extend(self.optional_parameters)
        for i in self.required_parameters:
            try:
                exec("self."+i+"=str(self." + self.Selection + ".PLUGIN_METADATA['"+i+"'])")
            except Exception:
                exec("self." + i + "=''")
        if self.fullwidth_symbol == '1':
            self.help = self.help.replace(",","，").replace(".","。").replace("'","‘").replace('"','”').replace('(','（').replace(')','）')
        self.output.SetValue(self.output_start+"\n")
        self.output.AppendText(self.output_name+" "+self.version+"\n")
        self.output.AppendText("by "+self.author+"\n"+"\n")
        self.output.AppendText("使用提示：\n"+self.help + "\n")
        self.output.AppendText(self.output_end)

    def showAbout(self, event):  # 菜单栏 关于作者
        self.output.SetValue(START_SHOW)

    def showTODO(self, event):  # 菜单栏 更新展望
        self.output.SetValue(TODO)

    def showDONE(self, event):  # 菜单栏 更新日志
        self.output.SetValue(UPDATE_LOG)

    def saveCheckEvent(self, event):  # 保存选项（那个√）事件
        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)
        self.setting['save_check'] = self.save_check.GetValue()
        if self.test_check.GetValue():
            self.test_check.SetValue(False)
        else:
            pass
        self.setting.close()

    def testCheckEvent(self,event):#test开就不报存
        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)
        if self.save_check.GetValue():
            self.save_check.SetValue(False)
            self.setting['save_location'] = False
        else:
            pass
        self.setting.close()

    def outputOptimizationCheckEvent(self,event):
        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)
        if self.output_optimization_check.GetValue():
            pass
        else:
            self.output_lock_maximums_check.SetValue(False)
            self.setting['output_lock_maximums'] = False
        self.setting['output_optimization'] = self.output_optimization_check.GetValue()
        self.setting.close()

    def outputLockMaximumsCheckEvent(self, event):#锁上限开，就要开优化
        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)
        if self.output_lock_maximums_check.GetValue():
            if self.output_optimization_check.GetValue():
                pass
            else:
                self.output_optimization_check.SetValue(True)
                self.setting['output_optimization'] = True
            self.setting['output_lock_maximums'] = True
        else:
            self.setting['output_lock_maximums'] = False
        self.setting.close()

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
        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)  # 读取设置文件
        self.setting['save_location'] = str(self.save_location_input_box.GetValue())
        self.setting.close()

    def __del__(self):
        pass

    def search_text(self,event): # 搜索框按回车之后的事件
        self.search_keyword = event.GetString()
        print(self.can_choose_number)
        self.search.ShowCancelButton(True)


        try:#清空选择栏
            for i in range(0,len(self.can_choose_number)):
                self.list_box.Delete(0)
        except Exception:
            pass

        for i in self.can_choose_number:#选出符合要求的
            if i.find(self.search_keyword)==-1:
                continue
            else:
                self.list_box.Append(i)

        return

    def search_cancel(self,event):#取消搜索结果，显示全部插件
        self.search.ShowCancelButton(False)

        try:
            for i in range(0, len(self.can_choose_number)):
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
