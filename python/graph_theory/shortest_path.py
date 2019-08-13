'''通过广度优先遍历来查询到最短路径'''
import queue


class ShortestPath:
    graph = None
    visited = dict()
    froms = dict()
    ords = dict()
    s = None

    def __init__(self, graph, s):
        self.graph = graph
        for i in self.graph.vector.keys():
            self.visited[i] = False
            self.froms[i] = -1
            self.ords[i] = -1
        self.s = s
        # 无向图最短路径算法
        q = queue.Queue()
        q.put(self.s)
        self.visited[self.s] = True
        self.ords[self.s] = 0
        while not q.empty():
            v = q.get()
            for i in self.graph.getEdge(v):
                if self.visited[i] is False:
                    self.visited[i] = True
                    self.froms[i] = v
                    self.ords[i] = self.ords[v] + 1

    def hasPath(self, w):
        assert w in self.visited.keys()
        return self.visited[w]

    def path(self, w):
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

    def graph_length(self, w):
        assert w in self.ords.keys()
        return self.ords[w]gu