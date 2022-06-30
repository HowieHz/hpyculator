import datetime
import os
import tempfile
import time
import traceback
from functools import partial  # 偏函数真好用
from threading import Thread
from types import ModuleType
from typing import IO, Generator

import hpyculator as hpyc
from hpyculator.hpysignal import instance_main_win_signal

from .. import document as doc
from ..data_structure import MetadataDict
from ..plugin import instance_plugin_manager


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
    ) -> None:
        """启动计算线程

        :param inputbox_data: 未经处理的用户输入
        :type inputbox_data: str
        :param plugin_attribute_input_mode: 需要转换的模式
        :type plugin_attribute_input_mode: int
        :param calculation_mode: 计算模式
        :type calculation_mode: str
        :param user_selection_id: 用户选择的插件的id
        :type user_selection_id: str
        :param output_dir_path: 输出目录
        :type output_dir_path: str
        :return: None
        :rtype: None
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
        """类型转换

        :param to_type: 目标类型
        :type to_type: int
        :param data: 需要转换的数据
        :type data: str
        :return: 转换后的数据
        :rtype: str | float | int | None
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


class CalculationThread(Thread):
    def __init__(
        self,
        converted_data: str | float | int,
        calculation_mode: str,
        output_dir_path: str,
        plugin_attributes: MetadataDict,
        instance_plugin: ModuleType,
    ):
        """计算线程

        :param converted_data: 经过类型转换处理的用户输入
        :type converted_data: str | float | int
        :param calculation_mode: 计算模式
        :type calculation_mode: str
        :param output_dir_path: 输出目录
        :type output_dir_path: str
        :param plugin_attributes: 插件属性
        :type plugin_attributes: MetadataDict
        :param instance_plugin: 插件实例
        :type instance_plugin: ModuleType
        """
        Thread.__init__(self)
        # Process.__init__(self)
        self.daemon: bool = True  # 避免后台残留
        self.converted_data: str | float | int = converted_data
        self.calculation_mode: str = calculation_mode
        self.output_dir_path: str = output_dir_path
        self.plugin_attributes: MetadataDict = plugin_attributes  # 插件属性字典
        self.instance_plugin: ModuleType = instance_plugin  # 插件加载实例

    def run(self) -> None:
        converted_data: str | float | int = self.converted_data
        calculation_mode: str = self.calculation_mode
        plugin_attributes: MetadataDict = self.plugin_attributes  # 插件属性字典
        selected_plugin: ModuleType = self.instance_plugin  # 插件加载实例

        instance_main_win_signal.draw_background.emit()  # 不知道为何使用了打表模式之后会掉背景，干脆重绘一次背景
        instance_main_win_signal.set_start_button_text.emit(
            doc.CALCULATION_PROGRAM_IS_RUNNING_LITERAL
        )
        instance_main_win_signal.set_start_button_state.emit(False)  # 防止按钮反复触发
        instance_main_win_signal.clear_output_box.emit()  # 清空输出框
        plugin_attribute_return_mode = plugin_attributes["return_mode"]
        try:
            match calculation_mode:
                case "calculate_save":
                    filename: str = f"{datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')} {plugin_attributes['save_name']}{str(converted_data)}{plugin_attributes['quantifier']}"
                    filepath_name: str = os.path.join(
                        self.output_dir_path, f"{filename}.txt"
                    )
                    time_spent: int = _calculateWithSave(filepath_name)
                    _outputSpentTime(
                        time_spent,
                        doc.THIS_CALCULATION_AND_SAVING_TOOK_LITERAL,
                        f"{doc.SAVED_IN_LITERAL} {filepath_name}",
                    )  # 输出本次计算时间
                case "calculate_o":
                    time_spent = _calculateWithOutputOptimization(limit=False)
                    _outputSpentTime(
                        time_spent,
                        doc.THIS_CALCULATION_AND_OUTPUT_TOOK_LITERAL,
                        doc.OUTPUT_OPTIMIZATION_ENABLED_LITERAL,
                    )  # 输出本次计算时间
                case "calculate_o_l":
                    time_spent = _calculateWithOutputOptimization(limit=True)
                    _outputSpentTime(
                        time_spent,
                        doc.THIS_CALCULATION_AND_OUTPUT_TOOK_LITERAL,
                        doc.OUTPUT_OPTIMIZATION_ENABLED_LITERAL,
                    )  # 输出本次计算时间
                case "calculate":
                    time_spent = _baseCalculate()
                    _outputSpentTime(
                        time_spent, doc.THIS_CALCULATION_AND_OUTPUT_TOOK_LITERAL
                    )  # 输出本次计算时间
        except Exception as e:
            instance_main_win_signal.set_output_box.emit(
                doc.PLUGIN_CALCULATION_ERROR_LITERAL % str(e)
            )
            traceback.print_exc()
        instance_main_win_signal.set_output_box_cursor.emit("end")  # 光标设到文本框尾部
        instance_main_win_signal.set_start_button_text.emit(
            doc.CALCULATION_LITERAL
        )  # 设置按钮字
        instance_main_win_signal.set_start_button_state.emit(True)  # 启用按钮
        instance_main_win_signal.draw_background.emit()  # 不知道为何使用了打表模式之后会掉背景，干脆重绘一次背景

        def _baseCalculate() -> int:
            """基础的计算模式

            :return: 计算花费的时间 单位ns
            :rtype: int
            """
            calculate_fun = selected_plugin.on_calculate
            time_before_calculate = time.perf_counter_ns()  # 储存开始时间
            match plugin_attribute_return_mode:
                case hpyc.RETURN_ONCE:
                    result = str(calculate_fun(converted_data))
                    instance_main_win_signal.append_output_box.emit(
                        str(result) + "\n"
                    )  # 结果为str，直接输出
                case hpyc.RETURN_ITERABLE:  # 算一行输出一行
                    result = calculate_fun(converted_data)
                    for result_process in result:
                        instance_main_win_signal.append_output_box.emit(
                            str(result_process)
                        )  # 算一行输出一行
                case hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                    result = calculate_fun(converted_data)
                    for result_process in result:  # 计算
                        instance_main_win_signal.insert_output_box.emit(
                            str(result_process)
                        )  # 算一行输出一行
                case hpyc.NO_RETURN_SINGLE_FUNCTION:
                    calculate_fun(converted_data, "output")
                case hpyc.NO_RETURN:
                    calculate_fun(converted_data)
                case _:
                    pass
            return time.perf_counter_ns() - time_before_calculate  # 储存结束时间

        def _calculateWithSave(filepath: str) -> int:
            """计算+保存模式

            :return: 计算花费的时间 单位ns
            :rtype: int
            """
            # filepath - 储存保存到哪个文件里 路径+文件名
            calculate_fun = selected_plugin.on_calculate
            time_before_calculate = time.perf_counter_ns()  # 储存开始时间
            with open(
                filepath,
                mode="w",
                buffering=1073741824,  # 1,073,741,824B = 1024MB  给插件足够的内存做缓冲区，也避免插件使得电脑内存爆炸
                encoding="utf-8",
            ) as filestream:  # buffering为-1的时候其实就是8192，现在显式的写出来
                match plugin_attribute_return_mode:
                    case hpyc.RETURN_ONCE:  # 分布输出和一次输出
                        result = calculate_fun(converted_data)
                        filestream.write(str(result) + "\n")
                    case hpyc.RETURN_ITERABLE:  # 算一行输出一行，但是没有换行
                        result = calculate_fun(converted_data)
                        for result_process in result:  # 计算
                            filestream.write(str(result_process) + "\n")
                        filestream.flush()  # 算出来最后存进去
                    case hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                        result = calculate_fun(converted_data)
                        for result_process in result:  # 计算
                            filestream.write(str(result_process))
                        filestream.flush()  # 算出来最后存进去
                    case hpyc.NO_RETURN:
                        hpyc.setIoInstance(filestream)
                        selected_plugin.on_calculate_with_save(converted_data)
                    case hpyc.NO_RETURN_SINGLE_FUNCTION:
                        hpyc.setIoInstance(filestream)
                        calculate_fun(converted_data, "save")
                    case _:
                        pass
            return time.perf_counter_ns() - time_before_calculate  # 储存结束时间

        def _calculateWithOutputOptimization(limit=False) -> int:
            """
            计算+输出优化的模式（先把结果存临时文件，再读取输出）

            :param limit: 是否开启输出上限，默认是False
            :type limit: bool
            :return: 计算花费的时间 单位ns
            :rtype: int
            """
            calculate_fun = selected_plugin.on_calculate
            with tempfile.TemporaryFile(
                mode="w+t",
                buffering=1073741824,  # 1,073,741,824B = 1024MB  给插件足够的内存做缓冲区，也避免插件使得电脑内存爆炸
                encoding="utf-8",
                errors="ignore",
            ) as filestream:
                time_before_calculate = time.perf_counter_ns()  # 储存开始时间
                try:
                    match plugin_attribute_return_mode:
                        case hpyc.RETURN_ONCE:  # 分布输出和一次输出
                            result = calculate_fun(converted_data)
                            filestream.write(str(result) + "\n")
                        case hpyc.RETURN_ITERABLE:  # 算一行输出一行，但是没有换行
                            result = calculate_fun(converted_data)
                            for result_process in result:  # 计算
                                filestream.write(str(result_process) + "\n")
                            filestream.flush()  # 算出来最后存进去
                        case hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                            result = calculate_fun(converted_data)
                            for result_process in result:  # 计算
                                filestream.write(str(result_process))
                            filestream.flush()  # 算出来最后存进去
                        case hpyc.NO_RETURN:
                            hpyc.setIoInstance(filestream)
                            selected_plugin.on_calculate_with_save(converted_data)
                        case hpyc.NO_RETURN_SINGLE_FUNCTION:
                            hpyc.setIoInstance(filestream)
                            calculate_fun(converted_data, "save")
                        case _:
                            pass
                finally:
                    filestream.seek(0)  # 将文件指针移到开始处，准备读取文件
                    if limit:
                        for times, line in enumerate(_quickTraverseFile(filestream)):
                            instance_main_win_signal.append_output_box.emit(line)
                            if times >= 128:
                                instance_main_win_signal.append_output_box.emit(
                                    doc.REACHED_OUTPUT_LIMIT_LITERAL
                                )
                                break
                    else:
                        for line in _quickTraverseFile(filestream):
                            instance_main_win_signal.append_output_box.emit(line)
            return time.perf_counter_ns() - time_before_calculate  # 储存结束时间

        def _quickTraverseFile(file: IO, chunk_size: int = 8192) -> Generator:
            """较快，低占用读取文件，迭代器

            :param file: 打开的文件流对象
            :type file: IO
            :param chunk_size: 一次读取的字节大小,默认为8192
            :type chunk_size: int
            :yield: 读取到的字节
            :rtype: Generator
            """
            for chunk in iter(
                partial(file.read, chunk_size), ""
            ):  # 用readline的话，读到换行符就会直接停止读取，不会读取到8192B，会增加读取次数
                yield chunk

        def _outputSpentTime(
            time_spent_ns: int = 0, prefix: str = "", suffix: str = ""
        ) -> None:
            """输出计算总结

            :param time_spent_ns: 所花费的时间（单位ns）, 默认为0
            :type time_spent_ns: int
            :param prefix: 前缀, 默认为""
            :type prefix: str
            :param suffix: 后缀, 默认为""
            :type suffix: str
            """
            instance_main_win_signal.append_output_box_.emit(
                f"\n\n"
                f"{prefix}"
                f"{time_spent_ns}ns\n"
                f"={time_spent_ns / 10_0000_0000}s\n"
                f"={time_spent_ns / 600_0000_0000}min\n\n"
                f"{suffix}"
            )  # 输出本次计算时间
