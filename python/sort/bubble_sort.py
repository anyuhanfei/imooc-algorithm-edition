'''
冒泡排序（Bubble Sort）

它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果他们的顺序（如从大到小、首字母从A到Z）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素已经排序完成。
'''

from generate_random_list import GenerateRandomList


def bubble_sort(disorder_list):
    for v in range(len(disorder_list)):
        switching_operation = False
        for number in range(len(disorder_list)-1):
            if disorder_list[number] > disorder_list[number+1]:
                disorder_list[number], disorder_list[number+1] = disorder_list[number+1], disorder_list[number]
                switching_operation = True
        if switching_operation is False:
            break
    return disorder_list


if __name__ == "__main__":
    grl = GenerateRandomList()
    disorder_list_one = grl.integer_list(10, 0, 100)
    print(bubble_sort(disorder_list_one))
