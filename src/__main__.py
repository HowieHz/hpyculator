from builtin_modules import CreateApp

# pyside6导入
from PySide6.QtWidgets import QApplication

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 启动一个应用
    instance_app = CreateApp()
    instance_app.run()
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出

# todo 8.可以分享脚本的平台（qq群也不错） 17.Github actions
# todo 11.可以读取文件作为输入 # todo 16.复制到剪贴板
# todo 15.美化 1.背景图 # todo 17.一个按钮打开插件目录
# todo 10.上线网页版
# todo 11.相对快捷方式

# """
# 各种量的命名规范
# hello_world 变量,文件名(xswl.txt)全部小写，使用下划线连接
# helloWorld 函数(def)和方法使用小驼峰式命名法，首单词字母小写，后面单词字母大写
# HelloWorld 类名(Class)、使用帕斯卡命名规则(大驼峰式命名法,每一个单词的首字母都采用大写字母)。
# HELLO_WORLD 常量(NEVER_GIVE_UP)全部大写，使用下划线连接单词
# numba jax感觉两个差不多都用不了
# """
