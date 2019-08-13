'''深度优先遍历和求连通分量'''


class Component:
    '''
    Agre:
        graph: 图对象
        visited: 图中所有的节点为键，其值初始化为False，遍历后修改为True，表示已遍历过
        ccount: 连通分量
        ids: 图对象中所有的节点为键，其值为连通分量的id号，通常用于判断两个节点是否连接(有相同的连通分量id)
    '''
    graph = None
    visited = dict()
    ccount = 0
    ids = dict()

    def __init__(self, graph):
        '''初始化 visited 和 ids，并进行遍历
        遍历一遍图对象的节点，将节点写入 visited 和 ids 字典中；
        第二遍遍历图对象的节点，如果节点没有遍历过这遍历其连接的节点，然后连通分量加一；
        Agre:
            graph: 图对象
        问题:
            由于在设计图的时候没有设计迭代器来遍历图对象中的节点，只能直接使用图对象中的节点存储对象
        '''
        self.graph = graph
        for i in self.graph.vector.keys():
            self.visited[i] = False
            self.ids[i] = 0
        for o in self.graph.vector.keys():
            if self.visited[o] is False:
                self._dfs(o)
                self.ccount += 1

    def _dfs(self, key):
        '''递归地将连接的节点遍历
        节点已遍历到，修改遍历参数和添加连通分量id号；
        查询与这个节点相联的节点，如果没有被遍历过则进行递归操作；
        Agre:
            key: 节点
        '''
        self.visited[key] = True
        self.ids[key] = self.ccount
        for i in self.graph.getEdge(key):
            if self.visited[i] is False:
                self._dfs(i)

    def count(self):
        '''返回连通分量'''
        return self.ccount

    def isConnected(self, v, w):
        '''判断两个节点是否相连
        通过两个节点的id号是否相同来判断是否相连
        Agre:
            v: 节点
            w: 节点
        return:
            bool
        '''
        assert v in self.ids.keys()
        assert w in self.ids.keys()
        return self.ids[v] == self.ids[w]
