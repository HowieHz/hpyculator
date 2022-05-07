import os
import logging
import importlib
from typing import List, Dict

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)  # 禁用日志


class Manager:
    def __init__(self):
        # 初始化模块目录
        self.PLUGIN_DIR_PATH = str(os.path.join(os.getcwd(), 'Plugin'))
        logging.debug(f'插件保存位置:{self.PLUGIN_DIR_PATH}')

        # 检查模块文件夹是否存在
        if os.path.exists(self.PLUGIN_DIR_PATH):
            pass
        else:
            os.makedirs(self.PLUGIN_DIR_PATH)

        # 载入模块
        self.plugin_files_and_folder_name: List[list] = []  # Plugin目录下读取到的文件夹和文件
        self.plugin_files_name_folder: List[str] = []  # Plugin目录下读取到的有__init__.py的文件夹
        # self.can_choose_number: List[str] = []  # 选择列表，储存着所有的选项名 #plugin_filename_option_name_map的键
        self.plugin_files_name_py: list[str] = []  # 储存着Plugin目录下的文件名
        self.plugin_filename_option_name_map: Dict[str, str] = {}  # 选项名和实际文件名的映射表
        self.loaded_plugin: Dict[str] = {}  # 存放加载完毕的插件对象 键值对：ID-读取的插件对象

    def init_plugin_singer_file(self, plugin_files_name_py):
        """
        导入指定单文件插件
        :param plugin_files_name_py: 插件文件名列表，如[1.py,2.py,3.py]
        :return: None
        """

        def remove_file_suffix(file_name: str):
            return file_name.split(".")[0]

        plugin_files_name = map(remove_file_suffix, plugin_files_name_py)
        logging.debug(f"去掉.py后缀的文件名 {plugin_files_name}")
        for name in plugin_files_name:
            self.loaded_plugin[name] = importlib.import_module(f'.{name}', package='Plugin')
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            logging.debug(name)
            try:
                # self.can_choose_number.append(
                #     self.loaded_plugin[name].PLUGIN_METADATA['option_name'])  # 读取模块元数据，添加gui选项
                self.plugin_filename_option_name_map[self.loaded_plugin[name].PLUGIN_METADATA['option_name']] = \
                    self.loaded_plugin[name].PLUGIN_METADATA['id']
            except Exception as e:
                logging.debug(f'init_plugin_singer_file inside Exception:{e}')

    def init_plugin_folder(self, plugin_files_name):
        """
        导入指定文件夹插件
        :param plugin_files_name: 文件夹插件名列表，如["a","b","c"]
        :return: None
        """
        logging.debug(f"读取到的文件夹插件:{plugin_files_name}")
        for name in plugin_files_name:
            self.loaded_plugin[name] = importlib.import_module(f'.{name}.__init__', package='Plugin')
            # self.i = importlib.import_module('.' + str(name), package='Plugin')  # 相对导入
            logging.debug(name)
            try:
                # self.can_choose_number.append(
                #     self.loaded_plugin[name].PLUGIN_METADATA['option_name'])  # 读取模块元数据，添加gui选项
                self.plugin_filename_option_name_map[self.loaded_plugin[name].PLUGIN_METADATA['option_name']] = \
                    self.loaded_plugin[name].PLUGIN_METADATA['id']
            except Exception as e:
                logging.debug(f'init_plugin_folder inside Exception:{e}')

    def readPlugin(self, path):
        """
        读取指定目录下插件需重构
        :param path: 指定的目录 绝对路径
        :return: None
        """
        for root, _dir, file in os.walk(path):
            self.plugin_files_and_folder_name.append(file)
            root_list = str(root).split("\\")
            if root_list[-2] == 'Plugin':
                if '__init__.py' in file:
                    self.plugin_files_name_folder.append(root_list[-1])

    def init_plugin(self):
        """
        导入插件
        :return: 读取到的插件的option_name字段列表,插件的option_name字段和id字段的键值对,插件的id字段和加载的插件对象的键值对
        """
        self.readPlugin(self.PLUGIN_DIR_PATH)  # 读目录获取文件名

        try:  # 从所有读取的文件中挑选出.py为后缀的文件
            for i_list in self.plugin_files_and_folder_name:
                if (i_list[0].split("."))[-1] == "py":
                    if not self.plugin_files_name_py:  # 第一遍空列表才写入
                        self.plugin_files_name_py = i_list
        # 这行bug很多，小心
        except Exception as e:
            logging.debug("挑选单文件插件名时出现问题" + str(e))

        try:
            self.init_plugin_singer_file(self.plugin_files_name_py)  # 导入单文件插件
        except Exception as e:
            logging.debug(f'init_plugin_singer_file outside Exception:{e}')

        try:
            self.init_plugin_folder(self.plugin_files_name_folder)  # 导入文件插件
        except Exception as e:
            logging.debug(f'init_plugin_folder outside Exception:{e}')

        return self.plugin_filename_option_name_map, self.loaded_plugin
