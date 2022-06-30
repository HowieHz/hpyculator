from PySide6.QtCore import QObject, Signal


class MainWinSignal(QObject):
    """主窗口 自定义信号"""

    set_output_box: Signal = Signal(str)
    clear_output_box: Signal = Signal()
    append_output_box: Signal = Signal(str)  # 输出前会添加换行符
    insert_output_box: Signal = Signal(str)  # 输出前不会添加换行符
    append_output_box_: Signal = Signal(str)  # 输出前会添加换行符 不会受到“打表模式”的影响
    insert_output_box_: Signal = Signal(str)  # 输出前不会添加换行符 不会受到“打表模式”的影响
    get_output_box: Signal = Signal()

    set_start_button_text: Signal = Signal(str)
    set_start_button_state: Signal = Signal(bool)

    set_output_box_cursor: Signal = Signal(str)

    draw_background: Signal = Signal()


instance_main_win_signal = MainWinSignal()  # 单例模式
