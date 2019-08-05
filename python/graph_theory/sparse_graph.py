

class SparseGraph:
    '''
    稀疏图--邻接表
    '''
    n_count = 0
    m_count = 0
    directed = False
    vector = dict()

    def __init__(self, init_list=[], directed=False):
        self.n_count = len(init_list)
        self.directed = directed
        for i in init_list:
            self.vector[i] = []

    def V(self):
        '''返回节点数'''
        return self.n_count

    def E(self):
        '''返回连接数'''
        return self.m_count

    def addEdge(self, v, w):
        '''
        问题：
            判断中 v != w 是为了解决自环边；
            这里没有进行平行边的判断，是因为邻接表在判断是否连接时是一个O(n)时间复杂度的方法
        '''
        assert v in self.vector
        assert w in self.vector
        self.vector[v].append(w)
        if v != w and self.directed is False:
            self.vector[w].append(v)
        self.m_count += 1

    def hasEdge(self, v, w):
        assert v in self.vector
        assert w in self.vector
        return bool(self.vector[v].count())

    def updateEdge(self):
        for i in self.vector.keys():
            self.vector[i] = list(set(self.vector[i]))
