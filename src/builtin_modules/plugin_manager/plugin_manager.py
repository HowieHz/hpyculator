import os
import logging
import importlib
import hpyculator as hpyc
from typing import List, Dict


class PluginManager:
    def __init__(self):
        """初始化模块目录"""
        self.PLUGIN_DIR_PATH = str(os.path.join(os.getcwd(), "Plugin"))
        logging.debug(f"插件保存位置:{self.PLUGIN_DIR_PATH}")

        # 检查模块文件夹是否存在
        if os.path.exists(self.PLUGIN_DIR_PATH):
            pass
        else:
            os.makedirs(self.PLUGIN_DIR_PATH)

        # 载入模块
        self.plugin_files_and_folder_name: List[list] = []  # Plugin目录下读取到的文件夹和文件
        self.plugin_files_name_folder: List[str] = []  # Plugin目录下读取到的有__init__.py的文件夹
        # self.can_choose_number: List[str] = []  # 选择列表，储存着所有的选项名 #plugin_option_id_dict的键
        self.plugin_files_name_py: list[str] = []  # 储存着Plugin目录下的文件名
        self.plugin_option_id_dict: Dict[str, str] = {}  # 选项名和实际文件名的映射表
        self.loaded_plugin: Dict[str] = {}  # 存放加载完毕的插件对象 键值对：ID-读取的插件对象

    def __init_plugin_singer_file(self, plugin_files_name_py):
        """导入指定单文件插件

        :param plugin_files_name_py: 插件文件名列表，如[1.py,2.py,3.py]
        :return: None
        """

        def remove_file_suffix(file_name: str):
            return file_name.split(".")[0]

        plugin_files_name = map(remove_file_suffix, plugin_files_name_py)
        logging.debug(f"去掉.py后缀的文件名 {plugin_files_name}")
        for name in plugin_files_name:
            self.loaded_plugin[name] = importlib.import_module(
                f".{name}", package="Plugin"
            )
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            logging.debug(name)
            try:
                # self.can_choose_number.append(
                #     self.loaded_plugin[name].PLUGIN_METADATA['option_name'])  # 读取模块元数据，添加gui选项
                self.plugin_option_id_dict[
                    self.loaded_plugin[name].PLUGIN_METADATA["option_name"]
                ] = self.loaded_plugin[name].PLUGIN_METADATA["id"]
            except Exception as e:
                logging.debug(f"init_plugin_singer_file inside Exception:{e}")

    def __init_plugin_folder(self, plugin_files_name):
        """导入指定文件夹插件

        :param plugin_files_name: 文件夹插件名列表，如["a","b","c"]
        :return: None
        """
        logging.debug(f"读取到的文件夹插件:{plugin_files_name}")
        for name in plugin_files_name:
            self.loaded_plugin[name] = importlib.import_module(
                f".{name}.__init__", package="Plugin"
            )
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            logging.debug(name)
            try:
                # self.can_choose_number.append(
                #     self.loaded_plugin[name].PLUGIN_METADATA['option_name'])  # 读取模块元数据，添加gui选项
                self.plugin_option_id_dict[
                    self.loaded_plugin[name].PLUGIN_METADATA["option_name"]
                ] = self.loaded_plugin[name].PLUGIN_METADATA["id"]
            except Exception as e:
                logging.debug(f"init_plugin_folder inside Exception:{e}")

    @staticmethod
    def __readPluginPath(path):
        """读取指定目录下插件需重构

        :param path: 指定的目录 绝对路径
        :return: plugin_file_names  单文件插件的文件名,
        folder_plugin_names  文件夹插件的文件名
        """
        plugin_file_names = []
        folder_plugin_names = []
        for root, _dir, file in os.walk(path):
            plugin_file_names.append(file)
            root_list = str(root).split("\\")
            if root_list[-2] == "Plugin" and "__init__.py" in file:
                folder_plugin_names.append(root_list[-1])
        return plugin_file_names, folder_plugin_names

    def initPlugin(self):
        """导入插件

        :return: [dict]{插件id字段,对应的插件对象}
        """
        plugin_file_names, folder_plugin_names = self.__readPluginPath(
            self.PLUGIN_DIR_PATH
        )  # 读目录获取文件名

        # 从所有读取的文件中挑选出.py为后缀的文件
        for i_list in plugin_file_names:
            if (i_list[0].split("."))[
                -1
            ] == "py" and not self.plugin_files_name_py:  # 第一遍空列表才写入
                self.plugin_files_name_py = i_list

        try:
            self.__init_plugin_singer_file(self.plugin_files_name_py)  # 导入单文件插件
        except Exception as e:
            logging.debug(f"init_plugin_singer_file outside Exception:{e}")

        try:
            self.__init_plugin_folder(folder_plugin_names)  # 导入文件插件
        except Exception as e:
            logging.debug(f"init_plugin_folder outside Exception:{e}")

        # loaded_plugin: Optional[Dict[str, Callable]] = None  # 存放加载完毕的插件 ID-读取的插件
        # plugin_option_id_dict: Optional[Dict[str, str]] = None  # 选项名和实际文件名的映射表
        # selection_list: Optional[list[str]] = None  # 存放选项名列表
        # self.loaded_plugin
        return self.plugin_option_id_dict

    def getPluginAttribute(self, user_selection_id):
        """读取插件属性

        :param user_selection_id:
        :return: [list]attributes of plugin
        """
        plugin_attributes = {}  # 读取好的属性放在这里

        PLUGIN_METADATA = self.loaded_plugin[
            user_selection_id
        ].PLUGIN_METADATA  # PLUGIN_METADATA暂时储存着插件的元数据
        for option_name in [
            "output_start",
            "quantifier",
            "author",
            "help",
            "output_end",
            "fullwidth_symbol",
            "input_mode",
            "return_mode",
            "save_name",
            "output_name",
            "use_quantifier",
            "version",
        ]:
            if option_name in PLUGIN_METADATA:
                plugin_attributes[option_name] = PLUGIN_METADATA[option_name]
            else:
                plugin_attributes[option_name] = hpyc.OFF
        if plugin_attributes["fullwidth_symbol"] == hpyc.ON:
            plugin_attributes["help"] = (
                plugin_attributes["help"]
                .replace(",", "，")
                .replace(".", "。")
                .replace("'", "‘")
                .replace('"', "”")
                .replace("(", "（")
                .replace(")", "）")
            )

        return plugin_attributes

    def getPluginInstance(self, user_selection_id):
        """获取插件对象

        :param user_selection_id:
        :return: A instance of plugin
        """
        return self.loaded_plugin[user_selection_id]
