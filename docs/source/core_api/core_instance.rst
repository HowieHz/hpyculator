创建核心实例
=============================================
.. code-block:: python

    class Core:
        def __init__(
            self,
            output_dir_path: Optional[str] = None,
            settings_dir_path: Optional[str] = None,
            plugins_dir_path: Optional[str] = None,
            settings_file_name: str = "hpyculator_setting",
            settings_file_format: str = "json",
        ) -> None:
            """核心实例

            :param output_dir_path: 输出目录
            :param settings_dir_path: 设置文件目录
            :param plugins_dir_path: 插件存放目录
            :param settings_file_name: 设置文件名
            :param settings_file_format: 设置文件格式
            """

创建核心实例

.. list-table:: 选取顺序： 输入 > 设置文件 > 默认值!
  :widths: 20 20 45 20
  :header-rows: 1

  * - 参数
    - 设置文件中对应键
    - 默认值
    - 数据要求
  * - output_dir_path
    - "output_dir_path"
    - str(os.path.join(os.getcwd(), "Output"))
    - 字符串类型
  * - settings_dir_path
    - 无
    - str(os.path.join(os.getcwd(), "Settings"))
    - 字符串类型
  * - plugins_dir_path
    - "plugins_dir_path"
    - str(os.path.join(os.getcwd(), "Plugin"))
    - 字符串类型
  * - settings_file_name
    - 无
    - "hpyculator_setting"
    - 字符串类型
  * - settings_file_format
    - 无
    - "json"
    - "json" | "yaml" | "toml"