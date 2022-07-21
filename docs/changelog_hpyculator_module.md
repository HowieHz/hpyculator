hpyculator (module)更新日志
====================================

    Added － 新增加的功能／接口
    Changed － 功能／接口变更
    Deprecated － 不建议使用的功能／接口，将来会删除
    Removed － 已删除的功能／接口
    Fixed － 解决的问题
    Others － 性能优化和安全性增强等改进

1.5.2

    Changed
        hpyculator.hpydecorator.reRunTimes重命名为hpyculator.hpydecorator.getRuntime

1.5.1

    Changed
        hpyculator.hpydecorator.getRuntime 功能更新，添加新参数使得可以直接输出到流

1.5.0

    Changed
        更新sdk，更新文档

1.4.14

    文档更新

1.4.13

    移除了RETURN_LIST和RETURN_LIST_OUTPUT_IN_ONE_LINE
    添加了新函数output_without_line_break
    修改了函数文档

1.4.12.3

    添加了hpyfunc模块，添加了三个函数用于展开列表

1.4.12.2

    文档更新

1.4.12.1
    
    文档更新

1.4.12

    修改目录结构
    弃用toml库改用rtoml库

1.4.11

    迁移到python3.10
    补充说明文档
    使设置文件对象支持链式调用
    简化设置文件api
    
    api修改：
        RETURN_LIST-> RETURN_ITERABLE
        RETURN_LIST_OUTPUT_IN_ONE_LINE-> RETURN_ITERABLE_OUTPUT_IN_ONE_LINE
    
    并将RETURN_LIST和RETURN_LIST_OUTPUT_IN_ONE_LINE标记为将移除

1.4.10
    
    修改了错误的变量名
    添加了设置文件管理模块

1.4.9

    修改变量名，去除不需要的代码

1.4.8
    
    修改说明
    编程风格更新

1.4.6

    编程风格更新

1.4.4.1

    忘记填版本号了

1.4.4

    添加ui信号

1.4.3

    添加ui信号

22w20a-a

    修复逆优化

22w20a

    重新实现
    提升程序效率

22w20
    
    简化api

1.4.0

    api更新

1.3.1

    修改文档风格

1.3.0

    文档完善

1.2.0

    更新api

1.1.0
    
    完全迁移到pyside6

1.0.5
    
    部分迁移到pyside6
    
1.0.3

    准备从wxpython迁移到pyside6

1.0.0

    api初始化