
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
