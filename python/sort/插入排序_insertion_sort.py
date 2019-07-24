"""
    插入排序 insertion_sort

    当前元素与前一个元素比较，如果比前一个元素小则双方交换位置，然后在与前一个元素比较，直到此元素比前一个元素大或者已经在最前位置。
"""

from generate_random_list import GenerateRandomList


def insertion_sort_one(disorder_list):
    """
        逆向思维解析

        从第二个元素开始循环，循环中，创建一个从大到小排序的列表（由当前循环元素之前的元素组成）；循环这个从大到小排序的列表，判断`当前位置上的元素值`与`下一个位置上的元素值`的大小，如果当前元素大则双方交换位置，否则结束本次循环（里层循环结束）；

        Args:
            disorder_list:未排序的列表

        Raises：
            每次符合条件就会交换位置，消耗比较大
    """
    for i in range(1, len(disorder_list)):
        j_list_sort = list(range(0, i))
        j_list_sort.reverse()
        for j in j_list_sort:
            if disorder_list[j] > disorder_list[j+1]:
                disorder_list[j], disorder_list[j+1] = disorder_list[j+1], disorder_list[j]
            else:
                break
    return disorder_list


def insertion_sort_one_optimize(disorder_list):
    """
        insertion_sort_one()方法的优化版

        解决了每次符合条件就会交换位置，修改为对比成功后再交换一次位置;

        Args:
            disorder_list:未排序的列表
    """
    for i in range(1, len(disorder_list)):
        i_place = i
        i_value = disorder_list[i]
        j_list_sort = list(range(0, i))
        j_list_sort.reverse()
        for j in j_list_sort:
            if disorder_list[j] > i_value:
                disorder_list[j+1] = disorder_list[j]
                i_place = j
            else:
                break
        disorder_list[i_place] = i_value
    return disorder_list


def insertion_sort_two(disorder_list):
    """
        顺向思维解析

        从第二个元素开始循环，循环中，创建while循环，如果当前位置的元素值比前一个位置的元素值小并且当前位置不小于0，则循环持续；循环内交换当前位置和前一个位置的元素值，并当前位置向前移动一位；

        Args:
            disorder_list:未排序的列表

        Raises：
            每次符合条件就会交换位置，消耗比较大
    """
    for i in range(1, len(disorder_list)):
        j = i
        while j > 0 and disorder_list[j] < disorder_list[j-1]:
            disorder_list[j], disorder_list[j-1] = disorder_list[j-1], disorder_list[j]
            j = j-1
    return disorder_list


def insertion_sort_two_optimize(disorder_list):
    """
        insertion_sort_two()方法的优化版

        解决了每次符合条件就会交换位置，修改为对比成功后再交换一次位置;

        Args:
            disorder_list:未排序的列表
    """
    for i in range(1, len(disorder_list)):
        j = i
        i_value = disorder_list[i]
        while j > 0 and i_value < disorder_list[j-1]:
            disorder_list[j] = disorder_list[j-1]
            j = j-1
        disorder_list[j] = i_value
    return disorder_list


if __name__ == "__main__":
    grl = GenerateRandomList()
    disorder_list_one = grl.integer_list(10, 0, 100)
    print(insertion_sort_one_optimize(disorder_list_one))
    disorder_list_two = grl.integer_list(10, 0, 100)
    print(insertion_sort_two_optimize(disorder_list_two))
