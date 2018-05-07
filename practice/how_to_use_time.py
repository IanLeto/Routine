

from datetime import datetime, date, time, timedelta


class Learn_how_to_use_time():

    '''
        调用构造函数,创建三个时间对象

    '''
    Ian_time = time(19, 12, 10)
    Ian_date = date(2018, 5, 7)
    Ian_datetime = datetime(2018, 5, 7, 19, 12, 10)
    date_str = '2018-5-7'
    time_str = '19:12:10'
    '''
        时间对象=> str
    '''

    def class_to_str(self):
        self.Ian_time = self.Ian_time.strftime('%H:%M:%S')
        self.Ian_date = self.Ian_date.strftime('%Y-%m-%d')
        self.Ian_datetime = self.Ian_datetime.strftime('%Y-%m-%d %H:%M:%S')

    '''
        str => 对象
    '''

    def str_to_class(self):
        self.date_str = datetime.strptime(self.date_str, '%Y-%m-%d')
        self.time_str = datetime.strptime(self.time_str, '%H:%M:%S')

    '''
        日期 运算 
    '''

    def add_date(self):
        res = date(2013,10,2) + timedelta(days=10)
        return date(2013,10,2).strftime('%Y-%m-%d'), res.strftime('%Y-%m-%d')







user = Learn_how_to_use_time()
print(type(user.Ian_date), user.Ian_time, user.Ian_datetime)
user.class_to_str()
print(type(user.Ian_date), user.Ian_time, user.Ian_datetime)
user.str_to_class()
print(type(user.date_str), user.time_str)
print(user.add_date())
