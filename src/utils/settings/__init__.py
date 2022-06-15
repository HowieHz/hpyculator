"""统一管理，操作设置文件"""
from hpyculator import hpysettings

instance_settings_file = hpysettings.load(
    settings_file_name="hpyculator_setting", settings_file_format="json"
)  # 单例
