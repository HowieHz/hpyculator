from builtin_modules import CreateApp
from builtin_modules.calculate_manager import CalculationThread
from builtin_modules.log_manager import LogManager
from builtin_modules.ui_manager import MainWindowApplication
from builtin_modules.plugin_manager import PluginManager
import sys
import os

# pyside6导入
from PySide6.QtWidgets import QApplication


class TestAllManager:
    def test_start(self):
        # app = QApplication(sys.argv)
        # sys.exit(instance_app.run().exec())  # 避免程序执行到这一行后直接退出
        # 路径返回测试
        instance_app = CreateApp(test=True)

        setting_file_path, output_dir_path = instance_app.pathCheck()
        #返回检查
        assert setting_file_path, output_dir_path == \
                                  (str(os.path.join(os.getcwd(), 'Setting', 'hpyculator_setting')),
                                   str(os.path.join(os.getcwd(), 'Output')))

        global_plugin_option_id_dict = instance_app.pluginCheck(test=True)  # 插件加载
        assert global_plugin_option_id_dict == \
               {"test_pluginV1.0.0 by HowieHz": "test_plugin",
                "test_folder_pluginV1.0.0 by HowieHz": "test_folder_plugin"}

    def test_path(self):
        setting_dir_path = str(os.path.join(os.getcwd(), 'Setting'))
        output_dir_path = str(os.path.join(os.getcwd(), 'Output'))

        assert os.path.exists(setting_dir_path) is True  # 设置文件目录路径创建测试
        assert os.path.exists(output_dir_path) is True  # 输出目录路径创建测试

    def test_log(self):
        instance_app = CreateApp(test=True)
        setting_file_path = str(os.path.join(os.getcwd(), 'Setting', 'hpyculator_setting'))
        log_dir_path = str(os.path.join(os.getcwd(), 'Log'))

        instance_app.logCheck(setting_file_path)  # 日志检查

        assert os.path.exists(log_dir_path) is True  # 日志目录路径创建测试