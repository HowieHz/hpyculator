from builtin_modules import CreateApp
from builtin_modules.ui_manager.test_window_effect import testWindowApplication

# pyside6导入
from PySide6.QtWidgets import QApplication

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 启动一个应用
    instance_app = CreateApp()
    instance_app.run()
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出

    # instance_app = testWindowApplication()
    # sys.exit(app.exec())  # 避免程序执行到这一行后直接退出

# todo 1.可以分享脚本的平台（qq群也不错） 2.Github actions
# todo 3.可以读取文件作为输入 # todo 4.复制到剪贴板
# todo 5.美化 5.背景图 # todo 7.一个按钮打开插件目录
# todo 8.上线网页版
# todo 9.相对快捷方式
# todo ！！！10 os.listdir() https://github.com/CoderWanFeng/python-office/blob/master/office/word.py 学习这里重写插件读取方法
# todo 应该背景实，控件毛玻璃
# todo 窗口阴影，窗口拖动
# todo 介绍信息专门弹出窗口
# todo 窗口动画
# todo 自己写dll
# todo sys增加读取路径，让exe可以单独挑出来
# todo ！！！插件管理窗口
# todo 多套主题
# todo ！！！统一控件命名
# todo combo的样式
# todo label层叠
# todo 项目学习
# """
# 各种量的命名规范
# hello_world 变量,文件名(xswl.txt)全部小写，使用下划线连接
# helloWorld 函数(def)和方法使用小驼峰式命名法，首单词字母小写，后面单词字母大写
# HelloWorld 类名(Class)、使用帕斯卡命名规则(大驼峰式命名法,每一个单词的首字母都采用大写字母)。
# HELLO_WORLD 常量(NEVER_GIVE_UP)全部大写，使用下划线连接单词
# numba jax感觉两个差不多都用不了
# """
