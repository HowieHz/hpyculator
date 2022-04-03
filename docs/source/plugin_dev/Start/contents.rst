开始
================

0.读完文档

1.创建一个.py文件

2.文件开头写元数据

3.根据output_mode，进行不同的开发（这几种模式的不同，详情请见"output_mode参数讲解"）

        3.(1)当output_mode为0-2时，写一个main()函数，这个函数的return值会作为输出值和保存值

        3.(2)当output_mode为3时，

            将以下代码，复制到你的插件文件里(以下函数的使用，详情请见“函数”一节)

            .. code-block:: python

                def write(file,anything,end="\n"):
                    file.write(str(anything)+end)
                    file.flush()

                def write_without_flush(file,anything,end="\n"):
                    file.write(str(anything)+end)

                def flush(file):
                    file.flush()

                def output(self,anything,end="\n"):
                    self.output.AppendText(str(anything)+end)

            然后写main()函数用于计算并且输入到内框，main_save()函数用于计算并保存

        3.(3)当output_mode为4时，

            和数值为3的时候的步骤一样，但是会多传入一个参数说明是否保存，详情请见"主程序调用插件的方式（调用时的输入值）"