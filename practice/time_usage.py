import datetime
# from datetime import datetime
# from datetime import time
# from datetime import date

import time


class IanTime():
    '''

        datetime 是顶层的包文件
        里面有三个常用的class
        分别为 date, time, datetime
        date :年月日
        time : 时分秒
        datetime : 年月日 + 十分秒
    '''
    # 日历 年月日构成的
    calendar = datetime.date
    # 年月日 + 具体时间
    cale_time = datetime.datetime
    name = 'ian'

    date_ian = datetime.date
    time_ian = datetime.time
    datetime_ian = datetime.datetime

    def time_type_check(self, *args):
        for type in args:
            if not isinstance(type, (datetime.datetime, datetime.date, datetime.time)):
                return False


    def checkout_str_type(self, *args):
        if not isinstance(args, str):
            print('输入类型必须为str')
            return False
        else:
            return True

    def checkout_datetime_datetime_type(self, *args):
        if not isinstance(args, self.cale_time):
            print('输入类型必须为datetime.datetime:"2018-10-20 20:23:20" ')
            return False
        else:
            return True

    @staticmethod
    def get_today():
        return datetime.date.today()

    def datetime_to_str(self, datetime):
        '''

        :param datetime: 类型为datetime.date类型
        :return: 转换为字符串
        '''
        if not isinstance(datetime, self.calendar):
            print('输入参数为%s类型', self.calendar)
        else:
            return datetime.strftime('%Y-%m-%d %H:%M:%S')

    def str_to_datetime_with_time(self, string):
        '''

        :param string: 类型为 字符串 且有具体时间 2018-9-21 18:13:19
        :return: 转为 datetime.datetime 类型
        '''
        if not isinstance(string, str):
            print('输入参数应为str类型')
        else:
            return self.cale_time.strptime(string, '%Y-%m-%d %H:%M:%S')

    def str_to_datetime_without_time(self, string):
        '''

        :param string: 类型为 字符串 且没有具体时间 "2018-9-21"
        :return: 转为 datetime.datetime 类型
        '''
        if not isinstance(string, str):
            print('输入参数应为str类型')
        else:
            return self.cale_time.strptime(string, '%Y-%m-%d')

    def time_to_ctime(self, time):
        if not isinstance(time, datetime.time):
            print('输入参数为time类型')

    def date_add_date(self, days):
        pass
