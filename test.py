import importlib
import pprint
# 绝对导入
a = importlib.import_module('Plugin.A_Plus_B_import_Java.__init__')
a.main("1,2",3)     #(a.py中有函数show())
