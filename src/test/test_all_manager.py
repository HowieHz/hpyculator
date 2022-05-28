from ..builtin_modules import CreateApp
from hpyculator.hpysignal import instance_main_win_signal
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
        if not setting_file_path:
            raise AssertionError(
                output_dir_path
                == (
                    str(
                        os.path.join(os.getcwd(), "Setting", "hpyculator_setting.toml")
                    ),
                    str(os.path.join(os.getcwd(), "Output")),
                )
            )

        instance_main_window = instance_app.run()[0]
        instance_main_window.eventSaveCheck()
        instance_main_window.eventOutputOptimizationCheck()
        instance_main_window.eventOutputLockMaximumsCheck()
        instance_main_window.eventSearch()
        instance_main_window.eventSearchCancel()

        # global_plugin_option_id_dict = instance_app.pluginCheck(test=True)  # 插件加载
        # assert global_plugin_option_id_dict == \
        #        {"test_pluginV1.0.0 by HowieHz": "test_plugin",
        #         "test_folder_pluginV1.0.0 by HowieHz": "test_folder_plugin"}

    @pytest.mark.run(order=2)
    def test_signal(self):
        print(f"目前运行{self.__class__.__name__}类,test_signal函数")
        instance_main_win_signal.set_output_box.emit("test")
        instance_main_win_signal.clear_output_box.emit()
        instance_main_win_signal.append_output_box.emit("test")
        instance_main_win_signal.set_start_button_state.emit("test")
        instance_main_win_signal.set_output_box_cursor.emit("end")
        instance_main_win_signal.set_start_button_text.emit("test")

    @pytest.mark.run(order=1)
    def test_path(self):
        print(f"目前运行{self.__class__.__name__}类,test_path函数")
        setting_dir_path = str(os.path.join(os.getcwd(), "Setting"))
        output_dir_path = str(os.path.join(os.getcwd(), "Output"))

        if os.path.exists(setting_dir_path) is not True:
            raise AssertionError
        if os.path.exists(output_dir_path) is not True:
            raise AssertionError

    # TODO 计算模块测试 输入是否能得到输入，各种情况的输入，各种输入
    #  插件模块加载测试 检查各项加载是否正常
    #  插件模块调用测试 调用是否正常，返回值是否符合预估
    #  初始化测试 初始化是否能正常调用 路径是否正常调用
    #  ui管理测试 各个事件调用是否正常
    #  业务模拟 走一遍流程
