class UnionFindSz:
    '''并查集优化方案一
    创建sz字典来记录根节点的子节点总数
    '''
    root = dict()
    sz = dict()
    count = 0

    def __init__(self, init_list=[]):
        '''初始化
        字典的键为元素值，字典的值为此元素值的父节点；
        所有节点都是根节点，并且无子节点，子节点数统计为1(或0)
        '''
        self.count = len(init_list)
        for i in init_list:
            self.root[i] = i
            self.sz[i] = 1

    def find(self, key):
        '''查操作'''
        if key < 0 and key >= self.count:
            return None
        while self.root[key] != key:
            key = self.root[key]
        return key

    def isConnected(self, p, q):
        '''判断两键值是否连接'''
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        '''并操作
        查询两键值的顶级父节点，如果相同则不操作；
        判断两键值的顶级父节点的子节点数，子节点数少的指向子节点数多的(子节点数多的做顶级节点)，如果子节点数相同，则任意指向；
        注意，并操作后，需要将新加入的子节点数量添加到当前顶级节点上；
        '''
        p_root = self.find(p)
        q_root = self.find(q)
        if q_root == p_root:
            return
        if self.sz[p_root] > self.sz[q_root]:
            self.root[q_root] = self.root[p_root]
            self.sz[p_root] += self.sz[q_root]
        else:
            self.root[p_root] = self.root[q_root]
            self.sz[q_root] += self.sz[p_root]


if __name__ == "__main__":
    init_list = []
    list_len = 5
    for i in range(0, list_len):
        init_list.append(i)

    print(init_list)
    fund = UnionFindSz(init_list)

    print(fund.root)
    fund.unionElements(2, 3)
    fund.unionElements(3, 4)
    fund.unionElements(4, 0)
    print(fund.root)
    print(fund.sz)
