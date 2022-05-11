import logging  # 日志导入
import shelve
import os


class LogManager:
    def __init__(self, setting_file_path):
        self.setting_file_path = setting_file_path

        # 检查存放日志文件的文件夹是否存在
        LOG_FILE_PATH = os.path.join(os.getcwd(), 'Log')
        if os.path.exists(LOG_FILE_PATH):
            pass
        else:
            os.makedirs(LOG_FILE_PATH)

        logging.basicConfig(filename=os.path.join(LOG_FILE_PATH, 'log.txt'),
                            filemode="w",
                            level=logging.DEBUG,
                            format=' %(asctime)s - %(levelname)s - %(message)s')

        #TODO 修复日志不可用，日志现在只有把basicConfig放到main里面才能用

    def checkIsEnableLog(self):
        """
        日志检查

        :return: None
        """

        setting_file_path = self.setting_file_path

        # 读取配置文件-是否保存日志
        with shelve.open(setting_file_path, writeback=True) as setting_file:
            try:
                if setting_file['save_log']:  # 是否保存日志
                    print("日志初始化完成")
                else:
                    logging.disable(logging.CRITICAL)  # 禁用日志
            except Exception as e:
                logging.debug(f"读取save_log时发生错误:{e}")
                setting_file['save_log'] = False  # 默认不保存日志
                logging.disable(logging.CRITICAL)  # 禁用日志
        return None
