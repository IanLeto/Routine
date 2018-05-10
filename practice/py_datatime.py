# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 20:19
# @Author  : Ian Leto
# @Site    :
# @File    : py_datatime.py
# @Software: PyCharm
# Python datatime 自用
from datetime import datetime, date, time


class Time_Ian():
    '''
        创建时间对象
       返回的是<时间对象>
    '''

    Ian_date = date(2018, 10, 1)
    Ian_time = time(20, 23, 0)
    Ian_datetime = datetime(2018, 10, 1, 20, 23, 0)

    def class_to_str(self):



user = Time_Ian()
print(type(user.Ian_date), user.Ian_date)
print(user.Ian_time)
print(user.Ian_datetime)
