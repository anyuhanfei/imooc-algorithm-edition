<?php

/**
 * 选择排序 selection_sort
 * 
 * 第一次循环，找出所有元素值中最小的一个，与第一个元素交换位置；第二次循环，找出从第二位元素开始的元素的最小值，与第二个元素交换位置，依次类推；
 * 
 * O(n^2)
 */


/**
 * 第一个循环，获取本次循环中的元素位置并标记为最小值；在第一个循环内做第二个循环，只操作第一个循环位置之后的元素，对比循环元素的值是否小于已标记的最小值，如果小于则将最小值的标记修改为本元素的位置；第二个循环结束后交换第一个循环位置和最小值标记位置的值。
 *
 * 
 * @param [type] $disorder_array 未排序数组
 * @return void
 */
function selection_sort($disorder_array){
    $len_array = count($disorder_array);
    for($i=0;$i<$len_array;$i++){
        $min_number = $i;
        for($j=$i;$j<$len_array;$j++){
            if($disorder_array[$j] < $disorder_array[$min_number]){
                $min_number = $j;
            }
        }
        $middle = $disorder_array[$i];
        $disorder_array[$i] = $disorder_array[$min_number];
        $disorder_array[$min_number] = $middle;
    }
    return $disorder_array;
}

include_once "generate_random_array.php";
$gra = new GenerateRandomArray;
$disorder_array = $gra->integer_array(10, 0, 10);
print_r($disorder_array);
print_r(selection_sort($disorder_array));