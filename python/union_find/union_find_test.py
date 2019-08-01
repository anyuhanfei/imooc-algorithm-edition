import time
import random

from union_find_quick_select import UnionFindQuickSelect
from union_find import UnionFind
from union_find_sz import UnionFindSz
from union_find_rank import UnionFindRank
from union_find_path_compression import UnionFindPathCompression


class UnionFundTest:
    def test_UF_one(self, n):
        start_time = time.time()
        init_list = []
        for i in range(0, n + 1):
            init_list.append(i)
        uf = UnionFindQuickSelect(init_list)
        for i in range(0, n):
            uf.unionElements(random.choice(init_list), random.choice(init_list))
        for i in range(0, n):
            uf.isConnected(random.choice(init_list), random.choice(init_list))
        end_time = time.time()
        print('快速查询版并查集运行时间为：%s' % (end_time - start_time))

    def test_UF_two(self, n):
        start_time = time.time()
        init_list = []
        for i in range(0, n + 1):
            init_list.append(i)
        uf = UnionFind(init_list)
        for i in range(0, n):
            uf.unionElements(random.choice(init_list), random.choice(init_list))
        for i in range(0, n):
            uf.isConnected(random.choice(init_list), random.choice(init_list))
        end_time = time.time()
        print('并查集运行时间为：%s' % (end_time - start_time))

    def test_UF_three(self, n):
        start_time = time.time()
        init_list = []
        for i in range(0, n + 1):
            init_list.append(i)
        uf = UnionFindSz(init_list)
        for i in range(0, n):
            uf.unionElements(random.choice(init_list), random.choice(init_list))
        for i in range(0, n):
            uf.isConnected(random.choice(init_list), random.choice(init_list))
        end_time = time.time()
        print('sz优化版并查集运行时间为：%s' % (end_time - start_time))

    def test_UF_four(self, n):
        start_time = time.time()
        init_list = []
        for i in range(0, n + 1):
            init_list.append(i)
        uf = UnionFindRank(init_list)
        for i in range(0, n):
            uf.unionElements(random.choice(init_list), random.choice(init_list))
        for i in range(0, n):
            uf.isConnected(random.choice(init_list), random.choice(init_list))
        end_time = time.time()
        print('rank优化版并查集运行时间为：%s' % (end_time - start_time))

    def test_UF_five(self, n):
        start_time = time.time()
        init_list = []
        for i in range(0, n + 1):
            init_list.append(i)
        uf = UnionFindPathCompression(init_list)
        for i in range(0, n):
            uf.unionElements(random.choice(init_list), random.choice(init_list))
        for i in range(0, n):
            uf.isConnected(random.choice(init_list), random.choice(init_list))
        end_time = time.time()
        print('路径压缩版并查集运行时间为：%s' % (end_time - start_time))


if __name__ == "__main__":
    n = 10000
    test = UnionFundTest()
    test.test_UF_one(n)
    test.test_UF_two(n)
    test.test_UF_three(n)
    test.test_UF_four(n)
    test.test_UF_five(n)
