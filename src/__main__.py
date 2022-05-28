from builtin_modules import CreateApp

#  from builtin_modules.ui_manager.test_window_effect import testWinApp

# pyside6导入
from PySide6.QtWidgets import QApplication

import sys

#i18n
import gettext
gettext.install('en',localedir=r'.\builtin_modules\locale')

# from builtin_modules.ui import main_window_resource_rc

# 易于打包加几句
# import numba
import hpyculator
# import jpype
import dbm
import argparse

# sys.path.append(os.path.join(os.getcwd(),"bin"))

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 启动一个应用
    instance_app = CreateApp()
    instance_app.run()
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出

    # instance_app = testWinApp()
    # sys.exit(app.exec())  # 避免程序执行到这一行后直接退出

# todo debug qt.gui.imageio: libpng warning: iCCP: known incorrect sRGB profile
# todo 1.可以分享脚本的平台（qq群也不错） 2.Github actions
# todo 3.可以读取文件作为输入
# todo 8.上线网页版
# todo ！！！插件管理窗口
# todo 多套主题
# todo combo的样式
# todo pathlib替换掉os.path
# todo 重写无边框窗体
# todo 把模块里面偷懒的东西修一遍
# todo 学习snipaste的设置界面
# todo 动画问题
# todo 异形窗口
# todo 升级检查
# todo 插件 https://www.osgeo.cn/app/s2711把这个站里面的还原
# todo 默认插件里面放一份没有numba的，带numba作为拓展包提供给用
# todo 埃筛
# todo tag系统

# 命名规范v1.0.0
# 1类：hello_world 变量,函数(def)和方法，文件名(xswl.txt)全部小写，使用下划线连接
# 2类：helloWorld 没有使用小驼峰式命名法，首单词字母小写，后面单词字母大写
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

# 吐槽
# numba jax感觉两个差不多都用不了（但是插件可以用）
#
# 控件名命名规范v1.0.0
# 按钮 button_功能
# 输入输出框 input_/output_功能
# 搜索框 search_功能
# 检查框（一个勾） check_功能
# 列表控件 list_功能
# 下拉选择控件 combo_功能

#python C:\dev\python39\Tools\i18n\pygettext.py -d about_win_manager about_win_manager.py
"""
category
computer_language
depend

author
id
version

给插件加tag

修改开屏
"""
