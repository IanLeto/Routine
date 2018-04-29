
def static_func_A():
    return 'class_model has been used'


class Invoice:
    '''
        初始化一张发票应该有相应的
        发票id
        发票类型
        发票金额
    '''

    # 这里相当于固有属性
    # 换句话说是常量
    user = 'Ian'
    memo = '写着玩的'

    # 这里的在初始化的时候才会被调用

    def __init__(self, id=0, type='in_invoice', amount=0):
        self.id = id
        self.type = type
        self.amount = amount


class ReceiveStuRequire():

    def __init__(self):
        BaseStu.__init__()


class BaseStu():
    '''
        基础模型,年龄和类型
        information 为请求带入
    '''

    def __init__(self, age=False, type=False, information=None):
        self.age = age
        self.type = type
        self.information = information

    '''
        返回该对象的基本信息
        __class__返回构造self时使用的最底层的类
    '''

    def __str__(self):

        attr_list = [i for i in self.__dict__]

        return '<%s => %s, "属性为:%s">' % (
            self.__class__.__name__, self.__dict__, attr_list)
