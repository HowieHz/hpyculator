import datetime
import os
import shelve
import time
import wx
import threading
import sys
import importlib
#import pprint

import MainWin

M_VERSION = "V1.1.0"

TODO = """更新展望(咕咕咕):
1.背景图
2.可自定义文件保存的文件名格式
3.可选文件的保存位置
7.检查更新按钮
8.可以分享脚本的平台（qq群也不错
9.用pyqt重构
10.上线网页版
11.更精确的模块计算时间
"""

UPDATE_LOG = """更新日志:
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

各种量的命名更加规范
hello_world 变量全部小写，使用下划线连接
helloWorld 函数(def)和方法使用小驼峰式命名法，首单词字母小写，后面单词字母大写
HelloWorld 类名(Class)、文件名(Xswl.txt)使用帕斯卡命名规则(大驼峰式命名法,每一个单词的首字母都采用大写字母)。
HELLO_WORLD 常量(NEVER_GIVE_UP)全部大写，使用下划线连接单词




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
然后按下输入框右边按钮

必读:

！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
0.建议保存到文件，这样不会内屏输出导致卡死!!--------重点！！！
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

1.“保存”会将结果保存到程序所在目录下的
“年_月_日 时_分_秒 (计算种类)计算结果(输入数据).txt”
2.设置行(项)数较大请选择保存到文件，算的不久，但是导出很久，可以看看任务管理器，不同插件性能（读写速度和）不同，要看插件作者的水平
2.(2)内置模块说明:(n系列占用内存最小，读写速度最慢),
                (one系列占用内存最大（算太多内存占用会起飞，出问题概不负责）),
                (fix系列在n系列和one系列中找了一个平衡点，推荐使用),
3.在输入框输入 stop 或者 停止 可以强制停止当前计算线程


交流群694413711 - 此群安静的像一滩死水 -=作者中考完了，消息一般都会会
仅供学习，请勿进行商业用途
(好像这也没法用于进行商业用途的说2333)

悄悄说:在输入栏输入update_log之后点击运算就可以看更新日志了""" % M_VERSION)


class Application(MainWin.MainWindow):  # 主类

    def __init__(self):
        # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
        # self.setting - 配置文件ShelfFile(\皓式程序设置\hpyculator_setting)
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
        self.plugin_filename_option_name_map = {}
        self.readPlugin(r'.\Plugin')
        #pprint.pprint("读取到Plugin文件夹下文件:")
        #pprint.pprint(self.plugin_files_name)#读取到Plugin下面的文件
        #pprint.pprint("读取到的文件夹插件:")
        #pprint.pprint(self.plugin_files_name_folder)
        try:
            for list in self.plugin_files_name:#从所有读取的文件中挑选出.py为后缀的文件
                if (list[0].split("."))[-1] == "py":
                    self.plugin_files_name_py = list
        except:
            pass

        #pprint.pprint("读取到的.py文件:")
        #pprint.pprint(self.plugin_files_name_py)

        self.init_plugin_singerfile()#导入单文件插件
        self.init_plugin_folder()#导入文件插件

        super().__init__()

        #print("\n\n选项和文件名（ID）映射表:")
        #pprint.pprint(self.plugin_filename_option_name_map)

        # self.events=Events()#实例化Events
        # self.mainWindow()  # 初始化窗口
        self.is_thread_runing = False



        # 关于gui显示内容的初始化
        self.output.SetValue(START_SHOW)  # 开启的展示

        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)#读取设置文件
        try:
            self.save_check.SetValue(self.setting['save_check'])  # 根据数据设置选项状态
        except:
            self.setting['save_check'] = self.save_check.GetValue()
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
            except:
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
            except:
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

        if str(self.input_box.GetValue()) == "update_log":  # update_log检测
            self.output.SetValue(UPDATE_LOG)
            return
        #if str(self.input_box.GetValue()) == "停止":  # u停止检测
            #self.output.SetValue("当前计算线程已停止")
            #self.is_thread_runing = False
            #return
        #if str(self.input_box.GetValue()) == "stop":  # stop检测
            #self.output.SetValue("当前计算线程已停止")
            #self.is_thread_runing = False
            #return
        if self.choose_number.GetString(self.choose_number.GetSelection()) == "":  # 是否选择检测
            self.output.SetValue("\n\n" + "不选要算什么我咋知道要算啥子嘞" + "\n")
            return
        if str(self.input_box.GetValue()) == "":  # 是否输入检测
            self.output.SetValue("\n\n" + "不输要算什么我咋知道要算啥子嘞" + "\n")
            return

        self.result_last = []  # 返回一次就输出、保存专用

        #以上是计算前工作
        calculate_thread=threading.Thread(target=self.startCalculate)
        calculate_thread.start()



    def startCalculate(self):
        if self.is_thread_runing == False:
            try:
                self.output.SetValue("")  # 清空输出框
                self.output.AppendText("计算程序正在运行中，所需时间较长，请耐心等待")
                if self.save_check.GetValue() == True:  # 检测保存按钮的状态判断是否保存
                    self.whatNeedCalculateWithSave()
                    # 以下是计算后工作
                    self.output.Clear() # 清空输出框
                    self.output.AppendText(
                        "\n本次计算+保存花费了%.5f秒\n" % (self.time_after_calculate - self.time_before_calculate))  # 输出本次计算时间
                    self.output.AppendText("\n计算结果已保存在" + os.path.abspath(".\\皓式程序输出\\") + self.name_text_file + ".txt")
                    self.output.AppendText("\n")
                else:  # 选择不保存才输出结果
                    self.whatNeedCalculate()
                    # 以下是计算后工作
                    self.output.AppendText(
                        "\n\n本次计算+输出花费了%.5f秒\n" % (self.time_after_calculate - self.time_before_calculate))  # 输出本次计算时间
            except:
                self.output.SetValue("插件发生错误，请检查输入格式")
                self.is_thread_runing = False
        else:
            self.output.AppendText("\n运算程序正在进行中，请勿反复点击计算按钮！\n")  # 清空输出框


    def whatNeedCalculate(self):
        self.is_thread_runing = True
        if self.input_mode == '0':
            self.input_box_s_input = str(self.input_box.GetValue())  # 取得输入框的数字
        else:
            self.input_box_s_input = int(self.input_box.GetValue())  # 取得输入框的数字

        self.time_before_calculate = time.time()  # 储存开始时间

        if self.output_mode == '0':
            exec("self.result_last = self." + self.Selection + ".main(self.input_box_s_input)")
            self.output.SetValue(str(self.result_last) + "\n")  # 结果为str，直接输出
        elif self.output_mode == '2': # 算一行输出一行，但是没有换行
            self.output.Clear()  # 清空输出框
            exec("for self.result_process in self." + self.Selection + """.main(self.input_box_s_input):  # 计算
        self.output.AppendText(str(self.result_process))""")  # 算一行输出一行
        elif self.output_mode == '1': # 算一行输出一行
            self.output.Clear()  # 清空输出框
            exec("for self.result_process in self." + self.Selection + """.main(self.input_box_s_input):  # 计算
    self.output.AppendText(str(self.result_process)+"\\n")""")  # 算一行输出一行
        elif self.output_mode == '4':
            self.output.Clear()  # 清空输出框
            exec("self." + self.Selection + ".main(self.input_box_s_input,self,'output')")
        else:
            self.output.Clear()  # 清空输出框
            exec("self." + self.Selection + ".main(self.input_box_s_input,self)")
        self.time_after_calculate = time.time()  # 储存结束时间
        self.is_thread_runing = False

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

        save = open(os.path.abspath('.\\皓式程序输出\\' + self.name_text_file + ".txt"), "w", encoding="utf-8")

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
            self.is_thread_runing = False

        self.time_after_calculate = time.time()  # 储存结束时间

    def chooseNumberEvent(self, event):  # 选择算法事件
        self.Selection = self.plugin_filename_option_name_map[
            self.choose_number.GetString(self.choose_number.GetSelection())]
        self.required_parameters = ['input_mode','output_mode','save_name','output_name','save_mode','version']
        self.optional_parameters = ['output_start', 'quantifier', 'author', 'help', 'output_end', 'fullwidth_symbol','input_mode','output_mode','save_name','output_name','save_mode','version']
        self.required_parameters.extend(self.optional_parameters)
        for i in self.required_parameters:
            try:
                exec("self."+i+"=str(self." + self.Selection + ".PLUGIN_METADATA['"+i+"'])")
            except:
                exec("self." + i + "=''")
        if self.fullwidth_symbol == '1':
            self.help = self.help.replace(",","，").replace(".","。").replace("'","‘").replace('"','”').replace('(','（').replace(')','）')
        self.output.SetValue(self.output_start+"\n")
        self.output.AppendText(self.output_name+" "+self.version+"\n")
        self.output.AppendText("by "+self.author+"\n"+"\n")
        self.output.AppendText("使用提示：\n"+self.help + "\n")
        self.output.AppendText(self.output_end)

    def showAbout(self, event):  # 关于作者
        self.output.SetValue(START_SHOW)

    def showTODO(self, event):  # 更新展望
        self.output.SetValue(TODO)

    def showDONE(self, event):  # 更新日志
        self.output.SetValue(UPDATE_LOG)

    def saveCheckEvent(self, event):  # 保存选项事件
        self.setting = shelve.open(os.path.abspath(r'.\皓式程序设置\hpyculator_setting'), writeback=True)
        self.setting['save_check'] = self.save_check.GetValue()
        self.setting.close()
        return

if __name__ == '__main__':
    # app=wx.PySimpleApp()
    app = wx.App()
    # wx.App(False)
    mainWindow = Application()
    mainWindow.Show(True)
    app.MainLoop()  # 正常_必备_主事件循环
