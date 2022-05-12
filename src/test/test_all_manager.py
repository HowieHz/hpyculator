from ..builtin_modules import CreateApp
from hpyculator.signal import main_window_signal
import sys
import os
import pytest

# pyside6导入
from PySide6.QtWidgets import QApplication


class TestAllManager:
    @pytest.mark.run(order=1)
    def test_init(self):
        print(f"目前运行{self.__class__.__name__}类,test_init函数")
        self.app = QApplication(sys.argv)  # 启动一个应用
        # 路径返回测试
        instance_app = CreateApp()

        setting_file_path, output_dir_path = instance_app.pathCheck()
        assert setting_file_path, output_dir_path == (
            str(os.path.join(os.getcwd(), "Setting", "hpyculator_setting")),
            str(os.path.join(os.getcwd(), "Output")),
        )  # 返回检查

        instance_main_window = instance_app.run()[0]
        instance_main_window.saveCheckEvent()
        instance_main_window.outputOptimizationCheckEvent()
        instance_main_window.outputLockMaximumsCheckEvent()
        instance_main_window.searchText()
        instance_main_window.searchCancel()

        # global_plugin_option_id_dict = instance_app.pluginCheck(test=True)  # 插件加载
        # assert global_plugin_option_id_dict == \
        #        {"test_pluginV1.0.0 by HowieHz": "test_plugin",
        #         "test_folder_pluginV1.0.0 by HowieHz": "test_folder_plugin"}

    @pytest.mark.run(order=2)
    def test_signal(self):
        print(f"目前运行{self.__class__.__name__}类,test_signal函数")
        main_window_signal.setOutPutBox.emit("test")
        main_window_signal.clearOutPutBox.emit()
        main_window_signal.appendOutPutBox.emit("test")
        main_window_signal.setStartButtonState.emit("test")
        main_window_signal.setOutPutBoxCursor.emit("end")
        main_window_signal.setStartButtonText.emit("test")

    @pytest.mark.run(order=1)
    def test_path(self):
        print(f"目前运行{self.__class__.__name__}类,test_path函数")
        setting_dir_path = str(os.path.join(os.getcwd(), "Setting"))
        output_dir_path = str(os.path.join(os.getcwd(), "Output"))

        assert os.path.exists(setting_dir_path) is True  # 设置文件目录路径创建测试
        assert os.path.exists(output_dir_path) is True  # 输出目录路径创建测试

    @pytest.mark.run(order=2)
    def test_log(self):
        print(f"目前运行{self.__class__.__name__}类,test_log函数")
        instance_app = CreateApp()
        setting_file_path = str(
            os.path.join(os.getcwd(), "Setting", "hpyculator_setting")
        )
        log_dir_path = str(os.path.join(os.getcwd(), "Log"))

        instance_app.logCheck(setting_file_path)  # 日志检查

        assert os.path.exists(log_dir_path) is True  # 日志目录路径创建测试

    # TODO 计算模块测试 输入是否能得到输入，各种情况的输入，各种输入
    #  log模块测试 返回值，是否创建了路径，是否生成了文件，文件写入是否正常
    #  插件模块加载测试 检查各项加载是否正常
    #  插件模块调用测试 调用是否正常，返回值是否符合预估
    #  初始化测试 初始化是否能正常调用 路径是否正常调用
    #  ui管理测试 各个事件调用是否正常
    #  业务模拟 走一遍流程
