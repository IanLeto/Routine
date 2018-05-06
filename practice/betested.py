# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 10:02
# @Author  : Aries
# @Site    :
# @File    : betested.py
# @Software: PyCharm

from practice import socket_Server
class beTest():

    def __init__(self):
        self.list1 = [1, 2, 3]

    def func_tobe_tested(self):
        for i in self.list1:
            i += 1
        return len(self.list1)

def add():
    return 1