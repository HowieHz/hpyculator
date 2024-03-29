import locale
import pathlib
import time
from dataclasses import dataclass
from typing import Any, Optional
from queue import Queue
from threading import Thread

import hpyculator as hpyc
from hpyculator import SettingsFileObject
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QGuiApplication, QPalette, QPixmap, QTextCursor

from .signal import instance_main_win_signal
from .about_win_manager import AboutWinApp
from .settings_win_manager import SettingsWinApp  # 窗口管理类（用于管理设置的窗口）
from .. import document as doc
from ..var import instance_core
from qframelesswindow import FramelessWindow
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
        plugins_dir_path: str,
        background_dir_path: str,
        message_queue: Queue,
        instance_settings: SettingsFileObject,
    ):
        """主窗口程序类

        :param setting_file_path: 用于修改设置 设置文件路径
        :param output_dir_path: 用于输出结果 输出路径
        :param plugins_dir_path: 用于存放插件 插件文件夹路径
        :param background_dir_path: 用于存放背景图片的路径
        """
        # 初始化（变量初始化，文件夹初始化，读取设置（创建设置文件））
        global instance_settings_file
        instance_settings_file = instance_settings

        self.SETTING_FILE_PATH: str = setting_file_path
        self.OUTPUT_DIR_PATH: str = output_dir_path
        self.PLUGINS_DIR_PATH: str = plugins_dir_path
        self.user_selection_id: str = ""  # 用户选择的插件的文件名（id)
        self.background_dir_path: str = background_dir_path  # 用于存放背景图片的路径
        self.is_save_check_box_status: Optional[bool] = None  # 是否保存按键状态
        self.message_queue: Queue = message_queue

        super().__init__()
        self.ui = Ui_MainWin()  # UI类的实例化()
        self.ui.setupUi(self)  # ui初始化

        self.titleBar.hide()  # 隐藏默认标题栏

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
        """展示可用tag"""
        self.ui.output_box.appendPlainText(f"\n{doc.AVAILABLE_TAGS_LITERAL}\n")
        # tag和选项名的映射表_list_plugin_tag_option [(plugin1_tags: list, plugin1_option), (plugin2_tags: list, plugin2_option)]
        _list_plugin_tag_option: (
            tuple[tuple[tuple[str, ...], str], ...]
        ) = instance_core.getPluginsTagOption()
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
        """初始化check boxs"""
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
        test_input: None | int | str | float = None,
        test_selection_id: str | None = None,
    ) -> None:
        """输入检查，启动计算，输出计算结果

        :param test_input: 测试输入，测试专用, defaults to None
        :type test_input: None | int | str | float, optional
        :param test_input_mode: 测试模式，测试专用, defaults to None
        :type test_input_mode: int | None, optional
        :param test_selection_id: 测试选择id，测试专用, defaults to None
        :type test_selection_id: str | None, optional
        :param test_output_dir_path: 测试专用，测试目录, defaults to None
        :type test_output_dir_path: str | None, optional
        :return: None
        :rtype: None
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

        # 获取计算模式
        def _getCalculationMode():
            if self.ui.check_save.isChecked():  # 检测保存按钮的状态判断是否保存
                return "Save"
            if not self.ui.check_output_optimization.isChecked():
                return "Return"
            if self.ui.check_output_lock_maximums.isChecked():
                return "ReturnFromLimitedBuffer"
            return "ReturnFromBuffer"

        calculation_mode = _getCalculationMode()

        # 以上是计算前工作
        instance_core.eventStartCalculate(
            plugin_id=user_selection_id, input_data=input_data, mode=calculation_mode
        )

        # 实例化消息处理线程
        message_processing_thread = MessageProcessingThread(
            mode=calculation_mode, message_queue=self.message_queue
        )
        # 启动消息处理线程
        message_processing_thread.start()
        return

    def flushListChoicesPlugin(self) -> None:
        """刷新左侧列表 和对应映射表"""
        self.ui.list_choices_plugin.clear()
        self.ui.list_choices_plugin.addItems(
            instance_core.getPluginsOptionToId()
        )  # 选项名添加到ui上 选项名映射id（文件或文件夹名）

    def resizeEvent(self, event) -> None:
        """
        窗口大小改变 实现自适应背景图片

        :param event: just event
        :return: None
        :rtype: None
        """
        super().resizeEvent(event)
        self.drawBackground()

    def drawBackground(self) -> None:
        """绘制背景"""
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
        """最小化窗口"""
        self.showMinimized()

    def eventMaximize(self) -> None:
        """最大化窗口，和窗口还原"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mouseDoubleClickEvent(self, event) -> None:
        """
        双击框体的最大化和还原

        :param event: just event
        :return: None
        :rtype: None
        """
        self.eventMaximize()

    def mousePressEvent(self, event) -> None:
        """
        鼠标按下的事件

        :param event: just event
        :return: None
        :rtype: None
        """
        self.start_mouse_pos = event.globalPos()  # 鼠标点击位置
        self.origin_win_pos = self.pos()  # 窗口位置

    def mouseMoveEvent(self, event) -> None:
        """
        鼠标移动窗口

        :param event: just event
        :return: None
        :rtype: None
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

        :param item: just item
        :return: None
        :rtype: None
        """
        # print(f"选中的选项名{item.text()}")
        if item is None:  # 刷新列表的时候选中的item是None
            return
        self.user_selection_id = str(
            instance_core.getPluginIdFromOption(item.text())
        )  # 转换成ID
        self.selected_plugin_attributes = _METADATA = instance_core.getPluginMetadata(
            self.user_selection_id
        )
        self.ui.output_box.setPlainText(
            f"""\
{_METADATA["output_start"]}
{_METADATA["output_name"]} {_METADATA["version"]}
by {", ".join(_METADATA['author']) if isinstance(_METADATA['author'], list) else _METADATA['author']}


{doc.TIPS_FOR_USE_LITERAL}
{_METADATA["help"]}

{_METADATA["output_end"]}"""
        )

    def eventCloseMainWin(self) -> None:
        """关闭主窗口"""
        self.close()

    def eventOpenAboutWin(self) -> None:
        """打开关于窗口"""
        self.about_win = AboutWinApp()  # 绑定子窗口
        self.about_win.exec()

    def eventOpenSettingWin(self) -> None:
        """打开设置窗口"""
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
        """当触发保存选项（那个√）事件"""
        if self.is_save_check_box_status:  # 保存check设置
            instance_settings_file.modify(
                key="is_save", value=self.ui.check_save.isChecked()
            )

    def eventOutputOptimizationCheck(self) -> None:
        """当触发优化输出选项"""
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
        """当触发锁内框输出上限选项，开启锁上限需要同时开启输出优化"""
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
        """当点击切换 是否自动换行的勾勾"""
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
        """开关控制打表法"""
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
        """搜索框字符修改后触发的事件"""

        def _tagCheck(user_tags: list[str], plugin_tags: tuple[str, ...]) -> bool:
            """检查此项是否符合tag

            :param user_tags: 用户输入的tag ["tag1","tag2"]
            :type user_tags: list[str]
            :param plugin_tags: 插件的tag  (tag1,tag2)
            :type plugin_tags: tuple[str, ...]
            :return: 用户输入的tag是插件的tag的子集则返回True否则返回False
            :rtype: bool
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
            for _tags_and_option in instance_core.getPluginsTagOption():
                if _tagCheck(
                    _user_tags, _tags_and_option[0]
                ):  # _tags_and_option[0] -> plugin_tags: tuple[list]
                    _set_matched_item.add(
                        _tags_and_option[1]
                    )  # _tags_and_option[1] -> plugin_option: str

            self.ui.list_choices_plugin.addItems(_set_matched_item)  # 匹配的添加到选框
            return None

        for i in instance_core.getPluginsOptionToId():  # 选出符合要求的
            if i.find(_search_keyword) == -1:  # 字符串方法，没找到指定子串就-1
                continue
            self.ui.list_choices_plugin.addItem(i)
        return None

    def eventSearchCancel(self) -> None:
        """取消搜索结果，显示全部插件，显示介绍"""
        self.ui.list_choices_plugin.clear()
        self.ui.list_choices_plugin.addItems(
            instance_core.getPluginsOptionToId().keys()
        )
        self.outputIntroduce()  # 输出介绍


class MessageProcessingThread(Thread):
    def __init__(self, mode, message_queue):
        """消息处理线程

        :param mode: 输出模式
        :param message_queue: 消息队列
        """
        super().__init__()
        self.daemon = True
        self.mode = mode
        self.message_queue: Queue = message_queue

    @staticmethod
    def _outputSpentTime(
        time_spent_ns: int = 0, prefix: str = "", suffix: str = ""
    ) -> None:
        """输出计算总结

        :param time_spent_ns: 所花费的时间（单位ns）, 默认为0
        :param prefix: 前缀, 默认为""
        :param suffix: 后缀, 默认为""
        """
        instance_main_win_signal.append_output_box_.emit(
            f"\n\n"
            f"{prefix}"
            f"{time_spent_ns}ns\n"
            f"={time_spent_ns / 10_0000_0000}s\n"
            f"={time_spent_ns / 600_0000_0000}min\n\n"
            f"{suffix}"
        )  # 输出本次计算时间

    def run(self):  # 消息处理
        while True:
            head, body, *data = self.message_queue.get(block=True)
            if head == "OUTPUT":
                instance_main_win_signal.append_output_box.emit(body)
            elif head == "MESSAGE":
                match body:  # noqa: F999
                    case "OutputReachedLimit":
                        instance_main_win_signal.append_output_box.emit(
                            doc.REACHED_OUTPUT_LIMIT_LITERAL
                        )
                    case "CalculationProgramIsRunning":
                        instance_main_win_signal.draw_background.emit()  # 不知道为何使用了打表模式之后会掉背景，干脆重绘一次背景
                        instance_main_win_signal.set_start_button_text.emit(
                            doc.CALCULATION_PROGRAM_IS_RUNNING_LITERAL
                        )
                        instance_main_win_signal.set_start_button_state.emit(
                            False
                        )  # 防止按钮反复触发
                        instance_main_win_signal.clear_output_box.emit()  # 清空输出框
                    case "CalculationProgramIsFinished":
                        time_spent = data[0]

                        match self.mode:  # noqa: F999
                            case "Save":
                                filepath_name = data[1]
                                self._outputSpentTime(
                                    time_spent,
                                    doc.THIS_CALCULATION_AND_SAVING_TOOK_LITERAL,
                                    f"{doc.SAVED_IN_LITERAL} {filepath_name}",
                                )  # 输出本次计算时间
                            case "ReturnFromBuffer":
                                self._outputSpentTime(
                                    time_spent,
                                    doc.THIS_CALCULATION_AND_OUTPUT_TOOK_LITERAL,
                                    doc.OUTPUT_OPTIMIZATION_ENABLED_LITERAL,
                                )  # 输出本次计算时间
                            case "ReturnFromLimitedBuffer":
                                self._outputSpentTime(
                                    time_spent,
                                    doc.THIS_CALCULATION_AND_OUTPUT_TOOK_LITERAL,
                                    doc.OUTPUT_OPTIMIZATION_ENABLED_LITERAL,
                                )  # 输出本次计算时间
                            case "Return":
                                self._outputSpentTime(
                                    time_spent,
                                    doc.THIS_CALCULATION_AND_OUTPUT_TOOK_LITERAL,
                                )  # 输出本次计算时间

                        instance_main_win_signal.set_output_box_cursor.emit(
                            "end"
                        )  # 光标设到文本框尾部
                        instance_main_win_signal.set_start_button_text.emit(
                            doc.CALCULATION_LITERAL
                        )  # 设置按钮字
                        instance_main_win_signal.set_start_button_state.emit(
                            True
                        )  # 启用按钮
                        instance_main_win_signal.draw_background.emit()  # 不知道为何使用了打表模式之后会掉背景，干脆重绘一次背景
                        break
            elif head == "ERROR":
                info = data[0]
                if body == "TypeConversionError":
                    instance_main_win_signal.set_output_box.emit(
                        doc.TYPE_CONVERSION_ERROR_LITERAL % info
                    )
                    break
                elif body == "CalculationError":
                    instance_main_win_signal.set_output_box.emit(
                        doc.PLUGIN_CALCULATION_ERROR_LITERAL % info
                    )
                    break
                else:
                    pass
            else:
                pass

            time.sleep(0.00001)
