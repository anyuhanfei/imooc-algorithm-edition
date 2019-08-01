class UnionFindRank:
    '''并查集优化方案二
    创建rank字典来记录根节点的层级
    '''
    root = dict()
    rank = dict()
    count = 0

    def __init__(self, init_list=[]):
        '''初始化
        字典的键为元素值，字典的值为此元素值的父节点；
        所有节点都是根节点，层级记录为1
        '''
        self.count = len(init_list)
        for i in init_list:
            self.root[i] = i
            self.rank[i] = 1

    def find(self, key):
        '''查操作'''
        if key < 0 and key >= self.count:
            return None
        while self.root[key] != key:
            key = self.root[key]
        return key

    def isConnected(self, p, q):
        '''判断两键值是否连接'''
        return self.root[p] == self.root[q]

    def unionElements(self, p, q):
        '''并操作
        查询两键值的顶级父节点，如果相同则不操作；
        判断两键值的顶级父节点的层级，层级少的指向层级多的(层级多的做顶级节点)，如果层级相同，则任意指向，并且被指向的节点层级加一
        '''
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.rank[p_root] == self.rank[q_root]:
            self.root[p_root] = q_root
            self.rank[q_root] += 1
        elif self.rank[p_root] < self.rank[q_root]:
            self.root[p_root] = q_root
        elif self.rank[p_root] > self.rank[q_root]:
            self.root[q_root] = p_root


if __name__ == "__main__":
    init_list = []
    list_len = 5
    for i in range(0, list_len):
        init_list.append(i)

    print(init_list)
    fund = UnionFindRank(init_list)

    print(fund.root)
    print(fund.rank)
    fund.unionElements(2, 3)
    fund.unionElements(3, 4)
    fund.unionElements(4, 0)
    print(fund.root)
    print(fund.rank)
