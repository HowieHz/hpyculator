SPECIAL_TAGS: tuple[str, ...] = (
    "category:",
    "author:",
    "computer_language:",
    "version:",
    "depend:",
    "id:",
)
SPECIAL_TAGS_TRANSLATOR: dict[str, dict[str, str]] = {
    "zh_CN": {
        "category:": "用途/类别/使用场景：",
        "author:": "作者：",
        "computer_language:": "所用计算机语言：",
        "version:": "版本号：",
        "depend:": "依赖：",
        "id:": "文件名(插件唯一标识符)：",
    },
}
