'''
有权图的连接中的存储对象
'''


class Edge:
    '''有权图的连接中存储的对象
    Agre:
        a: 节点
        b: 节点
        weight: 存储数据
    '''
    a = None
    b = None
    weight = None

    def __init__(self, a=None, b=None, weight=None):
        '''初始化数据'''
        self.a = a
        self.b = b
        self.weight = weight

    def set_data(self, a, b, weight):
        '''设置数据'''
        self.a = a
        self.b = b
        self.weight = weight

    def v(self):
        '''返回a节点'''
        return self.a

    def w(self):
        '''返回b节点'''
        return self.b

    def wt(self):
        '''返回权'''
        return self.weight

    def other(self, x):
        '''传入一个节点，返回领一个相连的节点
        Agre:
            x: 节点
        '''
        assert(x == self.a or x == self.b)
        return self.b if x == self.a else self.a

    def ostream(self):
        '''打印此存储数据'''
        return '%s-->%s: %s' % (self.a, self.b, self.weight)
