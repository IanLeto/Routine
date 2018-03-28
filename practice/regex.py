import re

reg_str = ''  # 要匹配的规则
reg_str = 'end'
res = re.match(reg_str, 'friend')  # 这里是匹配,从字符串的其实位置开始匹配(感觉没啥用)
if res is not None:
    print(res.group())

res = re.search(reg_str, 'friend')  # search 是查找, 就行
if res is not None:  # 在交互模式下,不要加入if条件,但是在实际使用中要加上,否则抛异常
    print(res.group())  # group 返回匹配的对象 or none


'''
    封装search 方法
'''

# 如果函数参数第一个定义了默认值,则第二个不可以是单纯的位置参数??


def search_str(res='', str='', *args):
    res = re.search(res, str)
    if res is not None:
        print(res.group())
    else:
        print('匹配失败')
    if args:
        print('老铁,参数传多了!')


def match_str(res='', str='', *args):
    res = re.match(res, str)
    if res is not None:
        print(res.group())
    else:
        print('匹配失败')
    if args:
        print('老铁,参数传多了!')


# . 相当于额外匹配一个字符(匹配任何的单个字符) 空和\n 不行
#
search_str('.end', 'friend')

'''
    . 的精准匹配
    \ 转义字符
    因为. 是属于特殊字符,如果想要匹配它需要\. 转义
    * $ 这些符号也是如此
'''

str_tested = ['3.14', '3014']
reg_str = '3\.14'  # 可以匹配.
reg_str_not_accurate = '3.14'

search_str(reg_str, str_tested[0])  # none
search_str(reg_str, str_tested[1])  # 3.14

search_str(reg_str_not_accurate, str_tested[0])  # 3.14
# 3014 因为 . 是匹配所有单个字符串,. 也会别匹配出来
search_str(reg_str_not_accurate, str_tested[1])

'''
    字符集匹配
    '啊啊是疯了|xxx'这种不常用(在文本检索 -- spark 等可能会有用)
    '[1][2][as]' 目前更常用一些
'''

# 这里采用match 更加合理一点

reg_str = '[qwer]' * 4

str_tested = ['qwer111', '1ww', 'rqwe', 'eqfa']

match_str(reg_str, str_tested[0])
match_str(reg_str, str_tested[1])
match_str(reg_str, str_tested[2])
match_str(reg_str, str_tested[3])

'''
    () 匹配子组
    又叫获取目标的匹配模式
'''

reg_str = '(\w\w\w)-(\d\d\d)'
str_tested = 'abs-123'

res = re.match(reg_str, str_tested)
if res is not None:
    print(res.group())   # abs-123
    print(res.group(1))  # abs
    print(res.group(2))  # 123
    # print(res.group(3)) 越界
    print(res.groups())  # 'abs', '123')

'''
    \b 单词边界(蛋疼)
    正则这东西,笔记都不好记
'''
print(re.search(r'\bof', 'son of bitch').group())  # 原生字符串
# print(re.search('\bof', 'son of bitch').group())  # /b 变成了转义字符 匹配不到会抛异常
# print(re.search('\bof', 'son ofthe bitch').group())  # /b 变成了转义字符


'''
    findall
    # 注意,将会匹配所用符合条件的内容,
    返回一个list
'''
reg_list = re.findall('car', 'car' * 4)


reg_str = '\bof'
str_tested = 'son of bitch'
search_str('r' + reg_str, str_tested)

'''
    sub() & subn()
    sub(正则,替换成的东西,被替换的字符串)
    process: 将正则应用到字符串的每个字符上,如果匹配,则用替换成的东西来替代它
    
'''
# 把list 中所用的1 都替换成0

reg_str = '1'
reg_list = [str(i) for i in range(1, 11)]  # 将每一个数字装转为字符串
reg_list = ''.join(reg_list)

print(re.sub(reg_str, '0', reg_list))  # 02345678900
print(re.subn(reg_str, '0', reg_list))  # '02345678900', 2)  说明有两个陪替换了

'''
    贪婪模式 尽可能多的去匹配
    非贪婪 尽可能少的去匹配
'''

reg_str = '.*(\d+)'
str_tested = '1223'

print(re.match(reg_str, str_tested).group(1)) # 3 .* 尽可能地匹配到所有的字符,由于\d+ 的存在,所以至少有一个被 \d 给匹配到

reg_str = '.*?(\d+)'

print(re.match(reg_str, str_tested).group(1)) # 3 .* 与上边相反,它会先去查看()里面的合不合适
'''
    尽量非贪婪 re.S 除换行符
'''

