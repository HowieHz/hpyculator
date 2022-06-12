import os
import sys
import importlib
import hpyculator as hpyc
from typing import List, Dict
import traceback

# 这样才可以导入上层包哈哈
sys.path.append(os.path.join(sys.path[0], ".."))


class PluginManager:
    def __init__(self):
        # Plugin目录下读取到的有__init__.py的文件夹
        self._dict_plugin_option_id: Dict[str, str] = {}  # 选项名和实际文件名(ID)的映射表
        # 选项名和实际文件名(ID)的映射表 [([tag1,tag2],name),([tag1,tag2],name)]
        self._list_alL_plugin_tag_option: List[tuple[list[str], str]] = []
        self._dict_loaded_plugin: Dict[str] = {}  # 存放加载完毕的插件对象 键值对：ID-读取的插件对象

    def _loadPluginMetadata(self, name):
        """
        加载插件元数据

        :param name: 插件名
        :return:
        """
        try:
            # PLUGIN_METADATA暂时储存着插件的元数据
            _METADATA = self._dict_loaded_plugin[name].PLUGIN_METADATA
        except AttributeError:  # 比如说缺少PLUGIN_METADATA
            traceback.print_exc()
            return

        try:
            # 读取模块元数据，添加gui选项
            self._dict_plugin_option_id[_METADATA["option"]] = _METADATA["id"]

            tag_list = _METADATA["tag"] if "tag" in _METADATA else []
            tag_list.extend(
                ["author:" + i for i in _METADATA["author"]]
                if isinstance(_METADATA["author"], list)
                else ["author:" + _METADATA["author"]]
            )  # 作者列表或单个作者
            tag_list.extend(
                (f"id:{_METADATA['id']}", f"version:{_METADATA['version']}")
            )  # 版本号，id
            self._list_alL_plugin_tag_option.append(
                (tag_list, _METADATA["option"])
            )  # tag对应选项名
        except KeyError:  # 比如说缺少PLUGIN_METADATA
            traceback.print_exc()
            return
        except Exception as e:
            print(f"init_plugin_folder inside Exception:{str(e)}")
            traceback.print_exc()

    def _initPlugin(self, plugin_files_name, plugin_dirs_name) -> None:
        """
        导入指定单文件插件和文件夹插件

        :param plugin_files_name: 插件文件名列表，如[aasd,2asd,31qq]
        :param plugin_files_name: 文件夹插件名列表，如["a","b","c"]
        :return: None
        """
        # print(f"去掉.py后缀的文件名 {list(plugin_files_name)}")
        for name in plugin_files_name:
            if name:  # 跳过空位，有名字才读取
                try:
                    self._dict_loaded_plugin[name] = importlib.import_module(
                        f"Plugin.{name}"
                    )
                # 插件缺少依赖(ImportError包括ModuleNotFoundError)
                except ModuleNotFoundError:
                    traceback.print_exc()
                    continue
                except ImportError:  # 其他的导入问题
                    traceback.print_exc()
                    continue
                except Exception as e:
                    print(f"init_file_plugin inside Exception:{e}")
                    traceback.print_exc()
                    continue

                self._loadPluginMetadata(name)

        for name in plugin_dirs_name:
            try:
                self._dict_loaded_plugin[name] = importlib.import_module(
                    f".{name}.__init__", package="Plugin"
                )
            # 插件缺少依赖(ImportError包括ModuleNotFoundError)
            except ModuleNotFoundError:
                traceback.print_exc()
                continue
            except ImportError:  # 其他的导入问题
                traceback.print_exc()
                continue
            except Exception as e:
                print(f"init_dir_plugin inside Exception:{e}")
                traceback.print_exc()
                continue

            self._loadPluginMetadata(name)

    def initPlugin(self, path, plugin_suffix=".py") -> None:
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
            lambda file_name: file_name.split(".")[0]
            if file_name.endswith(plugin_suffix)
            else "",
            things_in_plugin_dir,
        )
        # 去除空值
        files_in_plugin_dir = [_ for _ in files_in_plugin_dir if _ != ""]

        # 从所有读取的文件和文件夹中挑选出文件夹
        dirs_in_plugin_dir = map(
            lambda file_name: file_name
            if os.path.isdir(os.path.join(path, file_name))
            and os.path.isfile(os.path.join(path, file_name, "__init__.py"))
            else "",
            things_in_plugin_dir,
        )
        # 去除空值
        dirs_in_plugin_dir = [_ for _ in dirs_in_plugin_dir if _ != ""]

        self._initPlugin(files_in_plugin_dir, dirs_in_plugin_dir)  # 导入单文件插件和文件夹插件

    def getPluginAttributes(self, user_selection_id) -> dict:
        """
        读取指定id的插件属性

        :param user_selection_id: 插件的id
        :return: [list]attributes of plugin
        """
        _plugin_attributes = {}  # 读取好的属性放在这里

        # PLUGIN_METADATA暂时储存着插件的元数据
        _METADATA = self._dict_loaded_plugin[user_selection_id].PLUGIN_METADATA
        for _metadata_item in [
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
            "version",
            "tag",
        ]:
            _plugin_attributes[_metadata_item] = (
                _METADATA[_metadata_item] if _metadata_item in _METADATA else hpyc.OFF
            )

        if _plugin_attributes["fullwidth_symbol"] == hpyc.ON:  # 处理全角转换
            _plugin_attributes["help"] = (
                _plugin_attributes["help"]
                .replace(",", "，")
                .replace(".", "。")
                .replace("'", "‘")
                .replace('"', "”")
                .replace("(", "（")
                .replace(")", "）")
            )

        return _plugin_attributes

    def getPluginInstance(self, user_selection_id) -> importlib.import_module:
        """
        获取指定id的插件对象

        :param user_selection_id: 插件的id
        :return: A instance of plugin
        """
        return self._dict_loaded_plugin[user_selection_id]

    @property
    def list_alL_plugin_tag_option(self) -> list[tuple[list[str], str]]:
        """
        获取所有插件的tag，tag对应插件选项名

        :return:
        """
        return self._list_alL_plugin_tag_option

    @property
    def option_id_dict(self) -> dict[str, str]:
        """
        获取插件选项名和id的映射表

        :return: A Dict [Option to Id]
        """
        return self._dict_plugin_option_id
