# 在核心基础上实现的功能

    实现背景图片
    
    实现搜索
    
    实现根据tag搜索

[结构介绍](https://hpyculator.readthedocs.io/zh_CN/latest/project_structure.html#hpyc-pyside-ui)

# 命名规范v1.0.0
  - 1类：hello_world 变量，文件名(xswl.txt)全部小写，使用下划线连接
  - 2类：helloWorld 函数(def)和方法使用小驼峰式命名法，首单词字母小写，后面单词字母大写
  - 3类：HelloWorld 类名(Class)、使用帕斯卡命名规则(大驼峰式命名法,每一个单词的首字母都采用大写字母)。
  - 4类：HELLO_WORLD 常量(NEVER_GIVE_UP)全部大写，使用下划线连接单词

命名特别约定：
  - instance_实例名 作为实例特别标识，属于1类
  - instance_signal_信号名 作为信号实例特别标识，属于1类

# ui控件名命名规范v1.0.0
  - 按钮 button_功能
  - 输入输出框 input_/output_功能
  - 搜索框 search_功能
  - 检查框（一个勾） check_功能
  - 列表控件 list_功能
  - 下拉选择控件 combo_功能

[//]: # (how to locale 从py生成pot文件)

[//]: # ()
[//]: # (- python C:\dev\python310\Tools\locale\pygettext.py -d __init__ __init__.py)

[//]: # (- mgsfmt.py来编译pot文件生成mo文件)

# 会被特殊识别的tag

  - category
    - 一些分类
      - 数学计算 category:Mathematical-calculations
      - 物理计算 category:Physical-computations
      - 换算工具 category:Unit-conversion
      - 其他    category:Other
  - computer-language
    - 一些例子 
      - computer-language:rust
      - computer-language:java
      - computer-language:cpp
  - depend
    - 一些例子
      - depend:jpype
      - depend:numba
      - depend:numpy
  - author
    - 一些例子
      - author:HowieHz 
  - id
    - 一些例子
      - id:test9 
  - version
    - 一些例子
      - version:V1.0.0 
