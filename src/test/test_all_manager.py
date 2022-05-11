from ..builtin_modules import CreateApp
from ..builtin_modules.calculate_manager import CalculationThread
from ..builtin_modules.log_manager import LogManager
from ..builtin_modules.ui_manager import MainWindowApplication
from ..builtin_modules.plugin_manager import PluginManager
from hpyculator import main_window_signal
import sys
import os
import pytest

# pyside6导入
from PySide6.QtWidgets import QApplication


class TestAllManager:
    @pytest.mark.run(order=1)
    def test_init(self):
        # app = QApplication(sys.argv)
        # sys.exit(instance_app.run().exec())  # 避免程序执行到这一行后直接退出
        # 路径返回测试
        instance_app = CreateApp(test=True)
        self.app = QApplication(sys.argv)  # 启动一个应用

        setting_file_path, output_dir_path = instance_app.pathCheck()
        assert setting_file_path, output_dir_path == \
                                  (str(os.path.join(os.getcwd(), 'Setting', 'hpyculator_setting')),
                                   str(os.path.join(os.getcwd(), 'Output')))  # 返回检查

        instance_main_window = instance_app.run()
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
        main_window_signal.setOutPutBox.emit("test")
        main_window_signal.clearOutPutBox.emit()
        main_window_signal.appendOutPutBox.emit("test")
        main_window_signal.setStartButtonState.emit("test")
        main_window_signal.setOutPutBoxCursor.emit("end")
        main_window_signal.setStartButtonText.emit("test")

    @pytest.mark.run(order=1)
    def test_path(self):
        setting_dir_path = str(os.path.join(os.getcwd(), 'Setting'))
        output_dir_path = str(os.path.join(os.getcwd(), 'Output'))

        assert os.path.exists(setting_dir_path) is True  # 设置文件目录路径创建测试
        assert os.path.exists(output_dir_path) is True  # 输出目录路径创建测试

    @pytest.mark.run(order=2)
    def test_log(self):
        instance_app = CreateApp(test=True)
        setting_file_path = str(os.path.join(os.getcwd(), 'Setting', 'hpyculator_setting'))
        log_dir_path = str(os.path.join(os.getcwd(), 'Log'))

        instance_app.logCheck(setting_file_path)  # 日志检查

        assert os.path.exists(log_dir_path) is True  # 日志目录路径创建测试
