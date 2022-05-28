# coding:utf-8
import os
from ctypes import POINTER, cast

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget

from ctypes.wintypes import MSG
import win32api
import win32gui
from win32.lib import win32con
from ..windoweffect import MINMAXINFO, NCCALCSIZE_PARAMS, WindowEffect

# if os.name == 'nt':
#     from ctypes.wintypes import MSG
#     import win32api, win32gui
#     from win32.lib import win32con
#     from ..windoweffect import MINMAXINFO, NCCALCSIZE_PARAMS, WindowEffect
# else:
#     # from utils.linux_utils import LinuxMoveResize
#     pass  # sip没有找到在pyside6下对应的模块，故砍去


class FramelessWindowBase(QWidget):
    # class FramelessWindowBase(QMainWindow):
    """Frameless window"""

    BORDER_WIDTH = 5

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.titleBar = TitleBar(self)
        # self.titleBar.raise_()
        self.resize(500, 500)

    def _isWindowMaximized(self, hWnd):
        """Determine whether the window is maximized"""
        return self.isMaximized()


class WindowsFramelessWindow(FramelessWindowBase):
    """Frameless window for Windows system"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__monitorInfo = None
        self.windowEffect = WindowEffect()

        # remove window border
        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowSystemMenuHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )

        # add DWM shadow and window animation
        self.windowEffect.addWindowAnimation(self.winId())
        self.windowEffect.addShadowEffect(self.winId())

        # solve issue #5
        self.windowHandle().screenChanged.connect(self.__onScreenChanged)

    def nativeEvent(self, eventType, message):
        """Handle the Windows message"""
        msg = MSG.from_address(message.__int__())
        if msg.message == win32con.WM_NCHITTEST:
            pos = QCursor.pos()
            xPos = pos.x() - self.x()
            yPos = pos.y() - self.y()
            w, h = self.width(), self.height()
            lx = xPos < self.BORDER_WIDTH
            rx = xPos > w - self.BORDER_WIDTH
            ty = yPos < self.BORDER_WIDTH
            by = yPos > h - self.BORDER_WIDTH
            if lx and ty:
                return True, win32con.HTTOPLEFT
            if rx and by:
                return True, win32con.HTBOTTOMRIGHT
            if rx and ty:
                return True, win32con.HTTOPRIGHT
            if lx and by:
                return True, win32con.HTBOTTOMLEFT
            if ty:
                return True, win32con.HTTOP
            if by:
                return True, win32con.HTBOTTOM
            if lx:
                return True, win32con.HTLEFT
            if rx:
                return True, win32con.HTRIGHT
        elif msg.message == win32con.WM_NCCALCSIZE:
            if self._isWindowMaximized(msg.hWnd):
                self.__monitorNCCALCSIZE(msg)
            return True, 0
        elif msg.message == win32con.WM_GETMINMAXINFO and self._isWindowMaximized(
            msg.hWnd
        ):
            window_rect = win32gui.GetWindowRect(msg.hWnd)
            if not window_rect:
                return False, 0

            # get the monitor handle
            monitor = win32api.MonitorFromRect(window_rect)
            if not monitor:
                return False, 0

            # get the monitor info
            __monitorInfo = win32api.GetMonitorInfo(monitor)
            monitor_rect = __monitorInfo["Monitor"]
            work_area = __monitorInfo["Work"]

            # convert lParam to MINMAXINFO pointer
            info = cast(msg.lParam, POINTER(MINMAXINFO)).contents

            # adjust the size of window
            info.ptMaxSize.x = work_area[2] - work_area[0]
            info.ptMaxSize.y = work_area[3] - work_area[1]
            info.ptMaxTrackSize.x = info.ptMaxSize.x
            info.ptMaxTrackSize.y = info.ptMaxSize.y

            # modify the upper left coordinate
            info.ptMaxPosition.x = abs(window_rect[0] - monitor_rect[0])
            info.ptMaxPosition.y = abs(window_rect[1] - monitor_rect[1])
            return True, 1

        return QWidget.nativeEvent(self, eventType, message)

    def _isWindowMaximized(self, hWnd) -> bool:
        # GetWindowPlacement() returns the display state of the window and the restored,
        # maximized and minimized window position. The return value is tuple
        windowPlacement = win32gui.GetWindowPlacement(hWnd)
        if not windowPlacement:
            return False

        return windowPlacement[1] == win32con.SW_MAXIMIZE

    def __monitorNCCALCSIZE(self, msg):
        """Adjust the size of window"""
        monitor = win32api.MonitorFromWindow(msg.hWnd)

        # If the display information is not saved, return directly
        if monitor is None and not self.__monitorInfo:
            return
        if monitor is not None:
            self.__monitorInfo = win32api.GetMonitorInfo(monitor)

        # adjust the size of window
        params = cast(msg.lParam, POINTER(NCCALCSIZE_PARAMS)).contents
        params.rgrc[0].left = self.__monitorInfo["Work"][0]
        params.rgrc[0].top = self.__monitorInfo["Work"][1]
        params.rgrc[0].right = self.__monitorInfo["Work"][2]
        params.rgrc[0].bottom = self.__monitorInfo["Work"][3]

    def __onScreenChanged(self):
        hWnd = int(self.windowHandle().winId())
        win32gui.SetWindowPos(
            hWnd,
            None,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED,
        )


FramelessWindow = WindowsFramelessWindow
