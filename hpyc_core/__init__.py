"""创建core"""
import os
import sys
import importlib
from queue import Queue
from typing import Optional, Any
from types import ModuleType

from hpyculator import message_queue, output_queue, error_queue

from .plugin import instance_plugin_manager  # 插件管理
from .settings import hpysettings
from .data_structure import MetadataDict
from .compute import CalculationManager

instance_settings_file: Any = None

# TODO  整体放到一个进程里面


class Core:
    """创建core"""

    def __init__(
        self,
        output_dir_path: Optional[str] = None,
        settings_dir_path: Optional[str] = None,
        plugins_dir_path: Optional[str] = None,
        settings_file_name: str = "hpyculator_setting",
        settings_file_format: str = "json",
    ) -> None:
        """"""
        global instance_settings_file
        # 初始化参数 采用顺序 输入 > 设置文件 > 初始化
        self.settings_dir_path = (
            settings_dir_path
            if settings_dir_path
            else str(os.path.join(os.getcwd(), "Setting"))  # 默认设置文件存放目录
        )
        instance_settings_file = hpysettings.load(
            settings_dir_path=settings_dir_path,
            settings_file_name=settings_file_name,
            settings_file_format=settings_file_format,
        )  # 单例

        self.output_dir_path = self._checkOutputPath(output_dir_path)  # 输出路径检查

        self.plugins_dir_path = self._checkPluginsPath(plugins_dir_path)  # 插件存放路径检查
        self.eventReloadPlugins()  # 加载插件

    @staticmethod
    def getOutputQueue() -> Queue:
        """获取输出队列

        :return: 输出队列
        """
        return output_queue

    @staticmethod
    def getErroeQueue() -> Queue:
        """获取错误输出队列

        :return: 错误输出队列
        """
        return error_queue

    @staticmethod
    def getMessageQueue() -> Queue:
        """获取消息输出队列

        :return: 消息输出队列
        """
        return message_queue

    def getPluginsDirPath(self) -> str:
        """获取插件存放路径

        :return: 插件存放路径
        :rtype: str
        """
        return self.plugins_dir_path

    def getOutputDirPath(self) -> str:
        """获取输出路径

        :return: 输出路径
        """
        return self.output_dir_path

    def getSettingsDirPath(self) -> str:
        """获取设置文件存放路径

        :return: 设置文件存放路径
        """
        return self.settings_dir_path

    @staticmethod
    def getPluginsTagOption() -> tuple[tuple[tuple[str, ...], str], ...]:
        """获取所有插件的tag，tag对应插件选项名
        [(plugin1_tags: list, plugin1_option), (plugin2_tags: list, plugin2_option)]

        :return: 所有插件的tag以及对应选项名
        """
        return instance_plugin_manager.list_alL_plugin_tag_option

    @staticmethod
    def getPluginsOptionToId() -> dict[str, str]:
        """获取插件选项名和id的映射表

        :return: 选项名映射id的字典
        """
        return instance_plugin_manager.option_id_dict

    @staticmethod
    def getPluginInstance(id: str) -> ModuleType:
        """获取对应插件实例

        :param id:
        :return: 插件实例
        """
        return instance_plugin_manager.getPluginInstance(id)

    @staticmethod
    def getPluginMetadata(id: str) -> MetadataDict:
        """获取对应插件元数据

        :param id:
        :return: 插件元数据
        """
        return instance_plugin_manager.getPluginMetadata(id)

    def setPluginsDirPath(self, path: str) -> None:
        """设置插件存放目录并且重新加载插件

        :param path: 新插件存放目录
        :return: None
        """
        self.plugins_dir_path = self._checkPluginsPath(path)
        self.eventReloadPlugins()

    def eventReloadPlugins(self):
        """重新加载插件"""
        instance_plugin_manager.initPlugin(self.plugins_dir_path)  # 加载插件

    def eventStartCalculate(self, plugin_id: str, input_data: Any, mode="Return"):
        """启动计算

        :param plugin_id: 插件id
        :param input_data: 未处理的原始输入数据
        :param mode: 计算模式
        :return: None
        :raise ValueError: 当输入了不存在的mode
        """
        modes = (
            (
                "ReturnAfterComputing",
                "ComputingAndReturn",
                "RAC",
                "Return",
                "ReturnAfterCalculating",
            ),
            (
                "SaveAfterComputing",
                "ComputingAndSave",
                "SAC",
                "Save",
                "SaveAfterCalculating",
            ),
            (
                "ReturnAfterComputingFromBuffer",
                "ComputingAndReturnFromBuffer",
                "RACFB",
                "ReturnFromBuffer",
                "ReturnAfterCalculatingFromBuffer",
            ),
            (
                "ReturnAfterComputingFromLimitedBuffer",
                "ComputingAndReturnFromLimitedBuffer",
                "RACFLB",
                "ReturnFromLimitedBuffer",
                "ReturnAfterCalculatingFromLimitedBuffer",
            ),
        )  # 计算模式
        if mode in modes[0]:
            calculation_mode = "Save"
        elif mode in modes[1]:
            calculation_mode = "Return"
        elif mode in modes[2]:
            calculation_mode = "ReturnFromBuffer"
        elif mode in modes[3]:
            calculation_mode = "ReturnFromLimitedBuffer"
        else:
            raise ValueError

        compute_manager = CalculationManager()
        compute_manager.start(  # TODO 需简化
            input_data=input_data,
            calculation_mode=calculation_mode,
            user_selection_id=plugin_id,
            output_dir_path=self.output_dir_path,
        )  # 启动计算

    @staticmethod
    def eventExit() -> None:
        """退出流程，防止进程残留"""

        def _exitJpype():
            # 退出流程，否则虚拟机不会退出，导致进程残留
            jpype = importlib.import_module("jpype")  # 不直接用import是防止打包程序识别到

            if jpype.isJVMStarted():
                jpype.shutdownJVM()

        _check_modules = {"jpype": _exitJpype}
        for _module in _check_modules:
            if _module in sys.modules:
                _check_modules[_module]()  # 调用对应退出处理函数

    @staticmethod
    def _checkOutputPath(path: Optional[str] = None) -> str:
        """设置输出目录(当path有值),
        读取输出目录(当path无值)

        :param path: 输出目录
        :return: output_dir_path
        """
        if path:
            output_dir_path = path
            instance_settings_file.add(
                key="output_dir_path", value=output_dir_path
            )  # 强制覆盖
        elif instance_settings_file.exists("output_dir_path"):  # 读取配置
            output_dir_path = instance_settings_file.read("output_dir_path")
        else:  # 初始化 为启动位置同目录下的Output文件夹
            output_dir_path = str(os.path.join(os.getcwd(), "Output"))
            instance_settings_file.add(
                key="output_dir_path", value=output_dir_path
            )  # 添加到配置文件

        # 检查输出文件夹是否存在
        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)

        return output_dir_path  # 返回输出路径

    @staticmethod
    def _checkPluginsPath(path: Optional[str] = None) -> str:
        """设置存放插件的路径(当path有值),
        读取存放插件的路径(当path无值)

        :param path: 插件存放目录
        :return: 放置插件的路径
        """
        if path:
            plugins_dir_path = path
            instance_settings_file.add(
                key="plugins_dir_path", value=plugins_dir_path
            )  # 强制覆盖
        elif instance_settings_file.exists("plugins_dir_path"):  # 从设置文件读取插件目录
            plugins_dir_path = instance_settings_file.read("plugins_dir_path")
        else:  # 初始化 为启动位置同目录下的Plugin文件夹
            plugins_dir_path = str(os.path.join(os.getcwd(), "Plugin"))
            instance_settings_file.add(
                key="plugins_dir_path", value=plugins_dir_path
            )  # 添加到配置文件

        if not os.path.exists(plugins_dir_path):  # 检查存放模块的文件夹是否存在
            os.makedirs(plugins_dir_path)  # 不存在生成文件夹

        return plugins_dir_path  # 返回插件存放路径
