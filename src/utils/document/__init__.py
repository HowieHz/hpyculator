from . import tags
from . import version
import gettext
import os

# i18n
langs = ["en"]
for lang in langs:
    gettext.install(lang, localedir=os.path.join(".", "utils", "locale"))

VERSION = version.VERSION

ABOUT = f"<h3>HpyCulator {VERSION}</h3>"
"<p>" + _("此为AGPL协议的开源项目") + "</p>"
"<p>" + _("项目地址：") + "https://github.com/HowieHz/hpyculator</p>"
"<p>" + _("软件文档：") + "https:///hpyculator.readthedocs.io/</p>"

START_SHOW = (
    _("高拓展性计算器")
    + f" hpyculator {VERSION}\n"
    + _(
        """作者：HowieHz

使用方法：
    首先选择你要计算的东西
    然后在上方输入框输入你要计算的项数（行数）
    之后在左侧选择计算核心

使用前必读：
    0.建议保存到文件，这样不会内屏输出导致卡死，再不济也开启输出优化
    1.“保存”会将结果保存到程序所在目录下 "Output" 文件夹内
    2.设置行(项)数较大请选择保存到文件，运算时间较长，可以通过查看任务管理器确认程序是否假死，不同插件性能（读写性能和运算性能）不同
    3.默认插件保存位置为程序同目录下的 "Plugin" 文件夹内，可通过设置页面打开
    4.输入" :tag "进入tag搜索模式，如" :tag 我是tag1 我是tag2 我是tag3 "，查看可用tag请下拉

交流群694413711，欢迎反馈bug，提出建议

已在github开源：
    地址：https://github.com/HowieHz/hpyculator
    软件文档：https:///hpyculator.readthedocs.io/

hpyculator的名字来历：
    high extensibility calculator base on python

可用tag："""
    )
)

# Added － 新增加的功能／接口
# Changed － 功能／接口变更
# Deprecated － 不建议使用的功能／接口，将来会删除
# Removed － 已删除的功能／接口
# Fixed － 解决的问题
# Others － 性能优化和安全性增强等改进

CHANGELOG = """\
https://hpyculator.readthedocs.io/
"""

