"""入口文件"""
# 易于打包加几句
import argparse
import dbm
import sys

from PySide6.QtWidgets import QApplication

from utils import CreateApp

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 启动一个应用
    instance_app = CreateApp()
    list_apps = instance_app.run()
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出
