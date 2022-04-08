import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode' : '1',
    'id' : 'Yang_Hui_s_Triangle_n',
    'option_name' : "杨辉三角_nV1.0.1 by HowieHz",
    'version' : 'V1.0.1',

    'save_name' : "杨辉三角前",
    'quantifier' : "行",

    'output_start' : "",
    'output_name' : "杨辉三角",
    'author' : "HowieHz",
    'help' : """
    输入数字n ，输出前n行杨辉三角
""",

    'output_end' : "",

    'output_mode' : '3',
    'save_mode' : '0' ,
    "fullwidth_symbol" : '1'
}

def main(num,self):#返回一个列表
    if num == 0:
        hpyc.output(self,[])
        return
    if num == 1:
        hpyc.output(self,[1])
        return

    for i in range(0,num):
        hpyc.output(self,GetTriangleRow(i))
    return

def main_save(num,file):#返回一个列表
    if num == 0:
        hpyc.write(file, [])
        return
    if num == 1:
        hpyc.write(file, [1])
        return
    for i in range(0,num):
        hpyc.write(file, GetTriangleRow(i))
    return

#来源,知乎@酸痛鱼
def GetTriangleRow(n):
    size = n + 1
    result = [1] * size

    for cols in range(2, size):
        m = cols // 2
        mid_val = result[m - 1] + result[m]
        for j in range(1, m):
            result[j] = result[cols - j] + result[cols - j - 1]

        result[m] = mid_val

        for j in range(m + 1, cols):
            result[j] = result[cols - j]

    return result

#https://www.zhihu.com/people/coder-the-fish
#https://zhuanlan.zhihu.com/p/105454576