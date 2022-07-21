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
