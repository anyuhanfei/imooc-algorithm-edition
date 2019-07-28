'''
希尔排序 shell_sort

希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
'''

from generate_random_list import GenerateRandomList
import math


def shell_sort(disorder_list):
    '''
        以列表元素数除以二为增量分组（以后已增量分组除以二为新的增量分组）；
        第一个循环以增量分组的值为起始下标，每次循环递增1；
        第二个循环以第一个循环的值减去增量分组的值为起始，每次循环递减一个增量分组的值；
        在第二循环中，比较第二循环的值是否大于0（判断是否超出），比较以·第二循环的值为列表下标的值·是否大于以·第二循环的值相加增量分组值所得的值·为列表下标的值，如果大于则交换；
    '''
    list_count = len(disorder_list)
    shell = math.floor(list_count/2)
    while shell > 0:
        i = shell
        while i < list_count:
            j = i - shell
            while j >= 0 and disorder_list[j] > disorder_list[j+shell]:
                disorder_list[j], disorder_list[j+shell] = disorder_list[j+shell], disorder_list[j]
                j -= shell
            i += 1
        shell = math.floor(shell/2)
    return disorder_list


if __name__ == "__main__":
    grl = GenerateRandomList()
    disorder_list_one = grl.integer_list(10, 0, 100)
    print(shell_sort(disorder_list_one))
