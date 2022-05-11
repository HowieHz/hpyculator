from builtin_modules import CreateApp

# pyside6导入
from PySide6.QtWidgets import QApplication

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 启动一个应用
    instance_app = CreateApp()
    instance_app.run()
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出
