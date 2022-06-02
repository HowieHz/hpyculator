"""统一管理，操作设置文件"""
from .settings_file_manager import SettingsManager

instance_settings_manager = SettingsManager()
instance_settings_file = instance_settings_manager.load(
    settings_file_name="hpyculator_setting", settings_file_format="toml"
)  # 单例
