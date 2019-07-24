<?php

/**
 * 生成无序的纯数字类型的数组
 *
 * @param integer $number 数组元素个数
 * @param integer $min 最小值
 * @param integer $max 最大值
 * @return void
 */
function disorderly_array($number, $min = 0, $max = 100){
    $init_array = array();
    for($i = 0; $i < $number; $i++){
        array_push($init_array, mt_rand($min, $max));
    }
    return $init_array;
}