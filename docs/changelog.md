更新日志
====================================

    Added － 新增加的功能／接口
    Changed － 功能／接口变更
    Deprecated － 不建议使用的功能／接口，将来会删除
    Removed － 已删除的功能／接口
    Fixed － 解决的问题
    Others － 性能优化和安全性增强等改进

v1.7.2(草稿)
    None 

v1.7.1

    Added
        文档修改，补充
        添加hpyc_cli v1.0.0
    Changed
        修改一些插件的处理算法
    Fixed
        hpyc_pyside_ui达到输出上限不能正常停止消息监听线程的问题
    Others
        对模块名称进行了区分，防止意外的导入操作

v1.7.0
    
    Added
        分离核心为hpyc_core
        分离基于pyside6的ui为hpyc_pyside_ui
        完成文档关于API的说明
        hpyc_pyside_ui新增打表模式，每次输出后添加一个","
        新增common_factor_hz，pluperfect_digital_invariant_hz插件
    Changed
        多处文档更新
        插件更新
    Removed
        移除了output_without_line_break
        移除了hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE
    Others
        代码性能优化（尽可能多的使用元组）
        结构优化，并补充注释，类型表示
        引入mypy进行静态类型检查

v1.6.3

    Added
        添加了output_without_line_break函数
    Fixed
        hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE无法正常工作的错误
        test9_hz不正常工作的错误（表现为输出错误）
        output文档描述错误
        插件可能导致内存占用极大的特性（修复了文件缓冲不可控的问题）
        修复了插件缓冲和实际缓冲不符的问题
    Removed
        hpyc.RETURN_LIST
        hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE
    Others
        代码性能优化，结构优化，并补充注释

v1.6.2

    Added
        在搜索tag的时候会显示可用tag
    Changed
        常量名修改:
            hpyc.RETURN_LIST -> hpyc.RETURN_ITERABLE
            hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE -> hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE
    Fixed
        翻译不正确显示的问题
        退出残留问题
    Deprecated
        hpyc.RETURN_LIST
        hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE
    Others
        文字归档到一个文件，易于翻译和管理
        迁移到3.10
        修改写法(if elif -> match case)
        优化嵌套结构

20220611
v1.6.1

    Added
        添加多种设置文件格式支持（json，toml，yaml）
    Changed
        默认设置文件格式从toml更改为json
    Removed
        移除软件内置的更新日志
        移除输入框输入update_log显示更新日志
    Others
        修改文档描述
        修改计算后输出时间统计格式和使用函数

20220529
v1.6.0-fix.1

    Fixed
        控件名错误的bug 
    Deprecated
        软件内置的更新日志

20220528
v1.6.0

    Added
        i18n -> en语言支持
        tag系统，可以使用tag进行搜索了
        新增插件若干
        可切换背景图片
        插件元数据tag项
        可切换是否自动换行
    Changed
        插件元数据option_name -> option
        插件元数据author现支持多作者
        文档示例更新
    Removed
        移除无用插件
        插件元数据use_quantifier项
    Fixed
        修复插件无法正常运行的bug
    Others
        代码风格修订

v1.5.0

    Changed
        重绘ui

20220430-20220505
1.4.0

    Changed
        修改了api和插件事件
    Removed
        移除test模式
    Others
        分离插件读取部分
        性能优化（干掉exec，解决命名空间污染）
        规范文档，规范版本，编程风格修订
        菜单栏字体大小调整
        调整搜索框大小
        文档更新(函数说明，示例调整，api，插件示例）

20220429
v1.3.3

    Others
        debug

20220429
v1.3.2

    Added
        添加了设置窗口
        修改保存位置的选项回归
    Fixed
        修复搜索框不可用的问题
    Others
        完成从wxpython移植到pyside6

20220416
v1.3.1

    Fixed
        debug

20220414
v1.3.0

    Others
        部分移植到pyside6上

20220412
v1.2.7

    Others
        程序优化
        主程序优化
        内置插件优化

20220411
V1.2.6

    Added
        增加了输出上限的选项
    Fixed
        修复了内置插件不能正常工作的问题
        修复遗留问题
    Others
        优化了输出优化的模式

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

    多了一个可以切换计算核心的选项,
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
    
    a1.0 最初的经典(20220505注，最初的大粪)
