<?php

/**
 * 希尔排序 shell_sort
 *
 * 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
 * 
 * O(n^2)
 * 
 * @param [type] $disorder_array 未排序数组
 * @return void
 */
function shell_sort($disorder_array){
    $count_array = count($disorder_array);
    for($shell = floor($count_array/2); $shell > 0; $shell = floor($shell/2)){
        for($i = $shell; $i < $count_array; $i++){
            for($j = $i - $shell; $j >= 0 && $disorder_array[$j] > $disorder_array[$j + $shell]; $j -= $shell){
                $middle = $disorder_array[$j];
                $disorder_array[$j] = $disorder_array[$j + $shell];
                $disorder_array[$j + $shell] = $middle;
            }
        }
    }
    return $disorder_array;
}

include_once "generate_random_array.php";
$gra = new GenerateRandomArray;
$disorder_array = $gra->integer_array(10, 0, 100);
print_r(shell_sort($disorder_array));