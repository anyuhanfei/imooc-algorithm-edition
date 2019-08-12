from dense_graph import DenseGraph
from sparse_graph import SparseGraph


class ReadGraph:
    '''读取文件,创建一个图'''
    def __init__(self, graph_type, file_name):
        one = 1
        with open(file_name, 'r') as f:
            for line in f:
                a, b = line.split(' ')
                if one == 1:
                    init_list = [i for i in range(0, int(a) + 1)]
                    self.graph = DenseGraph(init_list) if graph_type == 'dense' else SparseGraph(init_list)
                else:
                    self.graph.addEdge(int(a), int(b))
                one += 1
        print(self.graph.getAllEdge())


if __name__ == "__main__":
    rgs = ReadGraph('sparse', 'D:\\project\\imooc-algorithm-edition-master\\python\\graph_theory\\testG1.txt')
    rgd = ReadGraph('dense', 'D:\\project\\imooc-algorithm-edition-master\\python\\graph_theory\\testG1.txt')
