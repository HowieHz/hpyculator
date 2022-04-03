插件参考（写法参考）
======================

以下.py文件均代指[内置插件](https://github.com/HowieHz/hpyculator/tree/main/Plugin)

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

