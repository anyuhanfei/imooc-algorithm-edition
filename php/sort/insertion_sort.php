<?php
/**
 * 插入排序 insertion_sort
 * 
 * 当前元素与前一个元素比较，如果比前一个元素小则双方交换位置，然后在与前一个元素比较，直到此元素比前一个元素大或者已经在最前位置。
 * 
 * O(n^2)
 * 
 * @param [type] $disorder_array
 * @return void
 */
function insertion_sort($disorder_array){
    $array_count = count($disorder_array);
    for($i = 1; $i < $array_count; $i++){
        for($j = $i; $j > 0 && $disorder_array[$j] < $disorder_array[$j-1]; $j--){
            $middle = $disorder_array[$j-1];
            $disorder_array[$j-1] = $disorder_array[$j];
            $disorder_array[$j] = $middle;
        }
    }
    return $disorder_array;
}

include_once "generate_random_array.php";
$gra = new GenerateRandomArray;
$disorder_array = $gra->integer_array(10, 0, 100);
print_r(insertion_sort($disorder_array));