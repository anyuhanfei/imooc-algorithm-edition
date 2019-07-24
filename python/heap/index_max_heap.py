import random


class IndexMaxHeap:
    '''索引堆'''
    data = []
    indexes = []
    reverse = []
    count = 0

    def __init__(self):
        '''初始化
        初始化元素值数组
        初始化索引数组
        初始化索引在堆中相应位置数组
        '''
        self.data.append('-')
        self.indexes.append('-')
        self.reverse.append('-')

    def size(self):
        '''获取堆的元素个数'''
        return self.count

    def is_empty(self):
        '''判断堆是否为空'''
        return self.count == 0

    def insert(self, i, value):
        '''插入一个元素和索引
        元素值加入data数组中，索引值加入indexes中，都以下标1为开始；
        data数组加入元素值，indexes数组加入索引值+1，堆计数+1，reverse数组加入堆计数的值；
        以堆计数的值为起点，向上更新堆；
        Arge：
            i: 传入的i对用户而言，是从0索引的
            value: i下标对应的元素值
        '''
        i += 1
        self.data.append(value)
        self.indexes.append(i)
        self.count += 1
        self.reverse.append(self.count)
        self._shift_up(self.count)

    def extract_max_value(self):
        '''删除一个元素
        即取出下标1的元素，即最大的元素
        先判断堆中的元素个数是否小于1；
        交换索引数组中的第一个索引和最后一个索引；
        交换后，reverse数组更新两者对应的位置；
        元素个数减一并从下标1向下更新堆，通过pop()函数取出并返回值（删除）
        '''
        if self.count < 1:
            return
        self.indexes[self.count], self.indexes[1] = self.indexes[1], self.indexes[self.count]
        self.reverse[self.indexes[1]] = 1
        self.reverse[self.indexes[self.count]] = 0
        pop_index = self.indexes.pop(self.count)
        self.count -= 1
        self._shift_down(1)
        return self.data[pop_index]

    def extract_max_index(self):
        '''删除一个元素，并返回索引值
        基本同extract_max_index()
        '''
        if self.count < 1:
            return
        self.indexes[self.count], self.indexes[1] = self.indexes[1], self.indexes[self.count]
        self.reverse[self.indexes[1]] = 1
        self.reverse[self.indexes[self.count]] = 0
        self.count -= 1
        self._shift_down(1)
        return self.indexes.pop(self.count + 1)

    def get_item(self, i):
        '''获取下标为i的元素值（i是对用户而言）'''
        assert self._contain(i)
        return self.data[i + 1]

    def change(self, i, new_item):
        '''修改一个元素值
        将i加一，转换为堆中的下标；
        将data数组中的i下标的元素值替换为新的元素值；
        这时因为修改了值，需要向上和向下更新堆；
        Agre：
            i：对用户而言的下标，以0开始
            new_item：要修改为的元素值
        '''
        assert self._contain(i)
        i += 1
        self.data[i] = new_item
        self._shift_down(self.reverse[i])
        self._shift_up(self.reverse[i])
        return

    def _contain(self, i):
        '''判断i是否有超出堆索引范围'''
        if i + 1 >= 1 and i + 1 <= self.count and self.reverse[i+1] != 0:
            return True
        return False

    def _shift_down(self, k):
        '''将指定位置的值向下移动的相应的位置
        同_shift_up()，以对应索引数值对应下标的值为下标取对应元素值数组的值做比较；
        交换操作交换索引数组中的值；
        交换后，reverse数组更新两者对应的位置；
        '''
        while True:
            left_down_k = 2 * k
            temp_k = left_down_k
            if temp_k + 1 <= self.count and self.data[self.indexes[temp_k]] < self.data[self.indexes[temp_k + 1]]:
                temp_k += 1
            if temp_k > self.count or self.data[self.indexes[temp_k]] <= self.data[self.indexes[k]]:
                break
            self.indexes[temp_k], self.indexes[k] = self.indexes[k], self.indexes[temp_k]
            self.reverse[self.indexes[temp_k]] = temp_k
            self.reverse[self.indexes[k]] = k
            k = temp_k

    def _shift_up(self, k):
        '''将指定位置的值向上移动到相应位置
        对比时需要对比以堆相应位置的索引为下标的元素值，交换的是索引的位置；
        交换后，reverse数组更新两者对应的位置；
        '''
        up_k = int(k / 2)
        while k > 1 and self.data[self.indexes[up_k]] < self.data[self.indexes[k]]:
            self.indexes[up_k], self.indexes[k] = self.indexes[k], self.indexes[up_k]
            self.reverse[self.indexes[up_k]] = up_k
            self.reverse[self.indexes[k]] = k
            k = up_k
            up_k = int(k / 2)

    def show(self):
        '''简单的堆展示'''
        print()
        level = 1
        i = 1
        while i <= self.count:
            print(' ' * int(self.count / level), end="")
            print(str(self.data[self.indexes[i]]), end="")
            print(' ' * int(self.count / level), end="")
            i += 1
            if level * 2 == i:
                print()
                level = level * 2


if __name__ == "__main__":
    max = 10
    init_list = [random.randint(100, 200) for x in range(max)]
    imh = IndexMaxHeap()
    for i in range(0, len(init_list)):
        imh.insert(i, init_list[i])
    imh.show()
    print()
    print(imh.indexes)
    print(imh.data)
    print(imh.reverse)
    # for o in range(0, len(init_list)):
    #     print(imh.extract_max_value())
    imh.change(9, 201)
    print()
    print(imh.indexes)
    print(imh.data)
    print(imh.reverse)
    imh.show()
