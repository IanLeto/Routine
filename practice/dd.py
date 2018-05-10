
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 22:17
# @Author  : Ian Leto
# @Site    :
# @File    : dd.py
# @Software: PyCharm


deadline = 12 + 3


def when_should_I_leave(cost_per_month=4000):
    leave_month = 0
    while 1 == 1:
        if (deadline - leave_month) * \
                cost_per_month < 8000 + (leave_month - 5) * 5000:
            break
        else:
            leave_month += 1

    print('%s月辞职,准备简历' % leave_month)
    print('%s月投奔酱腿' % (leave_month +1))


when_should_I_leave(3200)
