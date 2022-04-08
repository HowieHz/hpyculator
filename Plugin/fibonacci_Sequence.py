import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode' : '1',
    'id' : 'fibonacci_Sequence',
    'option_name' : "斐波那契数列V1.0.0 by HowieHz",
    'version' : 'V1.0.0',

    'save_name' : "斐波那契数列前",
    'quantifier' : "项",

    'output_start' : "",
    'output_name' : "斐波那契数列计算",
    'author' : "HowieHz",
    'help' : """
    输入数字n，输出斐波那契数列的前n项
""",

    'output_end' : "",

    'output_mode' : '4',
    'save_mode' : '0' ,

    "fullwidth_symbol" : '1'
}

"""主框在选择后的输出
            self.output_start
            self.output_name self.version
            by self.author
            
            使用提示:
            self.help
        
            self.output_end
            """

"""主框在输出后的输出
            本次计算花费了*秒
            在经过self.output_mode对应形式处理之后的输出（选择不保存）
            保存计算结果至文件中···（选择保存）
            计算结果已保存在 保存文件名的完整路径（选择保存）
        
            """

"""保存文件名
            时间 + self.save_name+ str(self.input_box_s_input(指代输入框的输入))+self.quantifier .txt
            """

"""添加的选项
            self.option_name
            """
def main(num,self,do_what):#返回一个列表
    if do_what == "output":
        if num == 0:
            hpyc.output(self,"")
        if num == 1:
            hpyc.output(self,"1")
        if num >= 2:
            hpyc.output(self,"1")
            hpyc.output(self, "1")
        fs1 = 1
        fs2 = 1
        fs3 = 1
        n = 2
        while n < num:
            fs3 = fs1
            fs1 += fs2
            fs2 = fs3
            hpyc.output(self,fs1)
            n += 1
    if do_what == "save":
        if num == 0:
            hpyc.write(self, "")
        if num == 1:
            hpyc.write(self, "1")
        if num >= 2:
            hpyc.write(self, "1")
            hpyc.write(self, "1")
        fs1 = 1
        fs2 = 1
        fs3 = 1
        n = 2
        while n < num:
            fs3 = fs1
            fs1 += fs2
            fs2 = fs3
            hpyc.write(self,fs1)
            n += 1
    else:
        pass