'''
最小生成树问题
在图中寻找出遍历了所有节点（连接数为节点总数减一），并且权相加值最小的树结构;
通常针对有权无向图，针对连通图;


切分定力（cut property）

把图中的节点切分为两部分，成为一个切分；
如果一个边的两个端点，属于切分后不同的两边，这个边称为横切边（crossing edge）

定理：给定任意切分，横切边中权值最小的边必然属于最小生成树；
'''


class MinHeap:
    '''最小堆'''
    data = []
    count = 0

    def __init__(self):
        self.data.append('-')

    def empty(self):
        return self.count == 0

    def insert(self, value):
        self.data.append(value)
        self.count += 1
        self._shift_up(self.count)

    def extract_min(self):
        if self.count < 1:
            return False
        self.data[self.count], self.data[1] = self.data[1], self.data[self.count]
        self.count -= 1
        self._shift_down(1)
        minimum_number = self.data.pop()
        return minimum_number

    def _shift_down(self, k):
        while True:
            left_down_k = k * 2
            temp_k = left_down_k
            if left_down_k + 1 <= self.count and self.data[left_down_k + 1].wt() < self.data[left_down_k].wt():
                temp_k = left_down_k + 1
            if temp_k > self.count or self.data[temp_k].wt() >= self.data[k].wt():
                break
            self.data[temp_k], self.data[k] = self.data[k], self.data[temp_k]
            k = temp_k

    def _shift_up(self, k):
        up_k = int(k / 2)
        while k > 1 and self.data[up_k].wt() > self.data[k].wt():
            self.data[up_k], self.data[k] = self.data[k], self.data[up_k]
            k = up_k
            up_k = int(k / 2)


class LazyPrim:
    graph = None
    min_heap = MinHeap()
    marked = dict()
    mst = []
    mst_weight = 0

    def __init__(self, graph):
        self.graph = graph
        for i in self.graph.vector.keys():
            self.marked[i] = False
        self._visit(0)
        while self.min_heap.empty() is False:
            temp_mst = self.min_heap.extract_min()
            if self.marked[temp_mst.v()] == self.marked[temp_mst.w()]:
                continue
            self.mst.append(temp_mst)
            self.mst_weight += temp_mst.wt()
            if self.marked[temp_mst.v()] is False:
                self._visit(temp_mst.v())
            else:
                self._visit(temp_mst.w())

    def _visit(self, k):
        assert k in self.marked.keys()
        if self.marked[k] is True:
            return
        self.marked[k] = True
        for i in self.graph.getEdge(k):
            if self.marked[i.other(k)] is False:
                self.min_heap.insert(i)

    def mstEdges(self):
        return self.mst

    def result(self):
        return self.mst_weight
