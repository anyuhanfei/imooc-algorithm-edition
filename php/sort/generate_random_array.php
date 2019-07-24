<?php

/**
 * 生成随机数组
 */
class GenerateRandomArray{

    /**
     * 生成随机整数数组
     *
     * @param [type] $number 元素个数
     * @param [type] $lower_limit 下限
     * @param [type] $upper_limit 上限
     * @return void
     */
    public function integer_array($number, $lower_limit, $upper_limit){
        $return_array = array();
        for($i=0;$i<$number;$i++){
            $return_array[] = rand($lower_limit, $upper_limit);
        }
        return $return_array;
    }

    /**
     * 近乎有序的整数列表
     * 
     * 生成一个有序列表，根据参数或者列表元素的个数来随机交换n次两个元素的位置；
     *
     * @param [type] $number 列表元素的个数
     * @param integer $exchange_number 元素位置交换的次数，默认为0，如果为0则交换次数为列表元素个数的五分之一
     * @return void
     */
    public function generate_nearly_ordered_list($number, $exchange_number = 0){
        $return_array = array();
        for($i=0;$i<$number;$i++){
            $return_array[] = $i;
        }
        $exchange_number = $exchange_number == 0 ? ceil($number / 5) : $exchange_number;
        for($j=0;$j<$exchange_number;$j++){
            $posx = rand(0, $number-1);
            $posy = rand(0, $number-1);
            $middle = $return_array[$posx];
            $return_array[$posx] = $return_array[$posy];
            $return_array[$posy] = $middle;
        }
        return $return_array;
    }
}