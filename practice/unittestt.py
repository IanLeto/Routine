# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 10:01
# @Author  : Aries
# @Site    :
# @File    : unittestt.py
# @Software: PyCharm

import unittest
from practice import betested


a = betested.beTest()
# print(a.func_tobe_tested())
class TestFunc(unittest.TestCase):

    def test_func(self):

        self.assertEqual(3, a.func_tobe_tested())


if __name__ == '__main__':
    unittest.main(module=None)
    print(a.list1)
