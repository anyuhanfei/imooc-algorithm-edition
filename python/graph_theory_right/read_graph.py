from dense_graph import DenseGraph
from sparse_graph import SparseGraph
import minimum_span_tree


class ReadGraph:
    '''读取文件,创建一个图'''
    def __init__(self, graph_type, file_name):
        one = 1
        with open(file_name, 'r') as f:
            for line in f:
                a, b, weight = line.split(' ')
                if one == 1:
                    init_list = [i for i in range(0, int(a) + 1)]
                    self.graph = DenseGraph(init_list) if graph_type == 'dense' else SparseGraph(init_list)
                else:
                    self.graph.addEdge(int(a), int(b), float(weight))
                one += 1

    def get_graph(self):
        return self.graph

    def print_all_edge(self):
        print(self.graph.getAllEdge())


if __name__ == "__main__":
    rgs = ReadGraph('dense', './python/graph_theory_right/testG1.txt')
    rgs.print_all_edge()
    m = minimum_span_tree.LazyPrim(rgs.get_graph())
    for i in m.mstEdges():
        print(i.ostream())
    print(m.result())
