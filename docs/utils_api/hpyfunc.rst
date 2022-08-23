hpyfunc
====================

hpyfunc.flatten
----------------------

.. code-block:: python

    def flatten(sequence: Union[list, tuple]) -> list:
        """将多维数据结构展平为一纬数据结构

        :param sequence: 多维数据结构
        :return: 一纬数据结构
        """

例子
~~~~~~~~~~~~~~

.. code-block:: python

    ret_lst = flatten([[1,2,3],[4,5,6,[7,8,9]]])
    print(ret_lst)

hpyfunc.flatten_layer
-------------------------------

.. code-block:: python

    def flatten_layer(sequence: Union[list, tuple]) -> list:
        """将多维数据结构展平一层

        :param sequence: 多维数据结构
        :return: 展平了一层的一纬数据结构
        """

例子
~~~~~~~~~~~~~~

.. code-block:: python

    ret_lst = flatten_layer([[1,2,3],[4,5,6,[7,8,9]]])
    print(ret_lst)

hpyfunc.flatten_no_recursion
--------------------------------

.. code-block:: python

    def flatten_no_recursion(sequence: Union[list, tuple]) -> Union[list, tuple]:
        """将多维数据结构展平为一纬数据结构(无递归)

        :param sequence: 多维数据结构
        :return: 一纬数据结构
        """

例子
~~~~~~~~~~~~~~

.. code-block:: python

    ret_lst = flatten_no_recursion([[1,2,3],[4,5,6,[7,8,9]]])
    print(ret_lst)

hpyfunc.expand_dims
--------------------------------

.. code-block:: python

    def expand_dims(
        array: Union[ArrayType, list],
        *dims,
        padding_value: Union[str, int, float] = 0
    ):
        """将一纬数据结构提升至多维

        :param array: 一维列表/数组
        :param dims: 各项维度上限 (顺序从最里层向外)
        :param padding_value: 填充值 默认为0
        """

例子
~~~~~~~~~~~~~~

.. code-block:: python

    ret_lst = expand_dims([1, 2, 3, 4], 2, 2)
    assert [[1, 2], [3, 4]] == ret_lst

    ret_lst = hpyfunc.expand_dims([1, 2, 3, 4, 5, 6], 1, 2, 3, padding_value = 1)
    print(ret_lst)

    # 结果 (经过格式化)
    assert ret_lst == [
                        [
                            [1],
                            [2]
                        ],
                        [
                            [3],
                            [4]
                        ],
                        [
                            [5],
                            [6]
                        ]
                    ]

hpyfunc.dont_change_my_code
--------------------------------

灵感来源: https://www.bilibili.com/video/BV1aP41157hu

.. code-block:: python

    def dont_change_my_code(
        fun: Callable,
        sign: str,
        hash_fun: Optional[Callable[[str], Union[int, str]]] = None,
        multisign: bool = False,
    ) -> str:
        """沙雕系列：别修改我的代码！
        使用print为计算出的hash值，未计算出结果则输出-1
        返回值也为计算出的hash值，未计算出结果则输出-1

        :param fun: 不要修改这个函数！
        :param sign: 标识符
        :param hash_fun: 你滴哈希函数，要求hash值范围在 0到(10 * 50 - 1)
        :param multisign: 允许多个标识符
        :return: hash值
        """

例子
~~~~~~~~~~~~~~

第一步

.. code-block:: python

    from hpyculator.hpyfunc import dont_change_my_code, easy_text_hash
    import inspect
    def fun_name_aaa():
        """给组员：你要是改了，有你好果子吃,,,"""
        if not easy_text_hash(inspect.getsource(fun_name_aaa)) == "!!!": # ""里面的是标识符
            print("改了是吧，有你好果子吃")

    dont_change_my_code(fun = fun_name_aaa, sign = "!!!")

得到输出
    283

(注：如输出-1，说明未能计算出结果，请修改代码(如注释增加一个逗号)再次计算)

第二步

将上一步得到的数字，选一个替换掉标识符

以下是最终代码

.. code-block:: python

    from hpyculator.hpyfunc import easy_text_hash
    import inspect
    def fun_name_aaa():
        """给组员：你要是改了，有你好果子吃,,,"""
        if not easy_text_hash(inspect.getsource(fun_name_aaa)) == "283": # ""里面的是标识符
            print("改了是吧，有你好果子吃")

此时如果修改函数，运行fun_name_aaa()，则会输出"改了是吧，有你好果子吃"(除非hash碰撞)
