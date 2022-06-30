from typing import TypedDict


class MetadataDict(TypedDict, total=False):
    """插件元数据数据类型"""

    input_mode: str
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
