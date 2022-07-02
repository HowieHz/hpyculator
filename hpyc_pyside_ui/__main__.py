"""入口文件"""
# 易于打包加几句
import argparse
import dbm
import sys

from PySide6.QtWidgets import QApplication

from utils import CreateApp

# pyside6导入
# from utils.ui import main_window_resource_rc
# sys.path.append(os.path.join(os.getcwd(),"bin"))

if __name__ == "__main__":
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)  # 启动一个应用
    instance_app = CreateApp()
    list_apps = instance_app.run()
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出
