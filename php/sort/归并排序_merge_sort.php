<?php
/**
 * 归并排序 merge_sort
 * 
 * 计算数组元素个数，并按照当前顺序分成左右两组，然后继续将已分离的数组分成左右两组，直到每个分离的数组都只有一个元素(或0个元素)
 * 初始化三个变量，$i表示左边数组的下标，$j表示右边数组的下标，$k表示排序完成的数组的下标
 * 第一个while循环，当$i小于左数组的元素数 并且 $j小于右数组的元素数时，判断左右数组的当前值哪个大，值大的一方添加到排序数组中并且$k++，那一方代表下标的变量++；
 * 第一个循环中，左右两数组元素一一对比，就会出现一方数组完成了排序，一方数组还有元素未完成排序；
 * 第二个while和第三while就是将剩余的未对比的元素按照顺序加入到排序数组的末尾（左右两数组中的元素已经是有序的了）；
 * 
 *
 * @param array $disorder_array
 * @return void
 */
function merge_sort($disorder_array){
    $count_array = count($disorder_array);
    if($count_array <= 1){
        return $disorder_array;
    }
    $mid = floor($count_array/2);
    $left_array = merge_sort(array_slice($disorder_array, 0, $mid));
    $right_array = merge_sort(array_slice($disorder_array, -($count_array - $mid)));
    $i = 0;
    $j = 0;
    $k = 0;
    $count_left = count($left_array);
    $count_right = count($right_array);
    while($i < $count_left && $j < $count_right){
        if($left_array[$i] <= $right_array[$j]){
            $disorder_array[$k] = $left_array[$i];
            $i++;
        }else{
            $disorder_array[$k] = $right_array[$j];
            $j++;
        }
        $k++;
    }
    while($i < $count_left){
        $disorder_array[$k] = $left_array[$i];
        $i++;
        $k++;
    }
    while($j < $count_right){
        $disorder_array[$k] = $right_array[$j];
        $j++;
        $k++;
    }
    return $disorder_array;
}

include_once "generate_random_array.php";
$gra = new GenerateRandomArray;
$disorder_array = $gra->integer_array(10, 0, 100);
$res = merge_sort($disorder_array);
print_r($disorder_array);

