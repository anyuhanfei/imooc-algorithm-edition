

class DenseGraph:
    '''
    稠密图--邻接矩阵

    n_count: 节点数
    m_count: 连接数
    directed: 是否是有向连接
    vector: 二维字典，邻接矩阵
    '''
    n_count = 0
    m_count = 0
    directed = False
    vector = dict()

    def __init__(self, init_list=[], directed=False):
        '''
        将节点数存储，定义连接有无向；
        嵌套循环定义一个二维字典；
        '''
        self.n_count = len(init_list)
        self.directed = directed
        for i in init_list:
            self.vector[i] = dict()
            for ii in init_list:
                self.vector[i][ii] = False

    def V(self):
        '''返回节点数'''
        return self.n_count

    def E(self):
        '''返回连接数'''
        return self.m_count

    def hasEdge(self, v, w):
        '''判断节点v和节点w是否有连接（v->w）
        '''
        assert v in self.vector.keys()
        assert w in self.vector.keys()
        return self.vector[v][w]

    def addEdge(self, v, w):
        '''添加一个连接'''
        assert v in self.vector.keys()
        assert w in self.vector.keys()
        if self.hasEdge(v, w):
            return
        self.vector[v][w] = True
        if self.directed is False:
            self.vector[w][v] = True
        self.m_count += 1

    def getEdge(self, v):
        assert v in self.vector.keys()
        res_list = []
        for i in self.vector[v].keys():
            if self.vector[v][i] is True:
                res_list.append(self.vector[v][i])

    def getAllEdge(self):
        res_list = dict()
        for i in self.vector.keys():
            res_list[i] = []
            for o in self.vector[i].keys():
                res_list[i].append(o) if self.vector[i][o] is True else False
        return res_list
