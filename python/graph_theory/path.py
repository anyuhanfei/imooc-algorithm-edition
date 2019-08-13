'''通过深度优先遍历来得到两个节点之间的路径（不一定是最短的）'''

'''
深度优先遍历的其他应用：
    查看图中的环
'''


class Path:
    graph = None
    visited = dict()
    froms = dict()
    s = None

    def __init__(self, graph, s):
        self.graph = graph
        for i in self.graph.vecctor.keys():
            self.visited[i] = False
            self.froms[i] = -1
        assert s in self.visited.keys()
        self.s = s
        self._dfs(s)

    def _dfs(self, key):
        self.visited[key] = True
        for i in self.graph.getEdge(key):
            if self.visited[i] is False:
                self.froms[i] = key
                self._dfs(i)

    def hasPath(self, w):
        assert w in self.visited.keys()
        return self.visited[w]

    def path(self, w):
        assert w in self.visited.keys()
        vec = []
        while self.froms[w] != -1:
            w = self.froms[w]
            vec.append(w)
        vec.reverse()
        return vec

    def showPath(self, w):
        vec = self.path(w)
        print(self.s, end=" ")
        print('↓', end=" ")
        for i in vec:
            print('↓', end=" ")
            print(i, end=" ")
        print(w)
