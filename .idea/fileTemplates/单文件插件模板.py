import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode' : hpyc.STRING,#输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
    'id' : '[文件名]',#ID,插件标识符,需要和文件名一致
    'option_name' : "[算法名][版本号(推荐语义化版本)] by [作者名]",#选项名-在选择算法列表中
    'version' : '[版本号(推荐语义化版本)]',#版本号

    'save_name' : "{}",#文件保存项目名-在输出
    'quantifier' : "{}",#文件保存量词-在输入后面(可选)

    'output_start' : "",#输出头(可选)
    'output_name' : "{算法名}", #选择此项后输出的名字
    'author' : "{作者名}",#作者(可选)
    'help' : """
        {帮助内容}
                """,#帮助和说明(可选)
    'output_end' : "",#输出小尾巴(可选)

    'return_mode' : hpyc.NO_RETURN_SINGLE_FUNCTION,
    # 具体说明和区别请看“return_mode参数讲解”一节
    # 调用类main的return形式，
    # hpyc.RETURN_ONCE为返回一次（适用于return字符串等情况），
    # hpyc.RETURN_LIST为将返回的数据迭代输出（适用于return列表等情况），
    # hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE为将返回的数据迭代输出（适用于return列表等情况，和hpyc.RETURN_LIST相似，但是每次输出不换行）,
    # （推荐）hpyc.NO_RETURN无return返回值，要求插件作者放置保存和输出（性能最好，推荐使用，默认值）（要求插件作者自己写好保存和返回，计算调用main函数，
    #         保存调用main_save函数），
    # （推荐）hpyc.NO_RETURN_SINGLE_FUNCTION和三类似，但是只会调用main，且会传入第三个参数，第三个参数为'save'时表示为要输出到内屏，第三个参数为'output'时表示要保存
    'use_quantifier' : hpyc.OFF ,#保存名的形式，OFF为 时间+算法名+输入+量词  ON为 时间+输入+“的”+算法名
                                    #如果是ON，则quantifier无效化
    "fullwidth_symbol" : hpyc.OFF #懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
    }
    
def on_calculate(data,do_what:str):
    pass