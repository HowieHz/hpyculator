from PySide6.QtCore import Signal,QObject

class MainWindowSignal(QObject):
    setOutPutBox = Signal(str)
    clearOutPutBox = Signal()
    appendOutPutBox = Signal(str)

main_window_signal = MainWindowSignal()