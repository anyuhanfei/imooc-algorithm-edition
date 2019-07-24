<?php

/**
 * 二分查找
 * 查询到第一个符合要求的值后直接返回响应的索引（迭代版）
 *
 * @param array $arr 有序一维数组
 * @param [type] $value 要查找的元素值
 * @return void
 */
function binary_search_iteration($arr, $value){
    $arr_count = count($arr);
    $left = 0;
    $right = $arr_count - 1;
    while($left <= $right){
        $mid = intval($left + ($right - $left) / 2);
        if($arr[$mid] == $value){
            return $mid;
        }elseif($arr[$mid] > $value){
            $right = $mid - 1;
        }else{
            $left = $mid + 1;
        }
    }
    return -1;
}

/**
 * 二分查找
 * 查询到第一个符合要求的值后直接返回响应的索引（递归版）
 *
 * @param array $arr 有序一维数组
 * @param int $left 左边界（闭区间）
 * @param int $right 右边界（闭区间，数组元素总数减一）
 * @param [type] $value 要查找的元素值
 * @return void
 */
function binary_search_recursion($arr, $left, $right, $value){
    if($left > $right){
        return -1;
    }
    $mid = intval($left + ($right - $left) / 2);
    if($arr[$mid] == $value){
        return $mid;
    }elseif($arr[$mid] > $value){
        return binary_search_recursion($arr, $left, $mid - 1, $value);
    }else{
        return binary_search_recursion($arr, $mid + 1, $right, $value);
    }
}

/**
 * 二分查找
 * 查找出所有值为指定值的元素（迭代版）
 *
 * @param array $arr 有序数组
 * @param [type] $value 要查找的元素值
 * @return array 与指定值相同的元素索引范围，开区间（如果没有则为两个连续的数）
 */
function binary_search_iteration_ceil_and_floor($arr, $value){
    $count = count($arr);
    $left = 0;
    $right = $count - 1;
    while($left <= $right){
        $mid = intval($left + ($right - $left) / 2);
        if($arr[$mid] == $value){
            $ceil = $mid + 1;
            $floor = $mid - 1;
            while($arr[$ceil] == $value){
                $ceil++;
            }
            while($arr[$floor] == $value){
                $floor--;
            }
            return array($floor, $ceil);
        }elseif($arr[$mid] > $value){
            $right = $mid - 1;
        }else{
            $left = $mid + 1;
        }
    }
    return array($right, $left);
}

/**
 * 二分查找法
 * 查找出所有值为指定值的元素（递归版）
 *
 * @param array $arr 有序数组
 * @param int $left 左边界（闭区间）
 * @param int $right 右边界（闭区间）
 * @param [type] $value 要查找的元素值
 * @return array 与指定值相同的元素索引范围，开区间（如果没有则为两个连续的数）
 */
function binary_search_recursion_ceil_and_floor($arr, $left, $right, $value){
    if($left > $right){
        return array($right, $left);
    }
    $mid = intval($left + ($right - $left) / 2);
    if($arr[$mid] == $value){
        $ceil = $mid + 1;
        $floor = $mid - 1;
        while($arr[$ceil] == $value){
            $ceil++;
        }
        while($arr[$floor] == $value){
            $floor--;
        }
        return array($floor, $ceil);
    }elseif($arr[$mid] > $value){
        return binary_search_recursion_ceil_and_floor($arr, $left, $mid - 1, $value);
    }else{
        return binary_search_recursion_ceil_and_floor($arr, $mid + 1, $right, $value);
    }
}



$arr = [];
for($i=1; $i < 10; $i++){
    if($i == 5){
        $arr[] = $i;
        $arr[] = $i;
        $arr[] = $i;
    }
    $arr[] = $i;
}
print_r($arr);
$value = 5;
print_r(binary_search_recursion($arr, 0, count($arr) - 1, $value));
echo "\n";
print_r(binary_search_iteratime($arr, $value));
echo "\n";
print_r(binary_search_iteratime_ceil_and_floor($arr, $value));
echo "\n";
print_r(binary_search_recursion_ceil_and_floor($arr, 0, count($arr) - 1, $value));