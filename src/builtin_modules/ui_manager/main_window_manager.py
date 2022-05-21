import shelve
import sys
import os
import hpyculator as hpyc
import logging  # 日志导入
from .. import document as doc
from ..plugin import instance_plugin_manager  # 插件管理
from ..calculate import CalculationManager  # 计算管理

# pyside6 ui signal导入
from PySide6.QtGui import QTextCursor, QGuiApplication, QBrush, QPalette, QPixmap
from PySide6.QtCore import Qt
from ..ui import Ui_MainWin
from hpyculator.hpysignal import main_win_signal

# 窗口管理类（用于管理设置的窗口）
from .setting_window_manager import SettingWinApp
from .about_win_manager import AboutWinApp

# refer to https://github.com/zhiyiYo/PyQt-Frameless-Window
from ..pyside_frameless_win.framelesswindow import FramelessWindow


class MainWinApp(FramelessWindow):
    def __init__(self,
                 setting_file_path,
                 output_dir_path,
                 plugin_dir_path,
                 background_dir_path):
        """
        主窗口程序类

        :param setting_file_path: 用于修改设置 设置文件路径
        :param output_dir_path:  用于输出结果 输出路径
        :param plugin_dir_path:  用于存放插件 插件文件夹路径
        :param background_dir_path:  用于存放背景图片的路径
        """
        # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
        self.SETTING_FILE_PATH = setting_file_path
        self.OUTPUT_DIR_PATH = output_dir_path
        self.PLUGIN_DIR_PATH = plugin_dir_path
        self.user_selection_id: str = ""  # 用户选择的插件的文件名（id)

        super().__init__()
        self.ui = Ui_MainWin()  # UI类的实例化()
        self.ui.setupUi(self)  # ui初始化
        self.bindSignalWithSlots()  # 信号和槽的绑定
        # self.main_win_signal = main_win_signal  # 更方便地使用自定义事件
        self.setWindowTitle("hpyculator %s" % doc.VERSION)  # 设置标题

        self.move_fix = False  # 一个窗口全屏之后，拖动，窗口会回到正常大小，且指针和在窗口长度和比值和原来一致,True的话就进行校正
        # self.bg_img = None  # 储存图片
        self.bg_img = QPixmap(os.path.join(os.getcwd(), "background_img", "background1.png"))

        # 读取设置文件-按钮状态和输出目录  check控件初始化
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:
            if "is_save_settings" in setting_file:
                self.is_save_settings = setting_file["is_save_settings"]  # 是否保存设置
                if self.is_save_settings:  # 当保存check状态
                    for sequence in [
                        ("is_save", False, self.ui.check_save),  # 键名 初始化状态 对应check控件
                        (
                                "output_optimization",
                                True,
                                self.ui.check_output_optimization,
                        ),
                        (
                                "output_lock_maximums",
                                True,
                                self.ui.check_output_lock_maximums,
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
                        ("is_save", False, self.ui.check_save),  # 键名 初始化状态 对应check控件
                        (
                                "output_optimization",
                                True,
                                self.ui.check_output_optimization,
                        ),
                        (
                                "output_lock_maximums",
                                True,
                                self.ui.check_output_lock_maximums,
                        ),
                    ]:
                        sequence[2].setChecked(sequence[1])  # 初始化控件
            else:
                setting_file["is_save_settings"] = False  # 默认不保存按键状态
                self.is_save_settings = False  # 默认不保存按键状态

        self.is_thread_running = [False]  # 防止反复启动计算线程

        # 关于gui显示内容的初始化
        self.flushListChoicesPlugin()
        self.ui.output_box.setPlainText(doc.START_SHOW)  # 开启的展示
        self.ui.search_plugin.setPlaceholderText("输入字符自动进行搜索\n清空搜索框显示全部插件")  # 灰色背景提示字符
        self.ui.search_plugin.clear()  # 不清空不显示灰色背景
        self.ui.input_box.setFocus()  # 设置焦点

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
            self.ui.button_start.setText(msg)

        def setStartButtonState(state: bool):
            self.ui.button_start.setEnabled(state)

        def setOutPutBoxCursor(where: str):  # 目前只有end
            cursor = self.ui.output_box.textCursor()
            cursor_state_map = {"end": QTextCursor.End}
            cursor.movePosition(cursor_state_map[where])
            # https://doc.qt.io/qtforpython-5/PySide2/QtGui/QTextCursor.html#PySide2.QtGui.PySide2.QtGui.QTextCursor.MoveOperation
            self.ui.output_box.setTextCursor(cursor)

        # 自定义信号绑定函数
        main_win_signal.appendOutPutBox.connect(appendOutPut)
        main_win_signal.setOutPutBox.connect(setOutPut)
        main_win_signal.clearOutPutBox.connect(clearOutPut)
        main_win_signal.getOutPutBox.connect(getOutPut)
        main_win_signal.setStartButtonText.connect(setStartButtonText)
        main_win_signal.setStartButtonState.connect(setStartButtonState)
        main_win_signal.setOutPutBoxCursor.connect(setOutPutBoxCursor)

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
            if self.ui.list_choices_plugin.currentItem() is None:  # 是否选择检测
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
            if self.ui.check_save.isChecked():  # 检测保存按钮的状态判断是否保存
                calculation_mode = "calculate_save"
            else:  # 选择不保存才输出结果
                if self.ui.check_output_optimization.isChecked():
                    if self.ui.check_output_lock_maximums.isChecked():
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

    def flushListChoicesPlugin(self):
        """
        刷新左侧列表 和对应映射表
        
        :return: None
        """
        self.plugin_option_id_dict = instance_plugin_manager.getOptionIdDict()  # 选项名映射id（文件或文件夹名）
        self.selection_list = self.plugin_option_id_dict.keys()  # 选项名列表
        self.ui.list_choices_plugin.addItems(
            self.selection_list
        )  # 选项名添加到ui上

    def resizeEvent(self, event):
        """
        窗口大小改变时间 实现自适应背景图片

        :param event:
        :return:
        """
        # don't forget to call the resizeEvent() of super class
        super().resizeEvent(event)
        # print("resizeEvent",self.width(), self.height())
        # self.ui.central_widget.resize(length, length)
        # self.ui.central_widget.move(
        #     self.width() // 2 - length // 2,
        #     self.height() // 2 - length // 2
        # )

        if not self.bg_img:
            return

        def _adapt_bg(image):
            """自适应图片"""
            return image.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.FastTransformation)
            # return image.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        palette = QPalette()
        img = _adapt_bg(self.bg_img)  # 转换为自适应大小的图片
        palette.setBrush(QPalette.Window, QBrush(img))
        self.setPalette(palette)

    def minimizeEvent(self):
        """
        最小化窗口

        :return:
        """
        self.showMinimized()

    def maximizeEvent(self):
        """
        最大化窗口，和窗口还原

        :return:
        """
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mouseDoubleClickEvent(self, event):
        """
        双击框体的最大化和还原

        :param event:
        :return:
        """
        self.maximizeEvent()

    def mousePressEvent(self, event):
        """
        鼠标按下的事件

        :param event:
        :return:
        """
        self.start_mouse_pos = event.globalPos()  # 鼠标点击位置
        self.origin_win_pos = self.pos()  # 窗口位置

    def mouseMoveEvent(self, event):
        """
        鼠标移动窗口

        :param event:
        :return:
        """
        if self.isMaximized():
            self.showNormal()  # 有个动画，所以会瞬移一下
            self.move_fix = True  # 需要按照比例将窗口移动到鼠标的对应位置
            self.start_mouse_pos = event.globalPos()  # 鼠标点击位置
            return
        if self.move_fix:
            screen = QGuiApplication.primaryScreen().geometry()  # 屏幕类并调用geometry获取屏幕大小
            screen_width = screen.width()  # 屏幕的宽
            screen_height = screen.height()  # 屏幕的高
            # print("屏幕大小",screen_width,screen_height)
            # print("窗口大小2 玄学",self.width(),self.height())
            # print("屏幕大小和原来鼠标点击位置的比值",(self.start_mouse_pos.x() / screen_width),(self.start_mouse_pos.y() / screen_height))
            # print("目前鼠标点击位置",event.globalPos().x(),event.globalPos().y())
            # print("原来鼠标点击位置",self.start_mouse_pos)
            # print("相对于窗口左上角的新位置", (self.start_mouse_pos.x() / screen_width) * self.width(),(self.start_mouse_pos.y() / screen_height) * self.height())
            # print("新计算位置",event.globalPos().x() - (self.start_mouse_pos.x() / screen_width) * self.width(), event.globalPos().y() - ( self.start_mouse_pos.y()/ screen_height) * self.height())
            # 这里的self.start_mouse_pos是全屏状态下点击的位置
            self.move(event.globalPos().x() - (self.start_mouse_pos.x() / screen_width) * self.width(), event.globalPos().y() - (self.start_mouse_pos.y() / screen_height) * self.height())
            self.move_fix = False
            # print("self.start_mouse_pos1.9", self.origin_win_pos)
            self.start_mouse_pos = event.globalPos()  # 鼠标点击位置 可能可以注释掉这句
            # print("self.start_mouse_pos2", self.origin_win_pos)
            # print("窗口位置1.9", self.origin_win_pos)
            self.origin_win_pos = self.pos()  # 窗口位置重置到新位置
            # print("窗口位置2", self.origin_win_pos)
            return
        # print("self.start_mouse_pos2.1!=2", self.start_mouse_pos)
        # print("窗口位置2.1=2", self.origin_win_pos)
        move_pos = event.globalPos() - self.start_mouse_pos  # 目前鼠标的位置和之前鼠标的位置的坐标差
        self.move(self.origin_win_pos + move_pos)  # 原本窗口的位置加上坐标差成为新窗口的位置

    def chooseOptionEvent(self, item):
        """
        左侧选择算法之后触发的函数 选择算法事件

        :param item:
        :return: None
        """
        # logging.debug(f'选中的选项名{self.ui.list_choices_plugin.currentItem().text()}')
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

    def quitEvent(self):
        """
        退出程序

        :return:
        """
        sys.exit(0)

    def openAboutWin(self):
        """
        打开关于窗口

        :return:
        """
        self.about_win = AboutWinApp()  # 绑定子窗口
        self.about_win.exec()

    def openSettingWin(self):
        """
        打开设置窗口

        :return:
        """
        self.setting_win = SettingWinApp()  # 绑定子窗口
        self.setting_win.exec()
        with shelve.open(
                self.SETTING_FILE_PATH, writeback=True
        ) as setting_file:  # 读取设置文件
            self.OUTPUT_DIR_PATH = setting_file["output_dir_path"]
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
                setting_file["is_save"] = self.ui.check_save.isChecked()

    def outputOptimizationCheckEvent(self):
        """
        当触发优化输出选项

        :return: None
        """
        if self.ui.check_output_optimization.isChecked():
            if self.is_save_settings:  # 保存check设置
                with shelve.open(
                        self.SETTING_FILE_PATH, writeback=True
                ) as setting_file:  # 读取设置文件
                    setting_file[
                        "output_optimization"
                    ] = self.ui.check_output_optimization.isChecked()
        else:
            self.ui.check_output_lock_maximums.setChecked(False)
            if self.is_save_settings:  # 保存check设置
                with shelve.open(
                        self.SETTING_FILE_PATH, writeback=True
                ) as setting_file:  # 读取设置文件
                    setting_file["output_lock_maximums"] = False
                    setting_file[
                        "output_optimization"
                    ] = self.ui.check_output_optimization.isChecked()

    def outputLockMaximumsCheckEvent(self):
        """
        当触发锁内框输出上限选项，开启锁上限需要同时开启输出优化

        :return: None
        """
        if self.ui.check_output_lock_maximums.isChecked():
            self.ui.check_output_optimization.setChecked(True)
            if self.is_save_settings:  # 保存check设置
                with shelve.open(
                        self.SETTING_FILE_PATH, writeback=True
                ) as setting_file:  # 读取设置文件
                    setting_file["output_optimization"] = True
                    setting_file[
                        "output_lock_maximums"
                    ] = self.ui.check_output_lock_maximums.isChecked()  # True
        else:
            if self.is_save_settings:  # 保存check设置
                with shelve.open(
                        self.SETTING_FILE_PATH, writeback=True
                ) as setting_file:  # 读取设置文件
                    setting_file[
                        "output_lock_maximums"
                    ] = self.ui.check_output_lock_maximums.isChecked()  # False

    def searchText(self):
        """
        搜索框字符修改后触发的事件

        :return: None
        """
        search_keyword = self.ui.search_plugin.toPlainText()
        logging.debug(f"search_keyword:{search_keyword}")

        if search_keyword == "":
            self.searchCancel()
            return None

        self.ui.list_choices_plugin.clear()  # 清空选择栏

        for i in self.selection_list:  # 选出符合要求的
            if i.find(search_keyword) == -1:  # 字符串方法，没找到指定子串就-1
                continue
            self.ui.list_choices_plugin.addItem(i)
        return None

    def searchCancel(self):
        """
        取消搜索结果，显示全部插件

        :return: None
        """
        self.ui.list_choices_plugin.clear()
        self.ui.list_choices_plugin.addItems(self.selection_list)
