class MaxHeap:
    '''最大堆'''
    data = []
    count = 0

    def __init__(self):
        '''初始化堆列表，占用掉下标为0的元素，使堆的第一个元素下标为1'''
        self.data.append('-')

    def size(self):
        '''获取堆的元素个数'''
        return self.count

    def is_empty(self):
        '''判断堆是否为空'''
        return self.count == 0

    def insert(self, value):
        '''添加一个元素到堆的末尾，堆的元素个数加一，并更新堆'''
        self.data.append(value)
        self.count += 1
        self._shift_up(self.count)

    def extract_max(self):
        '''取出堆中最大的元素
        也就是取出下标为1的元素，将堆的最后一个元素移动到下标1上；
        堆的元素个数-1；
        堆从指定位置向下更新；
        '''
        if self.count < 1:
            return
        self.data[self.count], self.data[1] = self.data[1], self.data[self.count]
        self.count -= 1
        self._shift_down(1)
        return self.data.pop(self.count + 1)

    def all_insert_heap(self, init_list):
        '''将整个无序数组加入到堆
        无序数组和堆的最大区别在于下标0的位置的值。
        堆的元素个数即为数组元素个数。
        当以堆中的无子节点的节点作为顶节点时，这个堆是符合条件的，因此，没有子节点的节点不需要进行判断，即count/2。
        其他有子节点的节点需要倒序依次进行向下判断。
        '''
        self.data = self.data + init_list
        self.count = len(init_list)
        for i in range(int(self.count/2), 0, -1):
            self._shift_down(i)

    def _shift_down(self, k):
        '''将指定位置的值向下移动的相应的位置'''
        while True:
            left_down_k = 2 * k
            temp_k = left_down_k
            if left_down_k + 1 <= self.count and self.data[left_down_k] < self.data[left_down_k + 1]:
                temp_k = left_down_k + 1
            if temp_k > self.count or self.data[temp_k] <= self.data[k]:
                break
            self.data[temp_k], self.data[k] = self.data[k], self.data[temp_k]
            k = temp_k

    def _shift_up(self, k):
        '''将指定位置的值向上移动到相应位置'''
        up_k = int(k / 2)
        while k > 1 and self.data[up_k] < self.data[k]:
            self.data[up_k], self.data[k] = self.data[k], self.data[up_k]
            k = up_k
            up_k = int(k / 2)

    def show(self):
        '''简单的堆展示'''
        print()
        level = 1
        i = 1
        while i < self.count:
            print(' ' * int(self.count / level), end="")
            print(str(self.data[i]), end="")
            print(' ' * int(self.count / level), end="")
            i += 1
            if level * 2 == i:
                print()
                level = level * 2
