创建核心实例
=============================================
首先确保你安装了 ``hpyc_core`` 模块

.. code-block:: bash

    pip install hpyc_core

接下来创建核心实例

.. code-block:: python

    from hpyc_core import Core
    instance_core = Core(output_dir_path: Optional[str] = None,  # 输出目录
                        settings_dir_path: Optional[str] = None,  # 设置文件所在目录
                        plugins_dir_path: Optional[str] = None,  # 插件存放目录
                        settings_file_name: str = "hpyculator_setting",  # 设置文件名
                        settings_file_format: str = "json",)  # 设置文件格式

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