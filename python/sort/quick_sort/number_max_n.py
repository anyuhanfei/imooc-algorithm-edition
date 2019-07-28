import random


def number_max_n(init_list, left_key, right_key, n):
    '''求数组中第n大的元素
    使用快速排序逐渐缩小范围，知道基准值或者分支仅剩余一位元素

    Arge:
        init_list: 数组
        left_key: 左边界
        right_key: 右边界
        n: 第几大的元素
    return:
        数值
    '''
    if left_key >= right_key:
        return init_list[n]
    base_key = random.randint(left_key, right_key)
    init_list[left_key], init_list[base_key] = init_list[base_key], init_list[left_key]
    base_value = init_list[left_key]
    sentry = left_key + 1
    left_pile = left_key
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
    if left_pile > n:
        res = number_max_n(init_list, left_key, left_pile - 1, n)
        return res
    elif left_pile <= n and right_pile > n:
        return init_list[n]
    else:
        res = number_max_n(init_list, right_pile, right_key, n)
        return res


if __name__ == "__main__":
    max = 30
    max_number = 1
    init_list = [random.randint(0, 10) for x in range(max)]
    print(init_list)
    res = number_max_n(init_list, 0, len(init_list)-1, len(init_list) - max_number)
    print(res)
