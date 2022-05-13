import datetime
import time
from threading import Thread
import tempfile
import os
from functools import partial  # 偏函数真好用
from hpyculator.hpysignal import main_window_signal
import hpyculator as hpyc
from typing import Any

# from multiprocessing import Process

from typing import Iterator

from ..plugin_manager import instance_plugin_manager


# TODO 用了多进程之后main_window_signal的实例化效果消失


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
        """启动计算线程

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
        calculate_thread = CalculationThread(
            inputbox_data, calculation_mode, user_selection_id, output_dir_path
        )

        # 启动新实例
        calculate_thread.start()
        return None

    @staticmethod
    def typeConversion(to_type: int, data: str):
        """类型转换

        :param to_type: 目标类型
        :param data: 需要转换的数据
        :return: 转换后的数据
        """
        try:
            if to_type == hpyc.STRING:
                data = str(data)
            elif to_type == hpyc.FLOAT:
                data = float(data)
            elif to_type == hpyc.NUM:
                data = int(data)
            else:
                data = None  # 缺省 转换不存在的类型就none
        except Exception as e:
            main_window_signal.setOutPutBox.emit(f"输入转换发生错误:{str(e)}\n\n请检查输入格式")
            return None  # 缺省 转换错误就none
        return data


class CalculationThread(Thread):
    def __init__(
        self,
        inputbox_data: Any,
        calculation_mode: str,
        user_selection_id: str,
        output_dir_path: str,
    ):
        """计算线程

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

    def run(self):
        inputbox_data = self.inputbox_data
        calculation_mode = self.calculation_mode
        # instance_plugin_manager.initPlugin()  # 多进程用
        plugin_attributes = instance_plugin_manager.getPluginAttribute(
            self.user_selection_id
        )  # 插件属性字典
        selected_plugin = instance_plugin_manager.getPluginInstance(
            self.user_selection_id
        )

        def whatNeedCalculate():
            """基础的计算模式"""
            calculate_fun = selected_plugin.on_calculate

            time_before_calculate = time.perf_counter()  # 储存开始时间

            if plugin_attribute_return_mode == hpyc.RETURN_ONCE:
                result = str(calculate_fun(inputbox_data))
                main_window_signal.appendOutPutBox.emit(
                    str(result) + "\n"
                )  # 结果为str，直接输出
            elif plugin_attribute_return_mode == hpyc.RETURN_LIST:  # 算一行输出一行
                result = calculate_fun(inputbox_data)
                for result_process in result:
                    main_window_signal.appendOutPutBox.emit(
                        str(result_process) + "\\n"
                    )  # 算一行输出一行
            elif (
                plugin_attribute_return_mode == hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE
            ):  # 算一行输出一行，但是没有换行
                result = calculate_fun(inputbox_data)
                for result_process in result:  # 计算
                    main_window_signal.appendOutPutBox.emit(
                        str(result_process)
                    )  # 算一行输出一行
            elif plugin_attribute_return_mode == hpyc.NO_RETURN_SINGLE_FUNCTION:
                calculate_fun(inputbox_data, "output")
            elif plugin_attribute_return_mode == hpyc.NO_RETURN:
                calculate_fun(inputbox_data)
            else:
                pass
            return time.perf_counter() - time_before_calculate  # 储存结束时间

        def whatNeedCalculateWithSave(filepath_name):
            """计算+保存模式"""
            # filepath_name - 储存保存到哪个文件里 路径+文件名

            calculate_fun = selected_plugin.on_calculate
            time_before_calculate = time.perf_counter()  # 储存开始时间

            with open(filepath_name, "w", encoding="utf-8") as filestream:
                if plugin_attribute_return_mode == hpyc.RETURN_ONCE:  # 分布输出和一次输出
                    result = calculate_fun(inputbox_data)
                    filestream.write(str(result) + "\n")
                elif plugin_attribute_return_mode == hpyc.RETURN_LIST:  # 算一行输出一行，但是没有换行
                    result = calculate_fun(inputbox_data)
                    for result_process in result:  # 计算
                        filestream.write(str(result_process) + "\\n")
                        filestream.flush()  # 算出来就存进去
                elif (
                    plugin_attribute_return_mode == hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE
                ):  # 算一行输出一行，但是没有换行
                    result = calculate_fun(inputbox_data)
                    for result_process in result:  # 计算
                        filestream.write(str(result_process))
                        filestream.flush()  # 算出来就存进去
                elif plugin_attribute_return_mode == hpyc.NO_RETURN:
                    hpyc.setIoInstance(filestream)
                    selected_plugin.on_calculate_with_save(inputbox_data)
                elif plugin_attribute_return_mode == hpyc.NO_RETURN_SINGLE_FUNCTION:
                    hpyc.setIoInstance(filestream)
                    calculate_fun(inputbox_data, "save")
                else:
                    pass

            return time.perf_counter() - time_before_calculate  # 储存结束时间

        def whatNeedCalculateWithOutputOptimization(limit=False):
            """计算+输出优化的模式（先把结果存临时文件，再读取输出）

            :param limit: 是否开启输出上限
            :return:
            """

            calculate_fun = selected_plugin.on_calculate

            with tempfile.TemporaryFile(
                "w+t", encoding="utf-8", errors="ignore"
            ) as filestream:
                time_before_calculate = time.perf_counter()  # 储存开始时间

                try:
                    if plugin_attribute_return_mode == hpyc.RETURN_ONCE:  # 分布输出和一次输出
                        result = calculate_fun(inputbox_data)
                        filestream.write(str(result) + "\n")
                    elif (
                        plugin_attribute_return_mode == hpyc.RETURN_LIST
                    ):  # 算一行输出一行，但是没有换行
                        result = calculate_fun(inputbox_data)
                        for result_process in result:  # 计算
                            filestream.write(str(result_process) + "\\n")
                            filestream.flush()  # 算出来就存进去
                    elif (
                        plugin_attribute_return_mode
                        == hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE
                    ):  # 算一行输出一行，但是没有换行
                        result = calculate_fun(inputbox_data)
                        for result_process in result:  # 计算
                            filestream.write(str(result_process))
                            filestream.flush()  # 算出来就存进去
                    elif plugin_attribute_return_mode == hpyc.NO_RETURN_SINGLE_FUNCTION:
                        hpyc.setIoInstance(filestream)
                        calculate_fun(inputbox_data, "save")
                    elif plugin_attribute_return_mode == hpyc.NO_RETURN:
                        hpyc.setIoInstance(filestream)
                        selected_plugin.on_calculate_with_save(inputbox_data)
                    else:
                        pass
                finally:
                    filestream.seek(0)  # 将文件指针移到开始处，准备读取文件
                    if limit:
                        for times, line in enumerate(quickTraverseFile(filestream)):
                            main_window_signal.appendOutPutBox.emit(line)
                            if times >= 128:
                                main_window_signal.appendOutPutBox.emit(
                                    "\n\n输出上限：检测到输出数据过大，请使用保存到文件防止卡死"
                                )
                                break
                    else:
                        for line in quickTraverseFile(filestream):
                            main_window_signal.appendOutPutBox.emit(line)

            return time.perf_counter() - time_before_calculate  # 储存结束时间

        def quickTraverseFile(file, chunk_size=8192) -> Iterator:
            """较快，低占用读取文件，迭代器

            :param file: 打开的文件流对象
            :param chunk_size: 一次读取的字节大小
            :return: 读取到的字节
            """
            for chunk in iter(
                partial(file.read, chunk_size), ""
            ):  # 用readline的话，读到换行符就会直接停止读取，不会读取到8192B，会增加读取次数
                yield chunk

        def calculate_save_mode(output_dir_path):
            """调用计算并保存的模式"""
            if plugin_attributes["use_quantifier"] == hpyc.ON:
                filename = f"{datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')} {plugin_attributes['save_name']}{str(inputbox_data)}{plugin_attributes['quantifier']}"
            else:
                filename = f"{datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')} {str(inputbox_data).replace('.', '_')}的{plugin_attributes['save_name']}"
            filepath_name = os.path.join(output_dir_path, f"{filename}.txt")
            time_spent = whatNeedCalculateWithSave(filepath_name)
            # 以下是计算后工作
            main_window_signal.appendOutPutBox.emit(
                f"""\n\n本次计算+保存花费了{time_spent:.6f}秒\n\n计算结果已保存在 {filepath_name} """
            )  # 输出本次计算时间

        def calculate_o_mode(limit=False):
            """调用计算+输出优化的模式"""
            time_spent = whatNeedCalculateWithOutputOptimization(limit)
            # 以下是计算后工作
            main_window_signal.appendOutPutBox.emit(
                f"""\n\n本次计算+输出花费了{time_spent:.6f}秒\n\n已启用输出优化"""
            )  # 输出本次计算时间

        def calculate_base_mode():
            """调用基础计算模式"""
            time_spent = whatNeedCalculate()
            # 以下是计算后工作
            main_window_signal.appendOutPutBox.emit(
                f"\n\n本次计算+输出花费了{time_spent:.6f}秒\n"
            )  # 输出本次计算时间

        # ------------------------------------------这些ui逻辑需外移
        main_window_signal.setStartButtonText.emit("计算程序正在运行中，请耐心等待")
        main_window_signal.setStartButtonState.emit(False)  # 防止按钮反复触发
        main_window_signal.clearOutPutBox.emit()  # 清空输出框
        plugin_attribute_return_mode = plugin_attributes["return_mode"]
        try:
            if calculation_mode == "calculate_save":
                calculate_save_mode(self.output_dir_path)
            elif calculation_mode == "calculate_o":
                calculate_o_mode()
            elif calculation_mode == "calculate_o_l":
                calculate_o_mode(limit=True)
            elif calculation_mode == "calculate":
                calculate_base_mode()
        except Exception as e:
            main_window_signal.setOutPutBox.emit(f"插件运算发生错误：{str(e)}\n\n请检查输入格式")
        main_window_signal.setOutPutBoxCursor.emit("end")  # 光标设到文本框尾部
        main_window_signal.setStartButtonText.emit("计算")  # 设置按钮字
        main_window_signal.setStartButtonState.emit(True)  # 启用按钮
