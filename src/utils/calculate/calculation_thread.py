import datetime
import os
import tempfile
import time
import traceback

from functools import partial  # 偏函数真好用
from threading import Thread
from typing import Generator, Optional

from ..plugin import instance_plugin_manager
from .. import document as doc
import hpyculator as hpyc
from hpyculator.hpysignal import instance_main_win_signal

# from multiprocessing import Process


class CalculationThread(Thread):
    def __init__(
        self,
        converted_data: str | float | int,
        calculation_mode: str,
        user_selection_id: str,
        output_dir_path: str,
    ):
        """
        计算线程

        :param converted_data: 经过类型转换处理的用户输入
        :param calculation_mode; 计算模式
        :param user_selection_id; 用户选择的插件的id
        :param output_dir_path; 输出目录
        :return:
        """
        Thread.__init__(self)
        # Process.__init__(self)
        self.daemon: bool = True  # 避免后台残留

        self.converted_data: str | float | int = converted_data
        self.calculation_mode: str = calculation_mode
        self.user_selection_id: str = user_selection_id
        self.output_dir_path: str = output_dir_path

    def run(self) -> None:
        converted_data: str | float | int = self.converted_data
        calculation_mode: str = self.calculation_mode
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

        def _calculateWithSave(filepath: Optional[str] = None) -> int:
            """计算+保存模式
            计算+输出优化的模式（先把结果存临时文件，再读取输出）
            """
            # filepath - 储存保存到哪个文件里 路径+文件名

            calculate_fun = selected_plugin.on_calculate

            def _open_filestream():
                if filepath:  # 传入了保存路径，说明是要保存
                    return open(
                        filepath,
                        mode="w",
                        buffering=1073741824,  # 1,073,741,824B = 1024MB  给插件足够的内存做缓冲区，也避免插件使得电脑内存爆炸
                        encoding="utf-8",
                    )
                return tempfile.TemporaryFile(
                    mode="w+t",
                    buffering=1073741824,  # 1,073,741,824B = 1024MB  给插件足够的内存做缓冲区，也避免插件使得电脑内存爆炸
                    encoding="utf-8",
                    errors="ignore",
                )

            with _open_filestream() as filestream:  # buffering为-1的时候其实就是8192，现在显式的写出来
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
                    if self.calculation_mode in ("calculate_o", "calculate_o_l"):
                        filestream.seek(0)  # 将文件指针移到开始处，准备读取文件
                        if self.calculation_mode == "calculate_o_l":  # 输出上限
                            for times, line in enumerate(
                                _quickTraverseFile(filestream)
                            ):
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

        def _quickTraverseFile(file, chunk_size: int = 8192) -> Generator:
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
            instance_main_win_signal.append_output_box_.emit(
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
                case "calculate_o" | "calculate_o_l":
                    time_spent = _calculateWithSave()
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
