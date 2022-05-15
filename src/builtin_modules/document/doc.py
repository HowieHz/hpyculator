from .version import VERSION  # 版本号导入

TODO = """
更新展望(咕咕咕):
clear"""

START_SHOW = f"""
高拓展性计算器 hpyculator {VERSION}
作者：HowieHz

使用方法：
    首先选择你要计算的东西
    然后在上方输入框输入你要计算的项数（行数）
    之后在左侧选择计算核心


使用前必读:
    0.建议保存到文件，这样不会内屏输出导致卡死，再不济也开启输出优化
    1.“保存”会将结果保存到程序所在目录下 "Output" 文件夹内
    2.设置行(项)数较大请选择保存到文件，算的不久，但是导出很久，可以看看任务管理器，不同插件性能（读写速度和）不同，要看插件作者的水平
    3.默认插件保存位置为程序同目录下的 "Plugin" 文件夹内

交流群694413711，欢迎反馈bug，提出建议

已在github开源
    地址：https://github.com/HowieHz/hpyculator
    软件文档：https:///hpyculator.readthedocs.io/

hpyculator的名字来历：
    high extensibility calculator base on python






悄悄说:在输入栏输入update_log之后点击运算就可以看更新日志了
"""

UPDATE_LOG = """更新日志:
20220430-20220512
1.4.0
程序：
模块化，耦合度降至低水平（分离插件读取部分，分离计算线程，分离日志管理，将自定义信号文件移至hpyculator模块内）
性能优化（干掉exec，解决命名空间污染）
功能调整（移除test模式）
api更新，事件更新（简化了api和插件事件）
细节更新（规范文档，规范版本号，编程风格更新）
修复了若干bug

ui：
菜单栏字体调整
调整搜索框

文档：
文档更新(函数说明，示例调整，api，插件事件，插件示例）

20220429
v1.3.3
debug

20220429
v1.3.2
添加了设置窗口
修复搜索框不可用的问题(完成移植工作)
修改保存位置的选项回归(完成移植工作)

宣告完成从wxpython移植到pyside6

20220416
v1.3.1
debug

20220414
v1.3.0
移植到pyside6上

20220412
v1.2.7
优化，更多的优化
主程序优化
插件优化

20220411
V1.2.6
增加了输出上限的选项
优化了输出优化的模式
修复了内置插件
修复遗留问题

20220409
V1.2.5
修复了遗留问题
完善了输出优化模式
细节修复
程序优化

20220408
V1.2.4
hpyculator模块上传了！现可通过pip下载
重写了内置插件
修改了gui,可自选保存位置

20220408
V1.2.3
修复了多线程的问题
修改了菜单栏

20220407
V1.2.2
修复了内置插件无法正常工作的问题
添加了更新检查按钮(打开浏览器跳转到https://github.com/HowieHz/hpyculator/releases)

20220407
V1.2.1
修复了无插件打不开的bug
修复了退出后还残留后台程序的bug

20220407
V1.2.0
修改gui
增加了搜索框
添加了测试选项，勾选之后程序就会使用test模式

20220405
V1.1.0
增加了对文件插件的支持
增加了很多提示，防止插件卡死程序

V1.0.0
改名为
皓式可编程计算器hpyculator
2022年1月19日添加了规范文档
2022年1月18-19日，重构了程序（从流水线+函数群变成了面向对象的编程）
2022年3月29再次捡起项目，
2022年3月31写完，实现了规范文档，但是掉进了打包的坑，还好第二天爬出来了
2022年4月1日第一个内测版
2022年4月1日添加了多线程支持，添加了更多用户友好类提示，修复了若干个bug，添加了一种输出模式
2022年4月2日修改了内置插件的性能，添加了新的输出模式，并提供了4个函数便于插件作者创作

趣闻:
2022年1月16日时想用PyQt（5/6）代替wxpython（哈哈wxpython不支持python3.10，其他版本又删掉了，被迫的）
由于PyQt（5/6）-tool用pip不能正确安装和考虑到学习成本，所以干脆卸载py310，改回py39（白配置一遍^_^）



来自 各类数组计算程序
2021年6月27日
V1.2
选择保存文件时不再输出
平均数，众数，中位数，方差，标准差的计算可以输入负数和小数了
为了节省体积，换了个图标

V1.1
添加了平均数，众数，中位数，方差，标准差的计算

2020年11月14日
V1.0
多了一个可以切换计算核心的选项
更加模块化，内置模块有杨辉三角计算和斐波那契数列计算
(作者电脑i5-5代低压u，4g内存。无聊算114514行，算了半小时，原本要关了，看任务管理器还在运行，就去睡了一会，起来看到一个1338412kb的文件（约1.28G），哈哈哈，请勿模仿（除非很闲）)



来自杨辉三角计算程序v3.4.2
a3.4.2 修复不能读取配置的问题，优化代码体积
2020年11月8日a3.4.1 创建了两个文件夹专门用来储存设置和输出,扩大1.5倍了默认生成的窗口
2020年11月8日a3.4.0 在输入栏输入update_log点击运算就可以看更新日志了!菜单栏它来了
2020年11月7日a3.3.4 修改保存名的时间
a3.3.3b 走向规范化
2020年11月7日a3.3.3a 遗弃的分支，消除了保存时间
2020年10月17日a3.3.2 删除多余代码优化体积
2020年10月17日a3.3.1 生成在gui里的不再是一行了,砍掉了可以修改算法的选项,删除多余代码优化体积
a3.3.0 被遗忘的版本号
a3.2 改进了算法，增快了运行速度,增加了可以修改算法的选项
2020年10月10日a3.1 将原来的运行并保存按钮修改为是否保存的选项
a3.0 有GUI了!生成的文件不再是一行了

a2.0 添加了保存文件到本目录，添加了计算计时器,防止因为错误信息造成的闪退,节省打包体积

a1.0 最初的经典"""
