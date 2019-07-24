"""
    选择排序 selection_sort

    第一次循环，找出所有元素值中最小的一个，与第一个元素交换位置；第二次循环，找出从第二位元素开始的元素的最小值，与第二个元素交换位置，依次类推；
"""

from generate_random_list import GenerateRandomList


def selection_sort(disorder_list):
    """
        选择排序

        第一个循环，获取本次循环中的元素位置并标记为最小值；在第一个循环内做第二个循环，只操作第一个循环位置之后的元素，对比循环元素的值是否小于已标记的最小值，如果小于则将最小值的标记修改为本元素的位置；第二个循环结束后交换第一个循环位置和最小值标记位置的值。

        Args:
            disorder_list:需要排序的列表;
    """
    for i in range(len(disorder_list)):
        min_number = i
        for j in range(i, len(disorder_list)):
            if disorder_list[j] < disorder_list[min_number]:
                min_number = j
        disorder_list[i], disorder_list[min_number] = disorder_list[min_number], disorder_list[i]
    return disorder_list


if __name__ == "__main__":
    grl = GenerateRandomList()
    disorder_list = grl.integer_list(10, 0, 100)
    print(selection_sort(disorder_list))
