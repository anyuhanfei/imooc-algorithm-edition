import time
import random


def quick_sort_two_ways(init_list, left_key, right_key):
    '''二路快速排序
    当分支元素个数小于16个时使用插入排序；
    待排序数组仅有少量乱序元素的问题，要随机获取基准值，并将基准值与第一个元素值交换；
    左右下标向中间移动时，注意判断的问题，两者移动有一个共同的条件就是左下标与右下标的相对位置；
    这里有几种情况，一个是左下标必定走到右下标右边，一个是左右下标相同，注意在 内层while语句,外存while语句的结束条件的判断；
    左右下标判断当前是否大于小于基准值时，不要加上等号，这样在有大量相同元素时会有迭代次数过多的错误；
    如果循环完成后左下标必定大于右下标，则需要用右下标与基准值交换，递归下标范围也是使用右下标；

    Arge:
        init_list: 待排序数组，列表
        left_key: 本次排序的左范围
        right_key: 本次排序的右范围
    return:
        None
    '''
    if right_key - left_key <= 16:
        assist_insertion_sort(init_list, left_key, right_key)
        return
    base_key = random.randint(left_key, right_key)
    init_list[left_key], init_list[base_key] = init_list[base_key], init_list[left_key]
    base_value = init_list[left_key]
    left_sentry = left_key + 1
    right_sentry = right_key
    while True:
        while left_sentry <= right_sentry and init_list[left_sentry] < base_value:
            left_sentry += 1
        while right_sentry >= left_sentry and init_list[right_sentry] > base_value:
            right_sentry -= 1
        if left_sentry > right_sentry:
            break
        init_list[right_sentry], init_list[left_sentry] = init_list[left_sentry], init_list[right_sentry]
        right_sentry -= 1
        left_sentry += 1
    init_list[left_key], init_list[right_sentry] = init_list[right_sentry], init_list[left_key]
    quick_sort_two_ways(init_list, left_key, right_sentry - 1)
    quick_sort_two_ways(init_list, right_sentry + 1, right_key)


def quick_sort_three_ways(init_list, left_key, right_key):
    '''三路快速排序
    和一路快速排序类似，但是多了一个对等于基准数的判断；
    定义一个一直向右的走下标（最左+1），定义一个左下标（最左），定义一个右下标（最右+1）；
    判断走下标的值，如果大于基准值，与右下标-1的值进行交换，然后右下标-1，走下标不动（因为交换到了一个为检测的值）；
    如果小于基准值，与左下标+1的值进行交换，然后左下标+1，走下标+1；
    如果等于基准值，则走下标+1；
    基准值与左下标交换位置；
    待排序左范围是（最左，左下标-1），右范围是（右下标，最右）
    '''
    if right_key - left_key <= 16:
        assist_insertion_sort(init_list, left_key, right_key)
        return
    base_key = random.randint(left_key, right_key)
    init_list[left_key], init_list[base_key] = init_list[base_key], init_list[left_key]
    base_value = init_list[left_key]
    left_pile = left_key
    sentry = left_key + 1
    right_pile = right_key + 1
    while sentry < right_pile:
        if init_list[sentry] > base_value:
            init_list[right_pile - 1], init_list[sentry] = init_list[sentry], init_list[right_pile - 1]
            right_pile -= 1
        elif init_list[sentry] < base_value:
            init_list[left_pile + 1], init_list[sentry] = init_list[sentry], init_list[left_pile + 1]
            left_pile += 1
            sentry += 1
        else:
            sentry += 1
    init_list[left_key], init_list[left_pile] = init_list[left_pile], init_list[left_key]
    quick_sort_three_ways(init_list, left_key, left_pile - 1)
    quick_sort_three_ways(init_list, right_pile, right_key)


def assist_insertion_sort(init_list, left_key, right_key):
    for i in range(left_key + 1, right_key + 1):
        j = i
        i_value = init_list[i]
        while j > left_key and i_value < init_list[j-1]:
            init_list[j] = init_list[j-1]
            j = j-1
        init_list[j] = i_value


if __name__ == "__main__":
    max = 1000000
    init_list = [random.randint(0, 100) for x in range(max)]
    start_time = time.time()
    quick_sort_three_ways(init_list, 0, len(init_list)-1)
    # print(init_list)
    end_time = time.time()
    print('执行时间:%s' % (end_time - start_time))
