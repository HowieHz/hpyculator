from typing import TypedDict, Literal
import hpyculator as hpyc


class MetadataDict(TypedDict, total=False):
    """插件元数据数据类型"""

    input_mode: Literal[hpyc.STRING, hpyc.NUM, hpyc.FLOAT]
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
    return_mode: Literal[
        hpyc.RETURN_ONCE,
        hpyc.RETURN_ITERABLE,
        hpyc.NO_RETURN,
        hpyc.NO_RETURN_SINGLE_FUNCTION,
    ]
    fullwidth_symbol: Literal[hpyc.ON, hpyc.OFF]
