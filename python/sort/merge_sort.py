'''
归并排序 merge_sort

将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
'''
import time

from generate_random_list import GenerateRandomList


def merge_sort(disorder_list):
    '''
        计算数组元素个数，并按照当前顺序分成左右两组，然后继续将已分离的数组分成左右两组，直到每个分离的数组都只有一个元素(或0个元素)
        初始化三个变量，$i表示左边数组的下标，$j表示右边数组的下标，$k表示排序完成的数组的下标
        第一个while循环，当$i小于左数组的元素数 并且 $j小于右数组的元素数时，判断左右数组的当前值哪个大，值大的一方添加到排序数组中并且$k++，那一方代表下标的变量++；
        第一个循环中，左右两数组元素一一对比，就会出现一方数组完成了排序，一方数组还有元素未完成排序；
        第二个while和第三while就是将剩余的未对比的元素按照顺序加入到排序数组的末尾（左右两数组中的元素已经是有序的了）；
    '''
    list_count = len(disorder_list)
    if list_count == 1:
        return disorder_list
    middle = int(list_count/2)
    left_list = merge_sort(disorder_list[0: middle])
    right_list = merge_sort(disorder_list[middle:])
    i, j, k = 0, 0, 0
    left_list_count = len(left_list)
    right_list_count = len(right_list)
    while i < left_list_count and j < right_list_count:
        if left_list[i] > right_list[i]:
            disorder_list[k] = left_list[i]
            i += 1
        else:
            disorder_list[k] = right_list[i]
            j += 1
        k += 1
    while i < left_list_count:
        disorder_list[k] = left_list[i]
        i += 1
        k += 1
    while j < right_list_count:
        disorder_list[k] = right_list[j]
        j += 1
        k += 1
    return disorder_list


if __name__ == "__main__":
    grl = GenerateRandomList()
    disorder_list_one = grl.integer_list(1000000, 0, 100)
    start_time = time.time()
    print('起始时间：%s' % start_time)
    merge_sort(disorder_list_one)
    end_time = time.time()
    print('结束时间：%s' % end_time)
    print('执行时间:%s' % (end_time - start_time))
