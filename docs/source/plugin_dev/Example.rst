插件参考（写法参考）
======================

以下是 单文件插件 ， 文件夹插件的__init__.py文件 的示例

使用时请替换掉[]的内容

并且完成 ``main`` 和 ``main_save`` 函数

可选项： ``main_test`` 函数用于测试性能，无需输出和保存

.. code-block:: python

    PLUGIN_METADATA = {
        'input_mode' : '[]',#输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)
        'id' : '[文件名]',#ID，插件标识符，需要和文件名一致
        'option_name' : "[算法名][版本号(推荐语义化版本)] by [作者名]",#选项名-在选择算法列表中
        'version' : '[版本号(推荐语义化版本)]',#版本号

        'save_name' : "[]",#文件保存项目名-在输出
        'quantifier' : "[]",#文件保存量词-在输入后面(可选)

        'output_start' : "",#输出头(可选)
        'output_name' : "[算法名]", #选择此项后输出的名字
        'author' : "[作者名]",#作者(可选)
        'help' : """
            【帮助内容】
                    """,#帮助和说明(可选)
        'output_end' : "",#输出小尾巴(可选)

        'output_mode' : '3',
        # 具体说明和区别请看“output_mode参数讲解”一节
        # 调用类main的return形式，
        # 0为返回一次（适用于return字符串等情况），
        # 1为返回多次（适用于return列表等情况），
        # 2为返回多次（适用于return列表等情况，和1相似，但是每次输出不换行）,
        # （推荐）3无return返回值，要求插件作者放置保存和输出（性能最好，推荐使用，默认值）（要求插件作者自己写好保存和返回，计算调用main函数，保存调用main_save函数），
        # 4和三类似，但是只会调用main，且会传入第三个参数，第三个参数为'save'时表示为要输出到内屏，第三个参数为'output'时表示要保存
        'save_mode' : '0' ,#保存名的形式，0为 时间+算法名+输入+量词  1为 时间+输入+“的”+算法名
                                        #如果是1，则self.quantifier无效化
        "fullwidth_symbol" : '0' #懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
        }

    import wx

    def write(file,anything,end="\n"):#写入数据到硬盘
        file.write(str(anything)+end)
        file.flush()

    def write_without_flush(file,anything,end="\n"):#写入数据到内存
        file.write(str(anything)+end)

    def flush(file):#写入内存中的数据到硬盘
        file.flush()

    def output(self,anything,end="\n"):#输出到框体内
        wx.CallAfter(self.outPutToOutPut,self,str(anything)+end)

    def outPutToOutPut(self, msg:str):
        self.output.AppendText(msg)

    def clearOutPut(self):
        self.output.Clear()

    def setOutPut(self, msg:str):
        self.output.SetValue(msg)
        
    def main(input,self):#输出到框体内
        pass
        
    def main_save(input,file):#保存到文件
        pass

    #def main_test(input,file):#测试函数，无需输出和保存,如果不写这个函数请注释掉
        #pass
            



以下.py文件均代指 `内置插件 <https://github.com/HowieHz/hpyculator/tree/main/Plugin>`_

test9_one.py
    是test9系列中内存开销最大，时间开销最小的方案，
    虽然这里用的是outputmode3，其实和outputmode1是一致的，
    用outputmode1的等价写法已经注释在插件文件主函数下面

test9_n.py
    是test9系列中内存开销最小，时间开销最大的方案，
    使用了write函数

test9_fix.py
    是output_mode3的典范，
    在test9系列中内存开销和时间开销中找了一个平衡点，
    使用了write_without_flush和flush函数

Statistics.py
    是output_mode0的典范，
    很好的展示了output_mode0的用处

fibonacci_Sequence.py
    output_mode4的典范，
    很好的展示了output_mode4的插件写法

