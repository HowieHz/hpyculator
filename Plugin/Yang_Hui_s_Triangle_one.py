import  re

PLUGIN_METADATA = {
    'input_mode' : '1',
    'id' : 'Yang_Hui_s_Triangle_one',
    'option_name' : "杨辉三角_oneV1.0.0 by HowieHz",
    'version' : 'V1.0.0',

    'save_name' : "杨辉三角前",
    'quantifier' : "行",

    'output_start' : "",
    'output_name' : "杨辉三角",
    'author' : "HowieHz",
    'help' : """
    输入数字n ，输出前n行杨辉三角
    one系列使用警告：如果输入过大的数导致内存爆炸，作者概不负责
""",
    'output_end' : "",

    'output_mode' : '1',
    'save_mode' : '0' ,
    "fullwidth_symbol" : '1'
}

def main(num):#返回一个列表
    if num == 0:
        return []
    l1 = [[1]]
    n = 1
    while n < num:
        l1.append(list(map(lambda x, y: x + y, [0] + l1[-1], l1[-1] + [0])))
        n += 1
    return l1
