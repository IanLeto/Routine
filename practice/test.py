from practice import time_usage

time_ian = time_usage.IanTime()

print(time_ian.str_to_datetime_with_time('2018-9-21 18:13:19'))
print(time_ian.str_to_datetime_without_time('2018-9-21'))
today = time_ian.get_today()


