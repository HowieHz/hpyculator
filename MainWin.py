# -*- coding: utf-8 -*-
import wx
import wx.xrc

M_VERSION = "V1.2.3"

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=-1, title="各类数组计算程序%s-Howie皓子制作" % M_VERSION, size=(1000, 750))
        # 主窗口(MainFrame)选项，编辑标题

        self.bkg = wx.Panel(self)  # bkg = background
        self.start_button = wx.Button(self.bkg, label="计算")  # 计算按钮

        self.save_check = wx.CheckBox(self.bkg, wx.ID_ANY, "保存为文件", wx.Point(250, 5), wx.DefaultSize, 0)  # 保存选项
        self.test_check = wx.CheckBox(self.bkg, wx.ID_ANY, "测试模块性能", wx.Point(250, 5), wx.DefaultSize, 0)  # 保存选项

        #self.can_choose_number=[]
        #self.choose_number = wx.Choice(self.bkg, wx.ID_ANY, choices=self.can_choose_number)  # 选择算法

        self.input_box = wx.TextCtrl(self.bkg, style=wx.TE_MULTILINE)  # 输入行数的文本框
        self.output = wx.TextCtrl(self.bkg, style=wx.TE_MULTILINE)  # 最大的文本框

        self.search = wx.SearchCtrl(self.bkg, wx.ID_ANY,style=wx.TE_PROCESS_ENTER)
        self.search.SetHint('输入后回车进行搜索')

        self.can_choose_number = []
        self.list_box = wx.ListBox(self.bkg,choices=self.can_choose_number,style=wx.LB_SINGLE)

        self.file_menu = wx.Menu()  # WxPython 中使用wx.Menu()类来表示一个菜单
        self.file_menu.Append(1002, '更新日志', '做完了做完了')
        self.file_menu.Append(1001, '更新展望', '在做了在做了')
        self.file_menu.Append(1000, '开屏介绍', '召唤作者的*话')
        self.file_menu.Append(1004, '检查更新', 'goto github')

        self.stop_menu = wx.Menu()  # WxPython 中使用wx.Menu()类来表示一个菜单
        self.stop_menu.Append(1010, '终止当前运算', '不准算！')
        self.quit = wx.MenuItem(self.stop_menu, 1011, '&退出程序\tCtrl+Q')
        self.stop_menu.Append(self.quit)


        """
        解读:此方法用于向菜单中添加一个选项
        参数(wx.ID_SAVE):这是wxWidgets提供的标准事件ID，我们实现的是保存功能，所以使用了ID_SAVE，如果你需要了解更多的标准ID，请访问 事件ID列表
        参数(保存):显示到选项上的文本
        最后一个参数:当鼠标选择此选项时显示到窗口状态栏中的文本（状态栏待会会讲到，很简单的一个东西）
        小提示:调用一次 Append() 添加一个菜单选项，调用多次可添加多个菜单选项
        """
        self.window_menu = wx.MenuBar()  # wxpython中使用wx.MenuBar()类来表示一个菜单栏（注意不是菜单哦）
        self.window_menu.Append(self.file_menu, '|----关于----|')
        self.window_menu.Append(self.stop_menu, '|----终止----|')
        """
        解读:此方法把菜单添加到菜单栏中
        参数(file_menu):使用wx.Menu()创建的菜单
        参数(文件):可以理解为菜单的名字，会显示到菜单栏中。
        小提示:调用一次 Append() 把一个菜单添加到菜单栏，调用多次可添加多个菜单
        """
        self.SetMenuBar(self.window_menu)
        """
        解读:把创建好的菜单栏添加到窗口上（如果你忘了这一步，你的菜单栏将不会显示到窗口，所以要此步骤要牢记）
        参数(window_menu):使用wx.MenuBar()创建的菜单栏
        """

        self.hbox1 = wx.BoxSizer()  # 尺寸器
        self.hbox1.Add(self.start_button, proportion=1, flag=wx.EXPAND)  # 计算按钮的尺寸器
        #self.hbox1.Add(self.choose_number, 0, wx.EXPAND | wx.LEFT, 5)  # 选择选项的尺寸器
        self.hbox1.Add(self.save_check, 0, wx.EXPAND | wx.LEFT, 5)  # 保存选项的尺寸器
        self.hbox1.Add(self.test_check, 0, wx.EXPAND | wx.LEFT, 5)  # 测试选项的尺寸器

        self.hbox2 = wx.BoxSizer()  # 尺寸器
        self.hbox2.Add(self.input_box, proportion=1, flag=wx.EXPAND)  # 输入行数的文本框的尺寸器

        self.hbox3 = wx.BoxSizer()  # 尺寸器
        self.hbox3.Add(self.output, proportion=1, flag=wx.EXPAND,
                      border=5)  # 最大的文本框的尺寸器

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.hbox1, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)  # 尺寸器的尺寸器
        self.vbox.Add(self.hbox2, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)  # 尺寸器的尺寸器
        self.vbox.Add(self.hbox3, proportion=3, flag=wx.EXPAND | wx.ALL, border=5)  # 尺寸器的尺寸器


        self.vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.vbox2.Add(self.search, proportion=1, flag=wx.EXPAND)
        self.vbox2.Add(self.list_box, proportion=5, flag=wx.EXPAND)

        self.hboxMain = wx.BoxSizer()  # 尺寸器
        self.hboxMain.Add(self.vbox2,proportion=1, flag=wx.EXPAND)
        self.hboxMain.Add(self.vbox,proportion=2, flag=wx.EXPAND)

        self.bkg.SetSizer(self.hboxMain)  # 布局显示_必备
        self.CreateStatusBar()  # 窗口状态栏显示_必备
        self.Center()
        # self.Show(True)#正常_必备_不要在此之后写任何窗口代码

        self.start_button.Bind(wx.EVT_BUTTON, self.startEvent)  # 计算按钮事件
        self.save_check.Bind(wx.EVT_CHECKBOX, self.saveCheckEvent)  # 保存选项事件
        self.test_check.Bind(wx.EVT_CHECKBOX, self.testCheckEvent)  #测试模式选项事件
        #self.choose_number.Bind(wx.EVT_CHOICE, self.chooseNumberEvent)  # 选择算法事件
        self.Bind(wx.EVT_MENU, self.showDONE, id=1002)
        self.Bind(wx.EVT_MENU, self.showTODO, id=1001)
        self.Bind(wx.EVT_MENU, self.showAbout, id=1000)
        self.Bind(wx.EVT_MENU, self.quit_event,id=1011)
        self.Bind(wx.EVT_MENU, self.stop_compute, id=1010)
        self.Bind(wx.EVT_MENU, self.cheak_update, id=1004)
        self.Bind(wx.EVT_LISTBOX,self.chooseNumberEvent,self.list_box)
        self.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN,self.search_text)#搜索框回车后执行的函数，self.search_text
        self.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.search_cancel)

    def __del__(self):
        pass

    def startEvent(self, event):
        event.Skip()

    def saveCheckEvent(self, event):
        event.Skip()

    def testCheckEvent(self,event):
        event.Skip()

    def chooseNumberEvent(self, event):
        event.Skip()

    def showDONE(self, event):
        event.Skip()

    def showTODO(self, event):
        event.Skip()

    def showAbout(self, event):
        event.Skip()

    def quit_event(self,event):
        event.Skip()

    def stop_compute(self,event):
        event.Skip()

    def cheak_update(self,event):
        event.Skip()


    def search_text(self,event):
        event.Skip()

    def search_cancel(self,event):
        event.Skip()