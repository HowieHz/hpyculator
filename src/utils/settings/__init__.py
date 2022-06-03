"""统一管理，操作设置文件"""
from .settings_file_factory import SettingsFactory

instance_settings_factory = SettingsFactory()  # 工厂
instance_settings_file = instance_settings_factory.load(
    settings_file_name="hpyculator_setting", settings_file_format="json"
)  # 单例
