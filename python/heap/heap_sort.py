import random
import time
from max_heap import MaxHeap


def heap_sort_one(init_list):
    '''堆排序1
    循环未排序数组，将数组依次添加到堆中。
    计算数组的个数或者获取堆的元素个数。
    下标倒序循环，依次取出堆的最大值并在此下标赋值。
    '''
    max_heap = MaxHeap()
    for i in init_list:
        max_heap.insert(i)
    list_count = len(init_list)
    # list_count = max_heap.size()
    for c in range(list_count, 0, -1):
        init_list[c - 1] = max_heap.extract_max()
    return init_list


def heap_sort_two(init_list):
    '''堆排序2
    将整个数组添加到堆中。
    计算数组的个数或者获取堆的元素个数。
    下标倒序循环，依次取出堆的最大值并在此下标赋值。
    '''
    max_heap = MaxHeap()
    max_heap.all_insert_heap(init_list)
    list_count = len(init_list)
    for c in range(list_count, 0, -1):
        init_list[c - 1] = max_heap.extract_max()
    return init_list


class heap_sort_three:
    '''堆排序三：原地堆排序'''
    def heap_sort(self, init_list):
        '''堆排序
        统计数组元素个数
        第一次循环，从后到前依次将拥有子节点的节点向下判断，循环后即为一个最大堆；
            注意：原地堆排序下标0为堆的顶点，那么节点的左子节点为2n+1，右子节点为2n+2
        第二次循环，从后向前依次与下标0元素交换位置，交换后需要对下标0元素向下判断；
        Agrs:
            init_list: 未排序数组
        '''
        list_n = len(init_list)
        for i in range(int((list_n-1)/2), -1, -1):
            self._shift_down(init_list, list_n, i)
        for i in range(list_n - 1, 0, -1):
            init_list[i], init_list[0] = init_list[0], init_list[i]
            self._shift_down(init_list, i, 0)

    def _shift_down(self, init_list, list_n, i):
        '''向下判断堆的条件
        原地堆排序下标0为堆的顶点，那么节点的左子节点为2n+1，右子节点为2n+2
        Agrs:
            init_list: 未进行判断的堆
            list_n: 堆的元素个数
            i: 要判断的顶节点
        '''
        while i * 2 + 1 < list_n:
            j = i * 2 + 1
            if j + 1 < list_n and init_list[j + 1] > init_list[j]:
                j = j + 1
            if init_list[j] < init_list[i]:
                break
            init_list[i], init_list[j] = init_list[j], init_list[i]
            i = j


if __name__ == "__main__":
    max = 1000000
    init_list = [random.randint(0, max) for x in range(max)]
    start_time = time.time()
    heap_sort_three = heap_sort_three()
    heap_sort_three.heap_sort(init_list)
    end_time = time.time()
    print('运行时间：%s' % (end_time - start_time))
