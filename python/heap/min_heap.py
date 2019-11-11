class MinHeap:
    '''最小堆'''
    data = []
    count = 0

    def __init__(self):
        self.data.append('-')

    def size(self):
        return self.count

    def insert(self, value):
        self.data.append(value)
        self.count += 1
        self._shift_up(self.count)

    def extract_min(self):
        if self.count < 1:
            return False
        self.data[self.count], self.data[1] = self.data[1], self.data[self.count]
        self.count -= 1
        self._shift_down(1)
        minimum_number = self.data.pop()
        return minimum_number

    def all_insert_heap(self, init_list):
        self.data = self.data + init_list
        self.count += len(init_list)
        for i in range(int(self.count/2), 0, -1):
            self._shift_down(i)

    def _shift_down(self, k):
        while True:
            left_down_k = k * 2
            temp_k = left_down_k
            if left_down_k + 1 <= self.count and self.data[left_down_k + 1] < self.data[left_down_k]:
                temp_k = left_down_k + 1
            if temp_k > self.count or self.data[temp_k] > self.data[k]:
                break
            self.data[temp_k], self.data[k] = self.data[k], self.data[temp_k]
            k = temp_k

    def _shift_up(self, k):
        up_k = int(k / 2)
        print(up_k, self.count, k, self.data)
        while k > 1 and self.data[up_k].wt() > self.data[k].wt():
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
