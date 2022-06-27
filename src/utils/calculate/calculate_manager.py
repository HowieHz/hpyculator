import traceback
from types import ModuleType

import hpyculator as hpyc
from hpyculator.hpysignal import instance_main_win_signal

from ..data_structure import MetadataDict
from .. import document as doc
from ..plugin import instance_plugin_manager
from .calculation_thread import CalculationThread

# TODO 用了多进程之后main_win_signal的实例化效果消失
# TODO 将插件加载之类的和计算写在一起就可以了


class CalculationManager:
    def __init__(self):
        """计算管理"""

    def start(
        self,
        inputbox_data: str,
        plugin_attribute_input_mode: int,
        calculation_mode: str,
        user_selection_id: str,
        output_dir_path: str,
    ):
        """
        启动计算线程

        :param inputbox_data; 未经处理的用户输入
        :param plugin_attribute_input_mode; 需要转换的模式
        :param calculation_mode; 计算模式
        :param user_selection_id; 用户选择的插件的id
        :param output_dir_path; 输出目录
        :return:
        """
        # 输入转换
        converted_data: str | float | int | None = self.typeConversion(
            plugin_attribute_input_mode, inputbox_data
        )
        if converted_data is None:  # 转换发生错误
            return None

        plugin_attributes: MetadataDict = instance_plugin_manager.getPluginAttributes(
            user_selection_id
        )  # 插件属性字典
        instance_plugin: ModuleType = instance_plugin_manager.getPluginInstance(
            user_selection_id
        )

        # 覆盖旧实例
        instance_calculate_thread = CalculationThread(
            converted_data=converted_data,
            calculation_mode=calculation_mode,
            output_dir_path=output_dir_path,
            plugin_attributes=plugin_attributes,
            instance_plugin=instance_plugin,
        )

        # 启动新实例
        instance_calculate_thread.start()
        return None

    @staticmethod
    def typeConversion(to_type: int, data: str) -> str | float | int | None:
        """
        类型转换

        :param to_type: 目标类型
        :param data: 需要转换的数据
        :return: 转换后的数据
        """
        try:
            match to_type:
                case hpyc.STRING:
                    ret = data
                case hpyc.FLOAT:
                    ret = float(data)  # type: ignore
                case hpyc.NUM:
                    ret = int(data)  # type: ignore
                case _:
                    ret = None  # type: ignore # 缺省 转换不存在的类型就none
        except Exception as e:
            instance_main_win_signal.set_output_box.emit(
                doc.TYPE_CONVERSION_ERROR_LITERAL % str(e)
            )
            traceback.print_exc()
            return None  # 缺省 转换错误就none
        return ret
