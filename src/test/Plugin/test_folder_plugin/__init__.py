from hpyculator import hpycore as hpyc

PLUGIN_METADATA = {
    'input_mode': hpyc.STRING,
    'id': 'test_folder_plugin',  # ID,插件标识符
    'option_name': "test_folder_pluginV1.0.0 by HowieHz",  # 选项名-在选择算法列表中
    'version': 'V1.0.0',  # 版本号
    'save_name': "test_folder_plugin",  # 文件保存项目名-在输出
    'quantifier': "quantifier",  # 文件保存量词-在输入后面
    'output_start': "output_start",  # 输出头
    'output_name': "test_folder_plugin",
    'author': "HowieHz",
    'help': "help",
    'output_end': "output_end",
    'return_mode': hpyc.NO_RETURN,
    'use_quantifier': hpyc.ON
}


def on_calculate(data):
    return data


def on_calculate_with_save(data):
    return data
