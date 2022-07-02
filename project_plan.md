# 开发计划

## 总体
- 创建cli应用程序hpyc_cli
- 可以分享插件的平台

## hpyc_core
- 添加ws作为核心通讯方法
- api相关开发无需导入hpyculator，只用导入hpyc_core
- 完成hpyc_core模块的test

## hpyc_pyside_ui
- ui
  - 插件管理窗口
  - 多套主题，并且重写combo样式
  - 重写无边框窗体
  - 重写设置页面
  - 框体动画
  - 槽函数外移，在程序里面连接易于管理
- 完成单元测试
- 允许文件输入
- 去除warning qt.gui.imageio: libpng warning: iCCP: known incorrect sRGB profile

## 更新方向

- 0.就是作为一个可以自己编写算法的计算机，因为网上在线效率太低，打表也不方便，自己写想调rust，cpp，java都随意
- 2.快速启动器(如wox)的插件
- 3.web app
- 4.轻量ui
- 5.完备API
- 6.快速将cli命令行应用转换为带ui的软件