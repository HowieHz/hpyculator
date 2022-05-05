import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': hpyc.STRING,
    'id': 'Statistics',
    'option_name': "平均数,众数,中位数,方差,标准差V1.1.0 by HowieHz",
    'version': 'V1.1.0',

    'save_name': "平均数,众数,中位数,方差,标准差",
    'quantifier': "",

    'output_start': "",
    'output_name': "平均数,众数,中位数,方差,标准差计算",
    'author': "HowieHz",
    'help': """
    输入若干个数字，以此来计算这些数字的 平均数,众数,中位数,方差,标准差
    
    输入格式:
    A,B,C,...
    （用半角逗号隔开的实数）
""",

    'output_end': "",

    'return_mode': hpyc.RETURN_ONCE,
    'use_quantifier': hpyc.ON,
    "fullwidth_symbol": hpyc.OFF
}


def on_calculate(num):
    num = str(num).split(",")  # 过滤输入框的数字并且将结果储存

    list_data = []
    for i in num:
        list_data.append(float(i))

    list_data.sort()
    allnumbers = 0
    for i in list_data:
        allnumbers = allnumbers + i

    pjs = "该数组的平均数是" + str(allnumbers / len(list_data))
    dict_data = {}
    for times in list_data:
        dict_data.update({times: list_data.count(times)})
    max_timesnumber = max(zip(dict_data.keys()))
    max_times = max(zip(dict_data.values()))

    zj = "该数组的众数是" + str(max_timesnumber)[1:-2] + ",该数出现次数为" + str(max_times)[1:-2]

    if int(len(list_data) / 2) == len(list_data) / 2:  # 检验列表长是否为偶数
        zws = "该数组的中位数是" + str((list_data[len(list_data) // 2] + list_data[len(list_data) // 2 - 1]) / 2)  # 是偶数
    else:
        zws = "该数组的中位数是" + str(list_data[((len(list_data) + 1) // 2) - 1])  # 不是偶数，去

    fcall = 0
    for i2 in list_data:
        fcall = fcall + (abs(i2 - allnumbers / len(list_data)) ** 2)
    fc = "该数组的方差是" + str(fcall / len(list_data))

    bzc = "该数组的标准差是" + str(int(fcall / len(list_data)) ** 0.5)

    last = pjs + "\n" + zj + "\n" + zws + "\n" + fc + "\n" + bzc

    return last
