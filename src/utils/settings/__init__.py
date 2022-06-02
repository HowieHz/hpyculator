"""统一管理，操作设置文件"""
from .settings_file_manager import SettingsManager

instance_settings_manager = SettingsManager()
instance_settings_file = instance_settings_manager.load()  # 单例
