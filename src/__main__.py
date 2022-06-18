"""入口文件"""
# 易于打包加几句
import argparse
import dbm
import hpyculator
import sys

# from PySide6 import QtWidgets, QtCore
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
    mainwin = instance_app.run()
    mainwin.show()
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出

# todo debug qt.gui.imageio: libpng warning: iCCP: known incorrect sRGB profile
# todo 1.可以分享脚本的平台（qq群也不错） 2.Github actions
# todo 3.可以读取文件作为输入
# todo 8.上线网页版
# todo 插件管理窗口
# todo 多套主题
# todo combo的样式
# todo 重写无边框窗体
# todo 学习snipaste的设置界面
# todo 动画
# todo 缓存结果模式 不是@cache
# todo 把槽函数外移，在程序里面connect
# todo 软件退出有残留

# 命名规范v1.0.0
# 1类：hello_world 变量，文件名(xswl.txt)全部小写，使用下划线连接
# 2类：helloWorld 函数(def)和方法使用小驼峰式命名法，首单词字母小写，后面单词字母大写
# 3类：HelloWorld 类名(Class)、使用帕斯卡命名规则(大驼峰式命名法,每一个单词的首字母都采用大写字母)。
# 4类：HELLO_WORLD 常量(NEVER_GIVE_UP)全部大写，使用下划线连接单词
# 命名特别约定：
# instance_实例名 作为实例特别标识，属于1类
# instance_signal_信号名 作为信号实例特别标识，属于1类
# event_ 作为槽命名特别标识，属于1类
# global_ 全局变量名，属于1类
# GLOBAL_ 全局常量名，属于4类
# local_ 局部变量名，属于1类
# list_ 列表特别标识
# dict_ 字典特别标识

# 控件名命名规范v1.0.0
# 按钮 button_功能
# 输入输出框 input_/output_功能
# 搜索框 search_功能
# 检查框（一个勾） check_功能
# 列表控件 list_功能
# 下拉选择控件 combo_功能

# how to locale 从py生成pot文件
# python C:\dev\python310\Tools\locale\pygettext.py -d __init__ __init__.py
# mgsfmt.py来编译pot文件生成mo文件

# 配置文件操作指南
# 初始化： a+open  然后初始化单项
# 修改： load 修改 w+open dump
# 初始化第二种： load 修改（因为是字典，不存在的项会自动初始化） w+open dump

# category
# computer_language
# depend
#
# author
# id
# version
#
# 给插件加tag
# 数学计算Mathematical calculations
# 物理计算Physical computations
# 换算工具Unit conversion
# 还有其他Other
# category:Mathematical calculations
