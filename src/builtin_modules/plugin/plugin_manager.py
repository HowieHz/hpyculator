import os
import sys
import importlib
import hpyculator as hpyc
from typing import List, Dict

# 这样才可以导入上层包哈哈
sys.path.append(os.path.join(sys.path[0], ".."))


class PluginManager:
    def __init__(self):
        # 载入模块
        # Plugin目录下读取到的文件夹和文件
        self.plugin_files_and_folder_name: List[list] = []
        # Plugin目录下读取到的有__init__.py的文件夹
        self.plugin_files_name_folder: List[str] = []
        self.plugin_option_id_dict: Dict[str, str] = {}  # 选项名和实际文件名(ID)的映射表
        self.loaded_plugin: Dict[str] = {}  # 存放加载完毕的插件对象 键值对：ID-读取的插件对象

    def __init_plugin_singer_file(self, plugin_files_name):
        """
        导入指定单文件插件

        :param plugin_files_name: 插件文件名列表，如[aasd,2asd,31qq]
        :return: None
        """
        # print(f"去掉.py后缀的文件名 {list(plugin_files_name)}")
        for name in plugin_files_name:
            if name:  # 跳过空位
                try:
                    self.loaded_plugin[name] = importlib.import_module(f"Plugin.{name}")
                    self.plugin_option_id_dict[
                        self.loaded_plugin[name].PLUGIN_METADATA["option_name"]
                    ] = self.loaded_plugin[name].PLUGIN_METADATA["id"]  # 读取模块元数据，添加gui选项
                except ImportError as e:
                    print(f"init_plugin_singer_file inside Exception:{str(e)}")
                except Exception as e:
                    print(f"init_plugin_singer_file inside Exception:{str(e)}")

    def __init_plugin_folder(self, plugin_files_name):
        """
        导入指定文件夹插件

        :param plugin_files_name: 文件夹插件名列表，如["a","b","c"]
        :return: None
        """
        # print(f"读取到的文件夹插件:{plugin_files_name}")
        for name in plugin_files_name:
            self.loaded_plugin[name] = importlib.import_module(f".{name}.__init__", package="Plugin")
            try:
                self.plugin_option_id_dict[
                    self.loaded_plugin[name].PLUGIN_METADATA["option_name"]
                ] = self.loaded_plugin[name].PLUGIN_METADATA["id"]  # 读取模块元数据，添加gui选项
            except ImportError as e:
                print(f"init_plugin_folder inside Exception:{str(e)}")
            except Exception as e:
                print(f"init_plugin_folder inside Exception:{str(e)}")

    def initPlugin(self, path, plugin_suffix=".py"):
        """
        导入插件

        :param path: 插件目录路径
        :param plugin_suffix: 插件后缀
        :return: [dict]{插件id字段,对应的插件对象}
        """
        # 读取该目录下的的文件和文件夹
        things_in_plugin_dir = os.listdir(path)

        # 从所有读取的文件和文件夹中挑选出.py为后缀的文件
        files_in_plugin_dir = map(
            lambda file_name: file_name.split(".")[0] if file_name.endswith(plugin_suffix) else "",
            things_in_plugin_dir)
        # 去除空值
        files_in_plugin_dir = [_ for _ in files_in_plugin_dir if _ != ""]

        # 从所有读取的文件和文件夹中挑选出文件夹
        dirs_in_plugin_dir = map(
            lambda file_name: file_name if os.path.isdir(os.path.join(path,file_name)) and os.path.isfile(os.path.join(path,file_name,"__init__.py")) else "",
            things_in_plugin_dir)
        #去除空值
        dirs_in_plugin_dir = [_ for _ in dirs_in_plugin_dir if _ != ""]

        try:
            self.__init_plugin_singer_file(files_in_plugin_dir)  # 导入单文件插件
        except Exception as e:
            print(f"init_plugin_singer_file outside Exception:{e}")

        try:
            self.__init_plugin_folder(dirs_in_plugin_dir)  # 导入文件插件
        except Exception as e:
            print(f"init_plugin_folder outside Exception:{e}")

        return None

    def getPluginAttribute(self, user_selection_id):
        """
        读取指定id的插件属性

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
        """
        获取指定id的插件对象

        :param user_selection_id:
        :return: A instance of plugin
        """
        return self.loaded_plugin[user_selection_id]

    def getOptionIdDict(self):
        """
        获取插件选项名和id的映射表

        :return: A Dict [Option to Id]
        """
        return self.plugin_option_id_dict
