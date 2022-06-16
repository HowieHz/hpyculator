import datetime
import os
import tempfile
import time
import traceback
from functools import partial  # 偏函数真好用
from threading import Thread
from typing import Generator, Union

import hpyculator as hpyc
from hpyculator.hpysignal import instance_main_win_signal

from .. import document as doc
from ..plugin import instance_plugin_manager

# from multiprocessing import Process
# TODO 用了多进程之后main_win_signal的实例化效果消失


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
        inputbox_data = self.typeConversion(plugin_attribute_input_mode, inputbox_data)
        if inputbox_data is None:  # 转换发生错误
            return None

        # 覆盖旧实例
        instance_calculate_thread = CalculationThread(
            inputbox_data=inputbox_data,
            calculation_mode=calculation_mode,
            user_selection_id=user_selection_id,
            output_dir_path=output_dir_path,
        )

        # 启动新实例
        instance_calculate_thread.start()
        return None

    @staticmethod
    def typeConversion(to_type: int, data: str):
        """
        类型转换

        :param to_type: 目标类型
        :param data: 需要转换的数据
        :return: 转换后的数据
        """
        try:
            match to_type:
                case hpyc.STRING:
                    data = str(data)
                case hpyc.FLOAT:
                    data = float(data)
                case hpyc.NUM:
                    data = int(data)
                case _:
                    data = None  # 缺省 转换不存在的类型就none
        except Exception as e:
            instance_main_win_signal.set_output_box.emit(
                doc.TYPE_CONVERSION_ERROR_LITERAL % str(e)
            )
            traceback.print_exc()
            return None  # 缺省 转换错误就none
        return data


class CalculationThread(Thread):
    def __init__(
        self,
        inputbox_data: Union[str, float, int],
        calculation_mode: str,
        user_selection_id: str,
        output_dir_path: str,
    ):
        """
        计算线程

        :param inputbox_data: 经过类型转换处理的用户输入
        :param calculation_mode; 计算模式
        :param user_selection_id; 用户选择的插件的id
        :param output_dir_path; 输出目录
        :return:
        """
        Thread.__init__(self)
        self.daemon = True  # 避免后台残留

        self.inputbox_data = inputbox_data
        self.calculation_mode = calculation_mode
        self.user_selection_id = user_selection_id
        self.output_dir_path = output_dir_path

    def run(self) -> None:
        inputbox_data = self.inputbox_data
        calculation_mode = self.calculation_mode
        # instance_plugin_manager.initPlugin()  # 多进程用
        plugin_attributes = instance_plugin_manager.getPluginAttributes(
            self.user_selection_id
        )  # 插件属性字典
        selected_plugin = instance_plugin_manager.getPluginInstance(
            self.user_selection_id
        )

        def _baseCalculate() -> int:
            """基础的计算模式"""
            calculate_fun = selected_plugin.on_calculate

            time_before_calculate = time.perf_counter_ns()  # 储存开始时间

            match plugin_attribute_return_mode:
                case hpyc.RETURN_ONCE:
                    result = str(calculate_fun(inputbox_data))
                    instance_main_win_signal.append_output_box.emit(
                        str(result) + "\n"
                    )  # 结果为str，直接输出
                case hpyc.RETURN_ITERABLE:  # 算一行输出一行
                    result = calculate_fun(inputbox_data)
                    for result_process in result:
                        instance_main_win_signal.append_output_box.emit(
                            str(result_process) + "\\n"
                        )  # 算一行输出一行
                case hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                    result = calculate_fun(inputbox_data)
                    for result_process in result:  # 计算
                        instance_main_win_signal.append_output_box.emit(
                            str(result_process)
                        )  # 算一行输出一行
                case hpyc.NO_RETURN_SINGLE_FUNCTION:
                    calculate_fun(inputbox_data, "output")
                case hpyc.NO_RETURN:
                    calculate_fun(inputbox_data)
                case _:
                    pass
            return time.perf_counter_ns() - time_before_calculate  # 储存结束时间

        def _calculateWithSave(filepath: str) -> int:
            """计算+保存模式"""
            # filepath - 储存保存到哪个文件里 路径+文件名

            calculate_fun = selected_plugin.on_calculate
            time_before_calculate = time.perf_counter_ns()  # 储存开始时间

            with open(filepath, "w", encoding="utf-8") as filestream:
                match plugin_attribute_return_mode:
                    case hpyc.RETURN_ONCE:  # 分布输出和一次输出
                        result = calculate_fun(inputbox_data)
                        filestream.write(str(result) + "\n")
                    case hpyc.RETURN_ITERABLE:  # 算一行输出一行，但是没有换行
                        result = calculate_fun(inputbox_data)
                        for result_process in result:  # 计算
                            filestream.write(str(result_process) + "\\n")
                            filestream.flush()  # 算出来就存进去
                    case hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                        result = calculate_fun(inputbox_data)
                        for result_process in result:  # 计算
                            filestream.write(str(result_process))
                            filestream.flush()  # 算出来就存进去
                    case hpyc.NO_RETURN:
                        hpyc.setIoInstance(filestream)
                        selected_plugin.on_calculate_with_save(inputbox_data)
                    case hpyc.NO_RETURN_SINGLE_FUNCTION:
                        hpyc.setIoInstance(filestream)
                        calculate_fun(inputbox_data, "save")
                    case _:
                        pass

            return time.perf_counter_ns() - time_before_calculate  # 储存结束时间

        def _calculateWithOutputOptimization(limit=False) -> int:
            """
            计算+输出优化的模式（先把结果存临时文件，再读取输出）

            :param limit: 是否开启输出上限
            :return:
            """
            calculate_fun = selected_plugin.on_calculate
            with tempfile.TemporaryFile(
                "w+t", encoding="utf-8", errors="ignore"
            ) as filestream:
                time_before_calculate = time.perf_counter_ns()  # 储存开始时间

                try:
                    match plugin_attribute_return_mode:
                        case hpyc.RETURN_ONCE:  # 分布输出和一次输出
                            result = calculate_fun(inputbox_data)
                            filestream.write(str(result) + "\n")
                        case hpyc.RETURN_ITERABLE:  # 算一行输出一行，但是没有换行
                            result = calculate_fun(inputbox_data)
                            for result_process in result:  # 计算
                                filestream.write(str(result_process) + "\\n")
                                filestream.flush()  # 算出来就存进去
                        case hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE:  # 算一行输出一行，但是没有换行
                            result = calculate_fun(inputbox_data)
                            for result_process in result:  # 计算
                                filestream.write(str(result_process))
                                filestream.flush()  # 算出来就存进去
                        case hpyc.NO_RETURN_SINGLE_FUNCTION:
                            hpyc.setIoInstance(filestream)
                            calculate_fun(inputbox_data, "save")
                        case hpyc.NO_RETURN:
                            hpyc.setIoInstance(filestream)
                            selected_plugin.on_calculate_with_save(inputbox_data)
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

        def _quickTraverseFile(file: open, chunk_size: int = 8192) -> Generator:
            """
            较快，低占用读取文件，迭代器

            :param file: 打开的文件流对象
            :param chunk_size: 一次读取的字节大小
            :return: 读取到的字节
            """
            for chunk in iter(
                partial(file.read, chunk_size), ""
            ):  # 用readline的话，读到换行符就会直接停止读取，不会读取到8192B，会增加读取次数
                yield chunk

        def _outputSpentTime(
            time_spent_ns: int = 0, prefix: str = "", suffix: str = ""
        ) -> None:
            """

            :param time_spent_ns: 所花费的时间（单位ns）
            :param prefix: 前缀
            :param suffix: 后缀
            :return:
            """
            instance_main_win_signal.append_output_box.emit(
                f"\n\n"
                f"{prefix}"
                f"{time_spent_ns}ns\n"
                f"={time_spent_ns / 10_0000_0000}s\n"
                f"={time_spent_ns / 600_0000_0000}min\n\n"
                f"{suffix}"
            )  # 输出本次计算时间

        # ------------------------------------------这些ui逻辑需外移
        instance_main_win_signal.set_start_button_text.emit(
            doc.CALCULATION_PROGRAM_IS_RUNNING_LITERAL
        )
        instance_main_win_signal.set_start_button_state.emit(False)  # 防止按钮反复触发
        instance_main_win_signal.clear_output_box.emit()  # 清空输出框
        plugin_attribute_return_mode = plugin_attributes["return_mode"]
        try:
            match calculation_mode:
                case "calculate_save":
                    filename = f"{datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')} {plugin_attributes['save_name']}{str(inputbox_data)}{plugin_attributes['quantifier']}"

                    filepath_name = os.path.join(
                        self.output_dir_path, f"{filename}.txt"
                    )
                    time_spent = _calculateWithSave(filepath_name)
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
