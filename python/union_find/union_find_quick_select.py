class UnionFindQuickSelect:
    '''快速查找的并查集
    查操作时间复杂度为O(1)，并集操作时间复杂度为O(n²)
    '''
    count = 0
    root = dict()

    def __init__(self, init_list=[]):
        '''初始化并查集
        将元素一一放入字典中，字典中的键表示元素值，值表示元素之间的连接关系

        Agre:
            init_list: 要插入并查集的元素集
        '''
        self.count = len(init_list)
        for i in range(0, self.count):
            self.root.update({init_list[i]: i})

    def find(self, value):
        '''查询一个元素值所在的组

        Agre:
            value: 元素值(键)
        '''
        return self.root[value]

    def isConnected(self, p, q):
        '''查询两个元素值是否是连接状态(是否在同一个组)

        Agre:
            p: 元素值
            q: 元素值
        return:
            bool
        '''
        return self.root[p] == self.root[q]

    def unionElements(self, p, q):
        '''将两个元素值连接
        连接两个元素值时，注意两个元素值已连接的元素不能被分离，所以要将两个元素值所在的组中的元素都合并到同一个组中

        Agre:
            p: 元素值
            q: 元素值
        '''
        p_id = self.root[p]
        q_id = self.root[q]
        if p_id == q_id:
            return
        for i in self.root.keys():
            if self.root[i] == p_id:
                self.root[i] = q_id


if __name__ == "__main__":
    init_list = []
    list_len = 10
    for i in range(10, 10 + list_len):
        init_list.append(i)

    fund = UnionFindQuickSelect(init_list)

    print(fund.root)
    fund.unionElements(12, 13)
    print(fund.root)
    print(fund.isConnected(12, 13))
