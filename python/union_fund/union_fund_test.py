import time
import random

from quick_union_fund import QuickUnionFund


class UnionFundTest:
    def test_UF_one(self, n):
        start_time = time.time()
        init_list = []
        for i in range(0, n + 1):
            init_list.append(i)
        uf = QuickUnionFund(init_list)
        for i in range(0, n):
            uf.unionElements(random.randint(0, n), random.randint(0, n))
        for i in range(0, n):
            uf.isConnected(random.randint(0, n), random.randint(0, n))
        end_time = time.time()
        print('运行时间为：%s' % (end_time - start_time))


if __name__ == "__main__":
    test = UnionFundTest()
    test.test_UF_one(10000)
