数据结构
==================
可通过 ``from hpyc_core.data_structure import 结构名`` 来获取对应结构


MetadataDict
---------------
插件元数据规定

通过 ``getPluginMetadata`` 获取到的数据类型

.. code-block:: python

    class MetadataDict(TypedDict, total=False):
        """插件元数据数据类型"""

        input_mode: int
        id: str
        option: str
        version: str
        tag: list | str
        save_name: str
        quantifier: str
        output_start: str
        output_name: str
        author: str | list
        help: str
        output_end: str
        return_mode: int
        fullwidth_symbol: int