class UnionFindPathCompression:
    '''并查集优化三--路径压缩
    在查询时通过子节点来减少层级
    可以与在并操作上进行优化的方法一同使用
    '''
    root = dict()
    count = 0

    def __init__(self, init_list=[]):
        '''初始化
        字典的键为元素值，字典的值为此元素值的父节点；
        '''
        self.count = len(init_list)
        for i in init_list:
            self.root[i] = i

    def find(self, key):
        '''查操作
        判断传入的键值是否超出范围；
        再循环判断键和值是否相同，不相同则向上循环，直到查询到键值相同的元素，返回键值；
        每次循环中，将节点指向自己的父节点的父节点；
        '''
        if key < 0 or key >= self.count:
            return None
        while self.root[key] != key:
            self.root[key] = self.root[self.root[key]]
            key = self.root[key]
        return key

    def isConnected(self, p, q):
        '''判断两键值是否连接'''
        return self.root[p] == self.root[q]

    def unionElements(self, p, q):
        '''并操作，无优化版'''
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self.root[p_root] = q_root


if __name__ == "__main__":
    init_list = []
    list_len = 5
    for i in range(0, list_len):
        init_list.append(i)

    print(init_list)
    fund = UnionFindPathCompression(init_list)

    print(fund.root)
    print(fund.rank)
    fund.unionElements(2, 3)
    fund.unionElements(3, 4)
    fund.unionElements(4, 0)
    print(fund.root)
    print(fund.rank)
