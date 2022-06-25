import gettext
import locale
import os

from . import tags, version

# todo ui-i18n
# how to locale 从py生成pot文件
# 1.
# python C:\dev\python310\Tools\locale\pygettext.py -d __init__ __init__.py
# 记得给pot文件"Content-Type: text/plain; charset=utf-8\n"cp936改utf-8
# 2.拖到翻译软件里面
# 3.
# 创建中文mo文件: python msgfmt.py -o locale/cn/LC_MESSAGES/i18n.mo cn.po
# 创建英文mo文件: python msgfmt.py -o locale/en/LC_MESSAGES/i18n.mo en.po

# domain/localedir	翻译文件名称 / 语言文件根目录
# languages	语言列表 不提供则在环境变量找 ‘LANGUAGE’, ‘LC_ALL’, ‘LC_MESSAGES’, ‘LANG’，找不到返回空列表
# print(os.path.abspath(os.path.join(".", "utils", "locale")))
if locale.getdefaultlocale()[0] == "zh_CN":

    def _(_):
        return _

else:
    try:
        t = gettext.translation(
            domain="i18n", localedir=os.path.join(".", "utils", "locale")
        )
        _ = t.gettext
    except FileNotFoundError:
        t = gettext.translation(
            domain="i18n",
            localedir=os.path.join(".", "utils", "locale"),
            languages=["en"],
        )
        _ = t.gettext
# https://docs.python.org/zh-cn/3/library/gettext.html#internationalizing-your-programs-and-modules

VERSION: str = version.VERSION

ABOUT: str = f"""<h3>HpyCulator {VERSION}</h3>
<p>{_("此为AGPL协议的开源项目")}</p>
<p>{_("项目地址：")}https://github.com/HowieHz/hpyculator</p>
<p>{_("软件文档：")}https:///hpyculator.readthedocs.io/</p>"""

START_SHOW: str = (
    _("高拓展性计算器")
    + f" hpyculator {VERSION}\n"
    + _(
        """作者：HowieHz

使用方法：
    首先选择你要计算的东西
    然后在上方输入框输入你要计算的项数（行数）
    之后在左侧选择计算核心

使用前必读： <-------!!
    0.建议保存到文件，这样不会内屏输出导致卡死
    1.先保存到临时文件再输出可以避免输出频率过高的程序“假死”
    2.“保存”会将结果保存到程序所在目录下 "Output" 文件夹内
    3.设置行(项)数较大请选择保存到文件，运算时间较长，可以通过查看任务管理器确认程序是否假死，不同插件性能（读写性能和运算性能）不同
    4.默认插件保存位置为程序同目录下的 "Plugin" 文件夹内，可通过设置页面打开
    5.输入" :tag "进入tag搜索模式，如" :tag 我是tag1 我是tag2 我是tag3 "，查看可用tag请下拉

交流群694413711，欢迎反馈bug，提出建议

已在github开源：
    地址：https://github.com/HowieHz/hpyculator
    软件文档：https:///hpyculator.readthedocs.io/

hpyculator的名字来历：
    high extensibility calculator base on python
"""
    )
)

# Added － 新增加的功能／接口
# Changed － 功能／接口变更
# Deprecated － 不建议使用的功能／接口，将来会删除
# Removed － 已删除的功能／接口
# Fixed － 解决的问题
# Others － 性能优化和安全性增强等改进

CHANGELOG: str = """\
https://hpyculator.readthedocs.io/
"""

USER_NO_INPUT: str = _(
    """                                                  ↑
                                                  ↑上面的就是输入框了
不输要算什么我咋知道要算啥子嘞     ↑
         → → → → → → → → → →  ↑
         ↑
请在上面的框输入需要被处理的数据

如果忘记了输入格式，只要再次选择运算核心就会显示了（· ω ·）"""
)

USER_NO_CHOOSE: str = _(
    """\n\n
不选要算什么我咋知道要算啥子嘞

请在左侧选择运算核心
          ↓
← ← ←"""
)

TIPS_FOR_USE_LITERAL: str = _("使用提示")
SEARCH_INPUT_BOX_TIPS: str = _("输入字符自动进行搜索\n清空搜索框显示全部插件")
SETTINGS_LITERAL: str = _("设置")
VERSION_LITERAL: str = _("版本")
SAVED_LITERAL: str = _("保存完成")
SAVED_TIPS: str = _("保存完成\n部分设置将在重新启动后生效")
ABOUT_HPYCULATOR_LITERAL: str = _("关于 hpyculator")
INTRODUCTION_LITERAL: str = _("开屏介绍")
CHANGELOG_LITERAL: str = _("更新日志")
ABOUT_LITERAL: str = _("关于")
CHECK_UPDATE_LITERAL: str = _("检查更新")
TYPE_CONVERSION_ERROR_LITERAL: str = _("输入转换发生错误:%s \n\n请检查输入格式")
REACHED_OUTPUT_LIMIT_LITERAL: str = _("\n\n输出上限：检测到输出数据过大，请使用保存到文件防止卡死")
CALCULATION_PROGRAM_IS_RUNNING_LITERAL: str = _("计算程序正在运行中，请耐心等待")
THIS_CALCULATION_AND_SAVING_TOOK_LITERAL: str = _("本次计算+保存花费了")
THIS_CALCULATION_AND_OUTPUT_TOOK_LITERAL: str = _("本次计算+输出花费了")
OUTPUT_OPTIMIZATION_ENABLED_LITERAL: str = _("已启用输出优化")
SAVED_IN_LITERAL: str = _("已保存在")
PLUGIN_CALCULATION_ERROR_LITERAL: str = _("插件运算发生错误：%s \n\n请检查输入格式")
CALCULATION_LITERAL: str = _("计算")
AVAILABLE_TAGS_LITERAL: str = _("可用tag：")
