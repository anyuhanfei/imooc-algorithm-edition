<?php
include_once("max_heap.php");
include_once("../generated_data.php");

/**
 * 堆排序一，将未排序数组元素一一添加入堆中
 *
 * @param array $init_array
 * @return void
 */
function heap_sort_one($init_array){
    $max_heap = new MaxHeap();
    foreach($init_array as $v){
        $max_heap->insert($v);
    }
    $count = $max_heap->size();
    for($i=0; $i < $count; $i++){
        $init_array[$i] = $max_heap->extract_max();
    }
    return $init_array;
}

/**
 * 堆排序二，将未排序数组一次添加入堆中
 *
 * @param array $init_array
 * @return void
 */
function heap_sort_two($init_array){
    $max_heap = new MaxHeap();
    $max_heap->all_insert_heap($init_array);
    $count = $max_heap->size();
    for($i=0; $i < $count; $i++){
        $init_array[$i] = $max_heap->extract_max();
    }
    return $init_array;
}

/**
 * 排序三：原地堆排序
 * 原地堆排序的顶节点下标为0
 */
class heap_sort_three{
    /**
     * 排序方法
     * 计算数组元素个数，从后向前依次对有子节点的节点进行堆条件判断；
     * 从后向前循环，依次于下标0的元素交换位置，并对下标0进行堆条件判断
     *
     * @param array $init_array 未排序数组，直接对此数组进行操作
     * @return void
     */
    public function heap_sort(&$init_array){
        $n = count($init_array);
        for($i = intval(($n - 1) / 2); $i >= 0; $i--){
            $this->_shift_down($init_array, $n, $i);
        }
        for($i = $n - 1; $i > 0; $i--){
            exchange($init_array, $i, 0);
            $this->_shift_down($init_array, $i, 0);
        }
    }

    /**
     * 从指定位置向下进行堆条件判断
     *
     * @param array $init_array 未进行堆条件判断的堆
     * @param int $n 堆的元素个数
     * @param int $i 指定下标
     * @return void
     */
    private function _shift_down(&$init_array, $n, $i){
        while($i * 2 + 1 < $n){
            $j = $i * 2 + 1;
            if($j + 1 < $n && $init_array[$j + 1] > $init_array[$j]){
                $j = $j + 1;
            }
            if($init_array[$j] < $init_array[$i]){
                break;
            }
            exchange($init_array, $j, $i);
            $i = $j;
        }
    }
}


/**
 * 位置交换函数
 *
 * @param array $array 数组
 * @param int $position_one 下标1
 * @param int $position_two 下标2
 * @return void
 */
function exchange(&$array, $position_one, $position_two){
    $temporary = $array[$position_one];
    $array[$position_one] = $array[$position_two];
    $array[$position_two] = $temporary;
    unset($temporary);
}


$init_array = disorderly_array(1000000, 0, 1000000);
$s_time = time();
$heap_sort_three = new heap_sort_three();
$heap_sort_three->heap_sort($init_array);
$e_time = time();
print_r("运行时间：". ($e_time - $s_time). 's');