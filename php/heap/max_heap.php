<?php

class MaxHeap{
    public $heap_array = array();
    private $count = 0;

    public function __construct(){
        array_push($this->heap_array,'-');
    }

    /**
     * 返回堆元素个数
     *
     * @return void
     */
    public function size(){
        return $this->count;
    }

    /**
     * 添加一个元素到堆
     *
     * @param [type] $value
     * @return void
     */
    public function insert($value){
        array_push($this->heap_array, $value);
        $this->count++;
        $this->_shift_up($this->count);
    }

    /**
     * 获取堆的最大值
     *
     * @return void
     */
    public function extract_max(){
        if($this->count < 1){
            return false;
        }
        //将下标1的值取出，将最后一个元素移动到下标1的位置上
        $max_value = $this->heap_array[1];
        $this->heap_array[1] = $this->heap_array[$this->count];
        unset($this->heap_array[$this->count]);
        $this->count--;
        //自上而下更新
        $this->_shift_down(1);
        return $max_value;
    }

    /**
     * 将未排序数组添加到堆中
     *
     * @param [type] $init_array
     * @return void
     */
    public function all_insert_heap($init_array){
        $this->heap_array = array_merge($this->heap_array, $init_array);
        $this->count = count($this->heap_array) - 1;
        for($i = ceil($this->count / 2); $i > 0; $i--){
            $this->_shift_down($i);
        }
    }

    /**
     * 从指定位置向上更新
     *
     * @param int $n
     * @return void
     */
    private function _shift_up($n){
        while(intval($n/2) >= 1){
            if($this->heap_array[$n] < $this->heap_array[intval($n/2)]){
                break;
            }
            $this->exchange($n, intval($n/2));
            $n = intval($n/2);
        }
    }

    /**
     * 从指定位置向下更新
     *
     * @param int $n
     * @return void
     */
    private function _shift_down($n){
        while($n * 2 <= $this->count){
            $j = $n * 2;
            if($j + 1 <= $this->count && $this->heap_array[$j + 1] > $this->heap_array[$j]){
                $j++;
            }
            if($this->heap_array[$j] < $this->heap_array[$n]){
                break;
            }
            $this->exchange($j, $n);
            $n = $j;
        }
    }

    /**
     * 交换位置
     *
     * @param int $position_one 位置一
     * @param int $position_two 位置二
     * @return void
     */
    private function exchange($position_one, $position_two){
        $temporary = $this->heap_array[$position_one];
        $this->heap_array[$position_one] = $this->heap_array[$position_two];
        $this->heap_array[$position_two] = $temporary;
        unset($temporary);
    }

    /**
     * 简陋的展示
     *
     * @return void
     */
    public function show_heap(){
        $a = $this->heap_array;
        $str = "";
        $str .="                           ".$a[1]."\n";
        $str .="             ".$a[2]."                           ".$a[3]."\n";
        $str .="      ".$a[4]."             ".$a[5]."             ".$a[6]."             ".$a[7]."\n";
        $str .="   ".$a[8]."      ".$a[9]."      ".$a['10']."\n";
        return $str;
    }
}