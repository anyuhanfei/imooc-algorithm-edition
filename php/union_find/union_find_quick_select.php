<?php
/**
 * 快速查询版并查集
 */
class UnionFindQuickSelect{
    public $root = array();
    public $count = array();

    /**
     * 统计传入键值数量，并将键值存放到并查集中，初始时每个节点单独分组
     *
     * @param array $init_list 添加数组
     */
    public function __construct($init_list = array()){
        $this->count = count($init_list);
        foreach($init_list as $v){
            $this->root[$v] = $v;
        }
    }

    /**
     * 查操作
     * 判断传入键值范围；
     * 返回节点的分组（值）
     *
     * @param int $key 键
     * @return void
     */
    public function find($key){
        if($key < 0 || $key >= $this->count){
            return null;
        }
        return $this->root[$key];
    }

    /**
     * 判断两键值是否在同一组
     *
     * @param int $p 键值
     * @param int $q 键值
     * @return boolean
     */
    public function isConnected($p, $q){
        return $this->root[$q] == $this->root[$p];
    }

    /**
     * 并操作
     * 获取靓键值的分组，如果相同则已经在同一组；
     * 遍历集，将其中一个分组的节点全部修改为另一个分组。
     *
     * @param int $p 键值
     * @param int $q 键值
     * @return void
     */
    public function unionElements($p, $q){
        $p_id = $this->root[$p];
        $q_id = $this->root[$q];
        if($p_id == $q_id){
            return;
        }
        foreach($this->root as $k => $v){
            if($this->root[$k] == $p_id){
                $this->root[$k] = $q_id;
            }
        }
    }
}