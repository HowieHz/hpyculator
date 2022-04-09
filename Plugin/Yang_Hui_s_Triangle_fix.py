import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode' : '1',#输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)（必须）
    'id' : 'Yang_Hui_s_Triangle_fix',#ID,插件标识符,需要和文件名一致（必须）
    'option_name' : "杨辉三角_fixV1.0.1 by HowieHz",#选项名-在选择算法列表中（必须）
    'version' : 'V1.0.1',#版本号（必须）

    'save_name' : "杨辉三角前",#文件保存项目名-在输出（必须）
    'quantifier' : "行",#文件保存量词-在输入后面(可选)

    'output_start' : "",#输出头(可选)
    'output_name' : "杨辉三角", #选择此项后输出的名字（必须）
    'author' : "HowieHz",#作者(可选)
    'help' : """
    输入数字n ，输出前n行杨辉三角
            """,#帮助和说明(可选)
    'output_end' : "",#输出小尾巴(可选)

    'output_mode' : '3',
    # 调用类main的return形式，
    # 0为返回一次（适用于return字符串等情况），
    # 1为返回多次（适用于return列表等情况），
    # 2为返回多次（适用于return列表等情况，和1相似，但是每次输出不换行）,
    # （推荐）3无return返回值，要求插件作者放置保存和输出（性能最好，推荐使用，默认值）（要求模块自己写好保存和返回，计算调用main函数，保存调用main_save函数），
    # 4和三类似，但是只会调用main，且会传入第三个参数，第三个参数为'save'时表示为要输出到内屏，第三个参数为'output'时表示要保存
    'save_mode' : '0' ,#保存名的形式，0为 时间+算法名+输入+量词  1为 时间+输入+“的”+算法名（必须）
                                #回文质数第5项(第1-5项)   51,12,31,45的方差（未加入特性）
                                #如果是1，则self.quantifier无效化
    "fullwidth_symbol" : '1' #懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}

def main(num,self):#返回一个列表
    if num <=3000:
        if num == 0:
            return []
        l1 = [[1]]
        n = 1
        while n < num:
            l1.append(list(map(lambda x, y: x + y, [0] + l1[-1], l1[-1] + [0])))
            n += 1
        for i in l1:
            hpyc.output(self,i)
    else:
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
    if num <= 3000:
        if num == 0:
            hpyc.write(file,[])
        l1 = [[1]]
        n = 1
        while n < num:
            l1.append(list(map(lambda x, y: x + y, [0] + l1[-1], l1[-1] + [0])))
            n += 1
        for i in l1:
            hpyc.write_without_flush(file,i)
        hpyc.flush(file)
        l1=None
        return
    else:
        need_write = []
        need_write_len = 0
        for i in range(0,num):
            need_write.append(GetTriangleRow(i))
            need_write_len += 1
            if need_write_len >= 3000:
                for write_i in need_write:
                    hpyc.write_without_flush(file, write_i)
                hpyc.flush(file)
                need_write = []
                need_write_len = 0
        for write_i in need_write:
            hpyc.write(file, write_i)
        need_write = None
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