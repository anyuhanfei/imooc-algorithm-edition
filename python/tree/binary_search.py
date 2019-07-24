def binary_search_iteration(arr, target):
    '''二分查找法，迭代版
    Arge:
        arr: 有序一维数组
        target: 要查找的值
    return:
        int,要查找的值的索引,如果没有则返回-1
    '''
    arr_count = len(arr)
    left, right = 0, arr_count - 1
    while left <= right:
        mid = int(left + (right - left) / 2)  # (left + right) / 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursion(arr, left, right, target):
    '''二分查找法，递归版
    Arge:
        arr: 有序一维数组
        left: 左边界
        right: 右边界,(初始化为数组总元素个数减一)
        target: 要查找的值
    return:
        int,要查找的值的索引,如果没有则返回-1
    '''
    if left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return binary_search_recursion(arr, mid + 1, right, target)
        else:
            return binary_search_recursion(arr, left, mid - 1, target)
    return -1


def binary_search_iteration_ceil_and_floor(arr, value):
    '''二分查找
    将有序数组中的符合要求的元素索引范围返回给用户，迭代版
    Arge：
        arr：有序数组
        value：要查找的值
    return：
        元组，符合要求的元素索引范围，开区间，如果是两个相连的索引则说明没有查找到符合要求的元素值
    '''
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] == value:
            floor, ceil = mid - 1, mid + 1
            while arr[floor] == value:
                floor -= 1
            while arr[ceil] == value:
                ceil += 1
            return floor, ceil
        elif arr[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return right, left


def binary_search_recursion_ceil_and_floor(arr, left, right, value):
    '''二分查找
    将有序数组中的符合要求的元素索引范围返回给用户，递归版
    Arge：
        arr：有序数组
        left：左边界，闭区间
        right：右边界，闭区间
        value：要查找的值
    return：
        元组，符合要求的元素索引范围，开区间，如果是两个相连的索引则说明没有查找到符合要求的元素值
    '''
    if left > right:
        return right, left
    mid = int(left + (right - left) / 2)
    if arr[mid] == value:
        floor, ceil = mid - 1, mid + 1
        while arr[floor] == value:
            floor -= 1
        while arr[ceil] == value:
            ceil += 1
        return floor, ceil
    elif arr[mid] > value:
        return binary_search_recursion_ceil_and_floor(arr, left, mid - 1, value)
    else:
        return binary_search_recursion_ceil_and_floor(arr, mid + 1, right, value)


if __name__ == "__main__":
    arr = []
    for i in range(1, 10):
        if i == 5:
            arr.append(i)
            arr.append(i)
            arr.append(i)
        arr.append(i)
    print(len(arr))
    value = 5
    print(binary_search_iteration(arr, value))
    print(binary_search_recursion(arr, 0, len(arr) - 1, value))
    print(binary_search_iteration_ceil_and_floor(arr, value))
    print(binary_search_recursion_ceil_and_floor(arr, 0, len(arr) - 1, value))