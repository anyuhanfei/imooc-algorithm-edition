<?php
/**
 * 快速排序
 * 
 * 过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
 * 
 * 每次以数组（限定范围内）最左边为基准值，左哨兵站最左侧向右走,右哨兵站最右侧向左走，当左哨兵遇到大于基准值的值时暂停，当右哨兵遇到小于基准值的值时暂停，两哨兵下的值交换位置；直到两个哨兵相遇，交换基准值和哨兵位置的值；将左右两边分为两个数组重复进行，直到左哨兵和右哨兵刚开始就在同一个位置；
 *
 * @param [type] $disorder_array 数组
 * @param [type] $left_key 数组左边下标
 * @param [type] $right_key 数组右边下标
 * @return void
 */
function quick_sort(&$disorder_array, $left_key, $right_key){
    if($left_key >= $right_key){
        return;
    }
    $temp = $disorder_array[$left_key];
    $sentry_left = $left_key;
    $sentry_right = $right_key;
    while($sentry_left < $sentry_right){
        while($disorder_array[$sentry_right] >= $temp && $sentry_left < $sentry_right){
            $sentry_right = $sentry_right - 1;
        }
        while($disorder_array[$sentry_left] <= $temp && $sentry_left < $sentry_right){
            $sentry_left = $sentry_left + 1;
        }
        if($sentry_left < $sentry_right){
            $middle = $disorder_array[$sentry_right];
            $disorder_array[$sentry_right] = $disorder_array[$sentry_left];
            $disorder_array[$sentry_left] = $middle;
        }else{
            break;
        }
    }
    $middle = $disorder_array[$left_key];
    $disorder_array[$left_key] = $disorder_array[$sentry_left];
    $disorder_array[$sentry_left] = $middle;
    quick_sort($disorder_array, 0, $sentry_left-1);
    quick_sort($disorder_array, $sentry_right+1, $right_key);
}

include_once "generate_random_array.php";
$gra = new GenerateRandomArray;
$disorder_array = $gra->integer_array(10, 0, 100);
$res = quick_sort($disorder_array, 0, count($disorder_array)-1);
print_r($disorder_array);