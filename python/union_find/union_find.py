class UnionFind:
    '''正常的并查集
    均衡时间复杂度的查操作和并操作
    '''
    root = dict()
    count = 0

    def __init__(self, init_list=[]):
        '''初始化并查集
        字典的键为元素值，字典的值为此元素值的父节点(初始为自己)
        '''
        self.count = len(init_list)
        for i in init_list:
            self.root[i] = i

    def find(self, key):
        '''查询这个值的顶级父节点的值(也就是组号)
        先判断传入的值是否超出范围；
        再循环判断键和值是否相同，不相同则向上循环，直到查询到键值相同的元素，返回键值；

        Agre:
            key: 键
        return:
            None 或键值
        '''
        if key < 0 or key >= self.count:
            return None
        while self.root[key] != key:
            key = self.root[key]
        return key

    def isConnected(self, p, q):
        '''判断两个键是否连接
        只需判断两个键的顶级父节点是否相同；

        Agre:
            p: 键
            q: 键
        return:
            bool
        '''
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        '''并集操作，将两个键连接
        先查询出两个键的顶级父节点；
        如果这两个顶级父节点相同，则已经这两个键就已经是连接状态了，不做任何操作；
        如果这两个顶级父节点不同，则将一个顶级父节点指向另一个顶级父节点；

        Agre:
            p: 键
            q: 键
        '''
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self.root[p_root] = q_root


if __name__ == "__main__":
    init_list = []
    list_len = 10
    for i in range(10, 10 + list_len):
        init_list.append(i)

    print(init_list)
    fund = UnionFind(init_list)

    print(fund.root)
    fund.unionElements(12, 13)
    fund.unionElements(13, 14)
    fund.unionElements(10, 14)
    fund.unionElements(17, 13)
    print(fund.root)
    print(fund.isConnected(12, 13))
