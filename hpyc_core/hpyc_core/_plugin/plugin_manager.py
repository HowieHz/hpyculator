import importlib
import os
import sys
import traceback
from types import ModuleType
from typing import Any, Generator

import hpyculator as hpyc

from ..data_structure import MetadataDict

# 这样才可以导入上层包哈哈
sys.path.append(os.path.join(sys.path[0], ".."))


class PluginManager:
    def __init__(self):
        # Plugin目录下读取到的有__init__.py的文件夹
        self._dict_plugin_option_id: dict[str, str] = {}  # 选项名和实际文件名(ID)的映射表
        # 选项名和实际文件名(ID)的映射表 [([tag1,tag2],name),([tag1,tag2],name)]
        self._list_alL_plugin_tag_option: tuple[tuple[tuple[str, ...], str], ...] = ()
        self._dict_loaded_plugin: dict[
            str, ModuleType
        ] = {}  # 存放加载完毕的插件对象 键值对：ID-读取的插件对象

    def _loadPluginMetadata(self, name: str) -> None:
        """加载插件元数据

        :param name: 插件名
        :type name: str
        """
        try:
            # PLUGIN_METADATA暂时储存着插件的元数据
            _METADATA: MetadataDict = self._dict_loaded_plugin[name].PLUGIN_METADATA
        except AttributeError:  # 比如说缺少PLUGIN_METADATA
            traceback.print_exc()
            return

        try:
            # 读取模块元数据，添加gui选项
            self._dict_plugin_option_id[_METADATA["option"]] = _METADATA["id"]

            tag_list: tuple[str, ...] = (
                (
                    (
                        (_METADATA["tag"],)  # 是字符串就转换为元组追加
                        if isinstance(_METADATA["tag"], str)  # 是tag列表还是tag字符串
                        else tuple(_METADATA["tag"])  # 是列表就转换为列表追加
                    )
                    if "tag" in _METADATA  # 检查是否有tag这个键
                    else ()  # 没有返回空
                )
                + (
                    tuple(["author:" + i for i in _METADATA["author"]])  # 作者列表转换成元组追加
                    if isinstance(_METADATA["author"], list)  # 是作者名还是作者列表
                    else ("author:" + _METADATA["author"],)  # 作者名转换为元组追加
                )
            ) + (
                f"id:{_METADATA['id']}",  # id
                f"version:{_METADATA['version']}",  # 版本号
            )

            self._list_alL_plugin_tag_option += (
                (
                    tag_list,
                    _METADATA["option"],
                ),
            )  # tag对应选项名
        except KeyError:  # 缺少了一项，因为这些项都是必选项，没就直接return不加载了
            traceback.print_exc()
            return

    def _importPlugin(
        self,
        plugin_files_name: Generator[str, Any, Any],
        plugin_dirs_name: Generator[str, Any, Any],
    ) -> None:
        """导入指定单文件插件和文件夹插件

        :param plugin_files_name: 插件文件名列表，如[asd,2asd,31qq]
        :type plugin_files_name: Generator[str, Any, Any]
        :param plugin_dirs_name: 文件夹插件名列表，如["a","b","c"]
        :type plugin_dirs_name: Generator[str, Any, Any]
        """
        # print(f"去掉.py后缀的文件名 {list(plugin_files_name)}")
        for name in plugin_files_name:
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

            self._loadPluginMetadata(name)

    def initPlugin(self, path: str, plugin_suffix: str = ".py") -> None:
        """导入插件

        :param path: 插件目录路径
        :type path: str
        :param plugin_suffix: 插件后缀, 默认".py"
        :type plugin_suffix: str
        """
        # 读取该目录下的的文件和文件夹
        things_in_plugin_dir = os.listdir(path)

        # 从所有读取的文件和文件夹中挑选出.py为后缀的文件
        files_in_plugin_dir: Generator[str, Any, Any] = (
            name.removesuffix(plugin_suffix)  # 后缀是.py 就提取文件名
            for name in things_in_plugin_dir
            if name.endswith(plugin_suffix)  # 检查文件名后缀是否是.py
        )

        # 从所有读取的文件和文件夹中挑选出文件夹
        dirs_in_plugin_dir: Generator[str, Any, Any] = (
            name
            for name in things_in_plugin_dir
            if (
                os.path.isdir(os.path.join(path, name))
                and os.path.isfile(os.path.join(path, name, "__init__.py"))
            )  # 检查是否是文件夹 检查是否是文件夹内是否有__init__.py文件
        )

        self._importPlugin(files_in_plugin_dir, dirs_in_plugin_dir)  # 导入单文件插件和文件夹插件

    def getPluginMetadata(self, user_selection_id: str) -> MetadataDict:
        """读取指定id的插件属性

        :param user_selection_id: 插件的id
        :type user_selection_id: str
        :return: [list]attributes of plugin
        :rtype: MetadataDict
        """
        _plugin_attributes = {}  # 读取好的属性放在这里

        # PLUGIN_METADATA暂时储存着插件的元数据
        _METADATA = self._dict_loaded_plugin[user_selection_id].PLUGIN_METADATA
        for _metadata_item in (
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
        ):
            _plugin_attributes[_metadata_item] = (
                _METADATA[_metadata_item] if _metadata_item in _METADATA else hpyc.OFF
            )

        if _plugin_attributes["fullwidth_symbol"] == hpyc.ON:  # 处理全角转换
            table = str.maketrans(r""",.'"():""", r"""，。‘“（）：""")
            _plugin_attributes["help"]: str = _plugin_attributes["help"].translate(
                table
            )

        return _plugin_attributes

    def getPluginInstance(self, user_selection_id: str) -> ModuleType:
        """获取指定id的插件对象

        :param user_selection_id: 插件的id
        :type user_selection_id: str
        :return: 插件实例
        :rtype: ModuleType
        """
        return self._dict_loaded_plugin[user_selection_id]

    @property
    def list_alL_plugin_tag_option(self) -> tuple[tuple[tuple[str, ...], str], ...]:
        """获取所有插件的tag，tag对应插件选项名
        [(plugin1_tags: list, plugin1_option), (plugin2_tags: list, plugin2_option)]

        :return: 所有插件的tag以及对应选项名
        :rtype: tuple[tuple[tuple[str, ...], str], ...]
        """
        return self._list_alL_plugin_tag_option

    @property
    def option_id_dict(self) -> dict[str, str]:
        """获取插件选项名和id的映射表

        :return: 选项名映射id的字典
        :rtype: dict[str, str]
        """
        return self._dict_plugin_option_id
