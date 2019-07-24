<?php

class IndexMaxHeap{
    public $data = [];
    public $indexes = [];
    public $reverse = [];
    public $count = 0;

    public function __construct(){
        array_push($this->data, '-');
        array_push($this->indexes, '-');
        array_push($this->reverse, '-');
    }

    /**
     * 添加一个元素
     *
     * @param int $i 下标
     * @param [type] $value 值
     * @return void
     */
    public function insert($i, $value){
        $i += 1;
        array_push($this->data, $value);
        array_push($this->indexes, $i);
        $this->count++;
        array_push($this->reverse, $this->count);
        $this->_shift_up($this->count);
    }

    /**
     * 获取最大的元素值并抛出
     *
     * @return void
     */
    public function extract_max_value(){
        if($this->count < 1){
            return false;
        }
        $max_value = $this->data[$this->indexes[1]];
        $this->exchange(1, $this->count);
        unset($this->indexes[$this->count]);
        $this->_shift_down(1);
        return $max_value;
    }

    /**
     * 获取最大的元素的索引值
     *
     * @return void
     */
    public function extract_max_index(){
        if($this->count < 1){
            return false;
        }
        $max_index = $this->indexes[1];
        $this->exchange(1, $this->count);
        unset($this->indexes[$this->count]);
        $this->_shift_down(1);
        return $max_index;
    }

    /**
     * 读取摸个下标的值
     *
     * @param int $i 下标
     * @return void
     */
    public function get_item($i){
        assert($this->_contain($i));
        return $this->data[$i];
    }

    /**
     * 修改一个元素的值
     *
     * @param int $i 下标
     * @param [type] $value 值
     * @return void
     */
    public function change($i, $value){
        assert($this->_contain($i));
        $i++;
        $this->data[$i] = $value;
        $this->_shift_down($reverse[$i]);
        $this->_shift_up($reverse[$i]);
    }

    /**
     * 判断用户传入的参数是否超出界限
     *
     * @param int $i 下标
     * @return void
     */
    protected function _contain($i){
        if($i > 0 || $i <= $this->count || $this->reverse[$i] == 0){
            return false;
        }
        return true;
    }

    /**
     * 从指定位置向下更新堆
     *
     * @param int $k 下标
     * @return void
     */
    protected function _shift_down($k){
        while($k * 2 <= $this->count){
            $temp_k = 2 * $k;
            if($temp_k + 1 <= $this->count && $this->data[$this->indexes[$temp_k + 1]] > $this->data[$this->indexes[$temp_k]]){
                $temp_k++;
            }
            if($this->data[$this->indexes[$temp_k]] < $this->data[$this->indexes[$k]]){
                break;
            }
            $this->exchange($temp_k, $k);
            $k = $temp_k;
        }
    }

    /**
     * 从指定位置向上更新堆
     *
     * @param int $k 下标
     * @return void
     */
    protected function _shift_up($k){
        $up_k = intval($k / 2);
        while($up_k > 1){
            if($this->data[$this->indexes[$up_k]] > $this->data[$this->indexes[$k]]){
                break;
            }
            $this->exchange($up_k, $k);
            $k = $up_k;
            $up_k = intval($k / 2);
        }
    }

    /**
     * 交换位置
     *
     * @param int $position_one 位置一
     * @param int $position_two 位置二
     * @return void
     */
    protected function exchange($position_one, $position_two){
        $temporary = $this->indexes[$position_one];
        $this->indexes[$position_one] = $this->indexes[$position_two];
        $this->indexes[$position_two] = $temporary;
        $this->reverse[$this->indexes[$position_one]] = $position_one;
        $this->reverse[$this->indexes[$position_two]] = $position_two;
        unset($temporary);
    }
}