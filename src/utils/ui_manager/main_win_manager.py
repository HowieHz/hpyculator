import locale
import pathlib
import importlib
import sys
from dataclasses import dataclass
from typing import Any, Optional

import hpyculator as hpyc
from hpyculator.hpysignal import instance_main_win_signal
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QGuiApplication, QPalette, QPixmap, QTextCursor

from .about_win_manager import AboutWinApp
from .settings_win_manager import SettingsWinApp  # 窗口管理类（用于管理设置的窗口）
from .. import document as doc
from ..calculate import CalculationManager  # 计算管理
from ..plugin import instance_plugin_manager  # 插件管理
from ..pyside_frameless_win.framelesswindow import (
    FramelessWindow,
)  # refer to https://github.com/zhiyiYo/PyQt-Frameless-Window
from ..settings import instance_settings_file  # 设置文件实例
from ..ui import Ui_MainWin


@dataclass
class default_widget_state:
    """
    settings_key 设置文件键名
    default_state 初始化状态
    widget 控件对象
    """

    settings_key: str
    default_state: bool
    widget: Any


class MainWinApp(FramelessWindow):
    def __init__(
        self,
        setting_file_path: str,
        output_dir_path: str,
        plugin_dir_path: str,
        background_dir_path: str,
    ):
        """
        主窗口程序类

        :param setting_file_path: 用于修改设置 设置文件路径
        :param output_dir_path:  用于输出结果 输出路径
        :param plugin_dir_path:  用于存放插件 插件文件夹路径
        :param background_dir_path:  用于存放背景图片的路径
        """
        # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
        self.SETTING_FILE_PATH: str = setting_file_path
        self.OUTPUT_DIR_PATH: str = output_dir_path
        self.PLUGIN_DIR_PATH: str = plugin_dir_path
        self.user_selection_id: str = ""  # 用户选择的插件的文件名（id)
        self.background_dir_path: str = background_dir_path  # 用于存放背景图片的路径
        self.is_save_check_box_status: Optional[bool] = None  # 是否保存按键状态

        super().__init__()
        self.ui = Ui_MainWin()  # UI类的实例化()
        self.ui.setupUi(self)  # ui初始化

        self.setWindowTitle(f"hpyculator {doc.VERSION}")  # 设置标题

        self.move_fix = False  # 一个窗口全屏之后，拖动，窗口会回到正常大小，且指针和在窗口长度和比值和原来一致,True的话就进行校正

        self.initCheck()  # 初始化checkbox和储存check的设置文件
        self.bindSignalWithSlots()  # 信号和槽的绑定 (先初始设置文件和check)

        # 初始化背景图片
        if instance_settings_file.exists("background_img"):
            # noinspection PyTypeChecker
            background_img_path = pathlib.Path(background_dir_path).joinpath(
                instance_settings_file.read("background_img")
            )
            # print(pathlib.Path().cwd())
        else:
            background_img_path = pathlib.Path(background_dir_path).joinpath(
                "default.png"
            )
            instance_settings_file.add("background_img", "default.png")

        if background_img_path.is_file():
            self.bg_img = QPixmap(background_img_path)

        self.is_thread_running = [False]  # 防止反复启动计算线程

        # 关于gui显示内容的初始化
        self.flushListChoicesPlugin()
        self.ui.search_plugin.setPlaceholderText(doc.SEARCH_INPUT_BOX_TIPS)  # 灰色背景提示字符
        self.ui.search_plugin.clear()  # 不清空不显示灰色背景
        self.ui.input_box.setFocus()  # 设置焦点

        # 主输出框内容初始化
        self.outputIntroduce()

    def outputIntroduce(self) -> None:
        self.ui.output_box.setPlainText(doc.START_SHOW)  # 开启的展示
        self.outputAvailableTag()  # 展示可用tag

    def outputAvailableTag(self) -> None:
        """
        展示可用tag

        :return: None
        """
        self.ui.output_box.appendPlainText(f"\n{doc.AVAILABLE_TAGS_LITERAL}\n")
        # tag和选项名的映射表_list_plugin_tag_option [(plugin1_tags: list, plugin1_option), (plugin2_tags: list, plugin2_option)]
        _list_plugin_tag_option: (
            tuple[tuple[tuple[str, ...], str], ...]
        ) = instance_plugin_manager.list_alL_plugin_tag_option
        _set_tags = set()  # _set_tags里面有所有的tag
        for _tags_and_option in _list_plugin_tag_option:
            for _tag in _tags_and_option[0]:
                _set_tags.add(_tag)  # _set_tags里面有所有的tag

        special_tags: tuple[str, ...] = doc.tags.SPECIAL_TAGS  # 读取特殊tag

        _dict_set_tags: dict[str, set[str]] = {}
        # {"special_tag1":{"tag1","tag2"}, "special_tag2":{"tag1","tag2"}, "special_tag3":{"tag1","tag2"}, "special_tag4":{"tag1","tag2"}}

        for _special_tag in special_tags:  # 初始化特殊tag的set
            _dict_set_tags[_special_tag] = set()

        for _tag in _set_tags:  # _set_tags里面有所有的tag
            for _special_tag in special_tags:  # 读取并分类特殊tag
                if _tag[: len(_special_tag)] == _special_tag:  # 检查tag开头是否是特殊tag
                    _dict_set_tags[_special_tag].add(_tag)  # 分到对应的类别
                    break
            else:  # 没break的就是普通tag，直接添加
                self.ui.output_box.appendPlainText(f"    {_tag}")  # 输出普通tag

        for _special_tag in special_tags:  # 输出特殊tag
            # tag标题i18n并输出
            if locale.getdefaultlocale()[0] in doc.tags.SPECIAL_TAGS_TRANSLATOR:
                _lang: str = locale.getdefaultlocale()[0]  # type: ignore  # 确实返回的是str而不是Optional[str]
                self.ui.output_box.appendPlainText(
                    f"    {doc.tags.SPECIAL_TAGS_TRANSLATOR[_lang][_special_tag]}"
                )
            else:
                self.ui.output_box.appendPlainText(
                    f"    {_special_tag}"
                )  # 输出无i18n的特殊tag标题

            for _tag in _dict_set_tags[_special_tag]:
                self.ui.output_box.appendPlainText(f"        {_tag}")  # 输出特殊tag

    def _appendTextMakeContainer(self, msg: str):
        self.ui.output_box.appendPlainText(f"{msg},")

    def _insertTextMakeContainer(self, msg: str):
        self.ui.output_box.insertPlainText(f"{msg},")

    def bindSignalWithSlots(self) -> None:
        """绑定信号和槽"""
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)
        # my_signal.setProgressBar.connect(self.set_progress_bar)
        # my_signal.setResult.connect(self.set_result)

        self.ui.button_close.clicked.connect(self.eventCloseMainWin)
        self.ui.button_start.clicked.connect(self.eventStartCalculation)
        self.ui.button_setting.clicked.connect(self.eventOpenSettingWin)
        self.ui.button_minimize.clicked.connect(self.eventMinimize)
        self.ui.button_maximum.clicked.connect(self.eventMaximize)
        self.ui.button_about.clicked.connect(self.eventOpenAboutWin)

        self.ui.check_save.clicked.connect(self.eventSaveCheck)
        self.ui.check_output_optimization.clicked.connect(
            self.eventOutputOptimizationCheck
        )
        self.ui.check_output_lock_maximums.clicked.connect(
            self.eventOutputLockMaximumsCheck
        )
        self.ui.check_auto_wrap.clicked.connect(self.eventAutoWrapCheck)
        self.ui.check_make_container.clicked.connect(self.eventMakeContainer)

        self.ui.search_plugin.textChanged.connect(self.eventSearch)
        self.ui.list_choices_plugin.currentItemChanged.connect(
            self.eventChooseOption
        )  # _: QListWidgetItem*

        def _setOutputBoxCursor(where: str) -> None:  # 目前只有end
            _cursor = self.ui.output_box.textCursor()
            _cursor_state_map = {
                "end": QTextCursor.End,
                "start": QTextCursor.Start,
                "up": QTextCursor.Up,
            }
            _cursor.movePosition(_cursor_state_map[where])
            # https://doc.qt.io/qtforpython-5/PySide2/QtGui/QTextCursor.html#PySide2.QtGui.PySide2.QtGui.QTextCursor.MoveOperation
            self.ui.output_box.setTextCursor(_cursor)

        # 自定义信号绑定函数
        instance_main_win_signal.append_output_box_.connect(
            self.ui.output_box.appendPlainText
        )  # 输出前会添加换行符
        instance_main_win_signal.insert_output_box_.connect(
            self.ui.output_box.insertPlainText
        )  # 输出前不会添加换行符

        if self.ui.check_make_container.isChecked():
            instance_main_win_signal.append_output_box.connect(
                self._appendTextMakeContainer
            )  # 输出前会添加换行符
            instance_main_win_signal.insert_output_box.connect(
                self._insertTextMakeContainer
            )  # 输出前不会添加换行符
        else:
            instance_main_win_signal.append_output_box.connect(
                self.ui.output_box.appendPlainText
            )  # 输出前会添加换行符
            instance_main_win_signal.insert_output_box.connect(
                self.ui.output_box.insertPlainText
            )  # 输出前不会添加换行符

        instance_main_win_signal.set_output_box.connect(self.ui.output_box.setPlainText)
        instance_main_win_signal.clear_output_box.connect(self.ui.output_box.clear)
        instance_main_win_signal.get_output_box.connect(
            lambda: hpyc.setOutPutData(self.ui.output_box.toPlainText())
        )

        instance_main_win_signal.set_start_button_text.connect(
            self.ui.button_start.setText
        )
        instance_main_win_signal.set_start_button_state.connect(
            self.ui.button_start.setEnabled
        )

        instance_main_win_signal.set_output_box_cursor.connect(_setOutputBoxCursor)

        instance_main_win_signal.draw_background.connect(self.drawBackground)

    def initCheck(self) -> None:
        """
        初始化check box

        :return:
        """
        # 初始化控件
        _default_state = (
            default_widget_state(
                settings_key="is_save", default_state=False, widget=self.ui.check_save
            ),
            default_widget_state(
                settings_key="output_optimization",
                default_state=False,
                widget=self.ui.check_output_optimization,
            ),
            default_widget_state(
                settings_key="output_lock_maximums",
                default_state=False,
                widget=self.ui.check_output_lock_maximums,
            ),
            default_widget_state(
                settings_key="auto_wrap",
                default_state=True,
                widget=self.ui.check_auto_wrap,
            ),
            default_widget_state(
                settings_key="make_container",
                default_state=False,
                widget=self.ui.check_make_container,
            ),
        )

        # 读取设置文件-按钮状态和输出目录  check控件初始化

        if instance_settings_file.exists(key="is_save_check_box_status"):
            # 是否保存设置
            self.is_save_check_box_status = instance_settings_file.read(
                key="is_save_check_box_status"
            )
            if self.is_save_check_box_status:  # 当保存check状态 所要读取和设置的控件 以及这个设置项不存在时的初始化
                for sequence in _default_state:
                    # 存在这个键就读取
                    if instance_settings_file.exists(key=sequence.settings_key):
                        sequence.widget.setChecked(
                            instance_settings_file.read(key=sequence.settings_key)
                        )  # 根据数据设置选项状态
                    else:  # 不存在就初始化
                        instance_settings_file.add(
                            key=sequence.settings_key, value=sequence.default_state
                        )  # 初始化设置文件中对应的项
                        sequence.widget.setChecked(sequence.default_state)  # 初始化控件
            else:  # 当不保存check状态 设置控件状态
                for sequence in _default_state:
                    sequence.widget.setChecked(sequence.default_state)  # 初始化控件
        else:
            # 第一遍启动初始化设置
            instance_settings_file.add(
                key="is_save_check_box_status", value=False
            )  # 默认不保存按键状态
            for sequence in _default_state:
                instance_settings_file.add(
                    key=sequence.settings_key, value=sequence.default_state
                )  # 初始化设置文件中对应的项
                sequence.widget.setChecked(sequence.default_state)  # 初始化控件
            self.is_save_check_box_status = False  # 默认不保存按键状态

    def eventStartCalculation(
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
        # 有就录入测试数据 没有就从输入框获取
        input_data = test_input if test_input else self.ui.input_box.toPlainText()
        # 输入检查
        if input_data == "":  # 是否输入检测
            self.ui.output_box.setPlainText(doc.USER_NO_INPUT)
            return

        # 选择的插件id
        # 被用户选择的插件，这个插件的id为user_selection_id
        user_selection_id = (
            test_selection_id if test_selection_id else self.user_selection_id
        )
        if self.ui.list_choices_plugin.currentItem() is None:  # 是否选择检测
            self.ui.output_box.setPlainText(doc.USER_NO_CHOOSE)
            return

        # 输入转换类型
        # 有就录入测试数据 没有就从属性列表获取
        input_mode = (
            test_input_mode
            if test_input_mode
            else self.selected_plugin_attributes["input_mode"]
        )

        # 获取计算模式
        def _getCalculationMode(mode):
            if mode:
                return mode  # 有就录入测试数据
            if self.ui.check_save.isChecked():  # 检测保存按钮的状态判断是否保存
                return "calculate_save"
            if not self.ui.check_output_optimization.isChecked():
                return "calculate"
            if self.ui.check_output_lock_maximums.isChecked():
                return "calculate_o_l"  # l=limit
            return "calculate_o"

        calculation_mode = _getCalculationMode(test_calculation_mode)

        output_dir_path = (
            test_output_dir_path if test_output_dir_path else self.OUTPUT_DIR_PATH
        )
        # 以上是计算前工作
        # print("启动计算")
        calculate_manager = CalculationManager()
        calculate_manager.start(
            inputbox_data=input_data,
            plugin_attribute_input_mode=input_mode,
            calculation_mode=calculation_mode,
            user_selection_id=user_selection_id,
            output_dir_path=output_dir_path,
        )  # 启动计算
        return

    def flushListChoicesPlugin(self) -> None:
        """
        刷新左侧列表 和对应映射表

        :return: None
        """
        self.ui.list_choices_plugin.clear()
        self.ui.list_choices_plugin.addItems(
            instance_plugin_manager.option_id_dict.keys()
        )  # 选项名添加到ui上 选项名映射id（文件或文件夹名）

    def resizeEvent(self, event) -> None:
        """
        窗口大小改变 实现自适应背景图片

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
        self.drawBackground()

    def drawBackground(self) -> None:
        """
        绘制背景

        :return:
        """
        try:
            if not self.bg_img:
                return
        except AttributeError:  # 无self.bg_img
            return

        def _adaptBackground(image: QPixmap):
            """自适应图片"""
            return image.scaled(
                self.width(),
                self.height(),
                Qt.KeepAspectRatioByExpanding,
                Qt.FastTransformation,
            )
            # todo 添加一个设置选项，背景图是高质量还是低质量
            # return image.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        palette = QPalette()
        img = _adaptBackground(self.bg_img)  # 转换为自适应大小的图片
        palette.setBrush(QPalette.Window, QBrush(img))
        self.setPalette(palette)

    def eventMinimize(self) -> None:
        """
        最小化窗口

        :return:
        """
        self.showMinimized()

    def eventMaximize(self) -> None:
        """
        最大化窗口，和窗口还原

        :return:
        """
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mouseDoubleClickEvent(self, event) -> None:
        """
        双击框体的最大化和还原

        :param event:
        :return:
        """
        self.eventMaximize()

    def mousePressEvent(self, event) -> None:
        """
        鼠标按下的事件

        :param event:
        :return:
        """
        self.start_mouse_pos = event.globalPos()  # 鼠标点击位置
        self.origin_win_pos = self.pos()  # 窗口位置

    def mouseMoveEvent(self, event) -> None:
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
            self.move(
                event.globalPos().x()
                - (self.start_mouse_pos.x() / screen_width) * self.width(),
                event.globalPos().y()
                - (self.start_mouse_pos.y() / screen_height) * self.height(),
            )
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

    def eventChooseOption(self, item) -> None:
        """
        左侧选择算法之后触发的函数 选择算法事件

        :param item:
        :return: None
        """
        # print(f"选中的选项名{item.text()}")
        if item is None:  # 刷新列表的时候选中的item是None
            return
        self.user_selection_id = str(
            instance_plugin_manager.option_id_dict[item.text()]
        )  # 转换成ID
        self.selected_plugin_attributes = (
            _METADATA
        ) = instance_plugin_manager.getPluginAttributes(self.user_selection_id)
        self.ui.output_box.setPlainText(
            f"""\
{_METADATA["output_start"]}
{_METADATA["output_name"]} {_METADATA["version"]}
by {", ".join(_METADATA['author']) if isinstance(_METADATA['author'], list) else _METADATA['author']}


{doc.TIPS_FOR_USE_LITERAL}
{_METADATA["help"]}

{_METADATA["output_end"]}"""
        )

    def closeEvent(self, event):
        """
        重构退出函数，处理可能导致子进程残留的模块

        :param event:
        :return:
        """

        def _exitJpype():
            # 退出流程，否则虚拟机不会退出，导致进程残留
            jpype = importlib.import_module("jpype")  # 不直接用import是防止打包程序识别到

            if jpype.isJVMStarted():
                jpype.shutdownJVM()

        _check_modules = {"jpype": _exitJpype}
        for _module in _check_modules:
            if _module in sys.modules:
                _check_modules[_module]()  # 调用对应退出处理函数

    def eventCloseMainWin(self) -> None:
        """
        关闭主窗口

        :return:
        """
        self.close()

    def eventOpenAboutWin(self) -> None:
        """
        打开关于窗口

        :return:
        """
        self.about_win = AboutWinApp()  # 绑定子窗口
        self.about_win.exec()

    def eventOpenSettingWin(self) -> None:
        """
        打开设置窗口

        :return:
        """
        self.settings_win = SettingsWinApp()  # 绑定子窗口
        self.settings_win.exec()

        # 读取新设置
        self.OUTPUT_DIR_PATH = instance_settings_file.read("output_dir_path")
        self.is_save_check_box_status = instance_settings_file.read(
            "is_save_check_box_status"
        )

        self.initCheck()  # 初始化checkbox

        background_img_path = pathlib.Path(self.background_dir_path).joinpath(
            instance_settings_file.read("background_img")
        )
        self.bg_img = (
            QPixmap(background_img_path) if background_img_path.is_file() else ""
        )
        self.drawBackground()

    def eventSaveCheck(self) -> None:
        """
        当触发保存选项（那个√）事件

        :return: None
        """
        if self.is_save_check_box_status:  # 保存check设置
            instance_settings_file.modify(
                key="is_save", value=self.ui.check_save.isChecked()
            )

    def eventOutputOptimizationCheck(self) -> None:
        """
        当触发优化输出选项

        :return: None
        """
        if (
            self.ui.check_output_optimization.isChecked()
            and self.is_save_check_box_status
        ):  # 保存check设置 并且是True选择
            instance_settings_file.modify(key="output_optimization", value=True)
            return

        # 关联最大限制选择项
        self.ui.check_output_lock_maximums.setChecked(False)
        if self.is_save_check_box_status:  # 保存check设置
            (
                instance_settings_file.modify(
                    key="output_lock_maximums", value=False
                ).modify(key="output_optimization", value=False)
            )

    def eventOutputLockMaximumsCheck(self) -> None:
        """
        当触发锁内框输出上限选项，开启锁上限需要同时开启输出优化

        :return: None
        """
        if (
            not self.ui.check_output_lock_maximums.isChecked()
            and self.is_save_check_box_status
        ):  # 保存check设置 并且是False选择
            instance_settings_file.modify(key="output_lock_maximums", value=False)
            return

        # 关联最大优化输出选项
        self.ui.check_output_optimization.setChecked(True)
        if self.is_save_check_box_status:  # 保存check设置
            (
                instance_settings_file.modify(
                    key="output_optimization", value=True
                ).modify(key="output_lock_maximums", value=True)
            )

    def eventAutoWrapCheck(self) -> None:
        """
        当点击切换 是否自动换行的勾勾

        :return:
        """
        if self.is_save_check_box_status:  # 保存check设置
            instance_settings_file.modify(
                key="auto_wrap", value=self.ui.check_auto_wrap.isChecked()
            )

        if self.ui.check_auto_wrap.isChecked():
            self.ui.output_box.setLineWrapMode(self.ui.output_box.WidgetWidth)
            self.ui.input_box.setLineWrapMode(self.ui.input_box.WidgetWidth)
        else:
            self.ui.output_box.setLineWrapMode(self.ui.output_box.NoWrap)
            self.ui.input_box.setLineWrapMode(self.ui.input_box.NoWrap)

    def eventMakeContainer(self) -> None:
        """
        开关控制打表法

        :return:
        """
        if self.is_save_check_box_status:  # 保存check设置
            instance_settings_file.modify(
                key="make_container", value=self.ui.check_make_container.isChecked()
            )

        if self.ui.check_make_container.isChecked():
            instance_main_win_signal.append_output_box.disconnect(
                self.ui.output_box.appendPlainText
            )  # 输出前会添加换行符
            instance_main_win_signal.insert_output_box.disconnect(
                self.ui.output_box.insertPlainText
            )  # 输出前不会添加换行符
            instance_main_win_signal.append_output_box.connect(
                self._appendTextMakeContainer
            )  # 输出前会添加换行符
            instance_main_win_signal.insert_output_box.connect(
                self._insertTextMakeContainer
            )  # 输出前不会添加换行符
        else:
            instance_main_win_signal.append_output_box.disconnect(
                self._appendTextMakeContainer
            )  # 输出前会添加换行符
            instance_main_win_signal.insert_output_box.disconnect(
                self._insertTextMakeContainer
            )  # 输出前不会添加换行符
            instance_main_win_signal.append_output_box.connect(
                self.ui.output_box.appendPlainText
            )  # 输出前会添加换行符
            instance_main_win_signal.insert_output_box.connect(
                self.ui.output_box.insertPlainText
            )  # 输出前不会添加换行符

    def eventSearch(self) -> None:
        """
        搜索框字符修改后触发的事件

        :return: None
        """

        def _tagCheck(user_tags: list[str], plugin_tags: tuple[str, ...]) -> bool:
            """
            检查此项是否符合tag

            :param user_tags: 用户输入的tag ["tag1","tag2"]
            :param plugin_tags: 插件的tag  (tag1,tag2)
            :return:
            """
            return all(
                (user_tag in plugin_tags) for user_tag in user_tags
            )  # 检查用户输入的tags是否是插件的tags的子集

        _search_keyword = self.ui.search_plugin.toPlainText()

        if _search_keyword == "":
            self.eventSearchCancel()
            return None

        self.ui.list_choices_plugin.clear()  # 清空选择栏
        if _search_keyword[:4] == ":tag" or _search_keyword[:4] == "：tag":  # 进入tag搜索模式
            self.ui.output_box.clear()  # 清空输出框
            self.outputAvailableTag()  # 显示可用tag
            instance_main_win_signal.set_output_box_cursor.emit("start")  # 设置光标到输入框开头

            _set_matched_item = set()  # 匹配上的插件名
            _, *_user_tags = _search_keyword.split()  # 第一项是:tag, 剩下的是用户输入的tag

            # instance_plugin_manager.list_alL_plugin_tag_option 单项 tag和选项名_tags_and_option ((tag1,tag2),name)
            for _tags_and_option in instance_plugin_manager.list_alL_plugin_tag_option:
                if _tagCheck(
                    _user_tags, _tags_and_option[0]
                ):  # _tags_and_option[0] -> plugin_tags: tuple[list]
                    _set_matched_item.add(
                        _tags_and_option[1]
                    )  # _tags_and_option[1] -> plugin_option: str

            self.ui.list_choices_plugin.addItems(_set_matched_item)  # 匹配的添加到选框
            return None

        for i in instance_plugin_manager.option_id_dict:  # 选出符合要求的
            if i.find(_search_keyword) == -1:  # 字符串方法，没找到指定子串就-1
                continue
            self.ui.list_choices_plugin.addItem(i)
        return None

    def eventSearchCancel(self) -> None:
        """
        取消搜索结果，显示全部插件，显示介绍

        :return: None
        """
        self.ui.list_choices_plugin.clear()
        self.ui.list_choices_plugin.addItems(
            instance_plugin_manager.option_id_dict.keys()
        )
        self.outputIntroduce()  # 输出介绍
