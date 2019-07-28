<?php

/**
 * 冒泡排序（Bubble Sort）
 * 
 * 它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果他们的顺序（如从大到小、首字母从A到Z）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素已经排序完成。
 *
 * O(n^2)
 * @param [type] $disorder_array 未排序数组
 * @return void
 */
function bubble_sort($disorder_array){
    $array_count = count($disorder_array);
    for($i = 0; $i < $array_count; $i++){
        $exchange = false;
        for($j = 0; $j < $array_count - 1; $j++){
            if($disorder_array[$j] > $disorder_array[$j + 1]){
                $middle = $disorder_array[$j];
                $disorder_array[$j] = $disorder_array[$j + 1];
                $disorder_array[$j + 1] = $middle;
                $exchange = true;
            }
        }
        if($exchange == false){
            break;
        }
    }
    return $disorder_array;
}

include_once "generate_random_array.php";
$gra = new GenerateRandomArray;
$disorder_array = $gra->integer_array(10, 0, 100);
print_r(bubble_sort($disorder_array));