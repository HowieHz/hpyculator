# 项目结构介绍

[hpyculator](https://github.com/HowieHz/hpyculator)仓库内存放着若干子项目
分别是
- [hpyc_core](https://github.com/HowieHz/hpyculator/tree/main/hpyc_core) 核心SDK
- [hpyc_pyside_ui](https://github.com/HowieHz/hpyculator/tree/main/hpyc_pyside_ui) 基于pyside6的应用程序
- [hpyc_cli](https://github.com/HowieHz/hpyculator/tree/main/hpyc_cli) 尽可能小的实现功能的应用程序

[hpyculatorPackage](https://github.com/HowieHz/hpyculatorPackage)仓库内存放着hpyculator模块 可通过pip获取

```bash
pip install hpyculator
```

## 项目关系

开发插件需要 [hpyculatorPackage](https://github.com/HowieHz/hpyculatorPackage)

开发新ui需要 [hpyc_core](https://github.com/HowieHz/hpyculator/tree/main/hpyc_core)和[hpyculatorPackage](https://github.com/HowieHz/hpyculatorPackage)

开发新SDK需要 [hpyc_core](https://github.com/HowieHz/hpyculator/tree/main/hpyc_core)

## 项目目录结构介绍

### [hpyc_core](https://github.com/HowieHz/hpyculator/tree/main/hpyc_core)

作为包使用

- [calculate](https://github.com/HowieHz/hpyculator/tree/main/hpyc_core/hpyc_core) -> 调用插件计算
- [plugin](https://github.com/HowieHz/hpyculator/tree/main/hpyc_core/plugin) -> 插件管理，插件加载
- [data_structure](https://github.com/HowieHz/hpyculator/tree/main/hpyc_core/data_structure) -> 数据结构
- [settings](https://github.com/HowieHz/hpyculator/tree/main/hpyc_core/settings) -> 管理设置文件

### [hpyculatorPackage](https://github.com/HowieHz/hpyculatorPackage)

作为包使用

- [tests](https://github.com/HowieHz/hpyculatorPackage/tree/main/tests) -> 单元测试
- [hpyculator](https://github.com/HowieHz/hpyculatorPackage/tree/main/hpyculator) -> 存放模块
  - [hpycore.py](https://github.com/HowieHz/hpyculatorPackage/blob/main/hpyculator/hpycore.py) -> 核心
  - [hpydecorator.py](https://github.com/HowieHz/hpyculatorPackage/blob/main/hpyculator/hpydecorator.py) -> 为了方便使用而添加的装饰器
  - [hpyfunc.py](https://github.com/HowieHz/hpyculatorPackage/blob/main/hpyculator/hpyfunc.py) -> 为了方便添加的函数

### [hpyc_pyside_ui](https://github.com/HowieHz/hpyculator/tree/main/hpyc_pyside_ui)
    
`__main__.py` 是入口文件
    
- hpyc_pyside_ui文件夹下

    - [Plugin](https://github.com/HowieHz/hpyculator/tree/main/hpyc_pyside_ui/Plugin) -> 内置插件
    - [background_img](https://github.com/HowieHz/hpyculator/tree/main/hpyc_pyside_ui/background_img) -> 背景图
    - [tests](https://github.com/HowieHz/hpyculator/tree/main/hpyc_pyside_ui/tests) -> 单元测试
    - [use_for_packing](https://github.com/HowieHz/hpyculator/tree/main/hpyc_pyside_ui/use_for_packing) -> 用于打包的工具
    - [utils](https://github.com/HowieHz/hpyculator/tree/main/hpyc_pyside_ui/utils)内是主要代码
       - document -> 常量存放
       - locale -> i18n
       - pyside_frameless_win -> 无边框ui
       - ui -> ui
       - ui_manager -> 管理ui, 程序逻辑

### [hpyc_cli](https://github.com/HowieHz/hpyculator/tree/main/hpyc_cli)
    
`__main__.py` 是入口文件
