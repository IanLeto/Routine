# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 22:23
# @Author  : Ian Leto
# @Site    :
# @File    : py_dict_usage_lab.py
# @Software: PyCharm

dict((x, (lambda x: x + 2)(x)) for x in range(10))
import functools

