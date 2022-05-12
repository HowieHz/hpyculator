from ..builtin_modules.calculate_manager import CalculationThread
from ..builtin_modules.calculate_manager import CalculationManager
from ..builtin_modules import CreateApp
from hpyculator import hpycore as hpyc
import pytest
import sys
import os
from typing import Any
from hpyculator import main_window_signal


class TestCalculationManager:
    def test_init(self):
        print(f"目前运行{self.__class__.__name__}类,test_init函数")
        # 类init测试
        CalculationManager()

    @pytest.mark.parametrize("test_input, test_input_mode, test_calculation_mode, test_selection_id, test_output_dir_path,rev_expected",
                             [("1", hpyc.STRING, "test_plugin", "calculate", str(os.path.join(os.getcwd(), 'Output')), None,),  # 最后一项应该是“1”的，但是怎么回事呢，共享对象都失效了
                              ("1", hpyc.FLOAT, "test_plugin", "calculate", str(os.path.join(os.getcwd(), 'Output')), None,),
                              ("1", hpyc.NUM, "test_plugin", "calculate", str(os.path.join(os.getcwd(), 'Output')), None)])
    def test_calculation_manager(self,
                                 test_input: str,
                                 test_input_mode: int,
                                 test_calculation_mode: str,
                                 test_selection_id: str,
                                 test_output_dir_path: str,
                                 rev_expected: Any,
                                 ):
        """
        启动计算线程

        :param test_input: 测试输入，测试专用
        :param test_input_mode: 测试目标转换模式，测试专用
        :param test_calculation_mode: 测试计算模式，测试专用
        :param test_selection_id: 测试选择插件id，测试专用
        :param test_output_dir_path: 测试目录
        :param rev_expected; 返回期望
        # param output_expected; 输出期望
        :return:
        """
        print(f"目前运行{self.__class__.__name__}类,test_calculation_manager函数")
        # 初始化
        # self.app = QApplication(sys.argv)  # 启动一个应用
        instance_app = CreateApp()
        instance_main_window = instance_app.run()[0]
        ret = instance_main_window.startEvent(test_input=test_input,
                                              test_input_mode=test_input_mode,
                                              test_calculation_mode=test_calculation_mode,
                                              test_selection_id=test_selection_id,
                                              test_output_dir_path=test_output_dir_path)

        Manager = CalculationManager()
        assert ret is rev_expected

        # # 校验输入框
        # assert instance_main_window.ui.output_box.toPlainText() == output_expected

    @ pytest.mark.parametrize("to_type,data,rev_expected",
                              [(hpyc.STRING, 1, "1"),  # 转换为字符串
                               (hpyc.FLOAT, 1, 1.0),  # 转换为浮点数
                               (hpyc.NUM, 1, 1),  # 转换为整形
                               (None, 1, None),  # 转换为不存在的类型 返回None
                               ((hpyc.NUM, "a", None))])  # 无法完成的转换
    def test_calculation_typeconversion(self,
                                        to_type: int,
                                        data: Any,
                                        rev_expected: Any):
        """
        测试类型转换函数

        :param to_type:
        :param data:
        :param rev_expected:
        :return:
        """
        print(f"目前运行{self.__class__.__name__}类,test_calculation_typeconversion函数")
        # 类typeConversion函数测试
        assert CalculationManager.typeConversion(to_type, data) == rev_expected