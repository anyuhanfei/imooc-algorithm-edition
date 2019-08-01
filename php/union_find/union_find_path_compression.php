<?php
/**
 * 并查集--路径压缩
 */
class UnionFindPathCompression{
    public $root = array();
    public $count = 0;

    public function __construct($init_list = array()){
        $this->count = count($init_list);
        foreach($init_list as $v){
            $this->root[$v] = $v;
        }
    }

    /**
     * 查操作
     * 判断传入键值是否超出范围；
     * 循环判断集中的键和值是否相同，不同则向上循环，循环内，当前节点的父节点更新为父节点的父节点；
     * 相同则返回键值；
     *
     * @param int $key 键值
     * @return void
     */
    public function find($key){
        if($key < 0 || $key >= $this->count){
            return null;
        }
        while($this->root[$key] != $key){
            $this->root[$key] = $this->root[$this->root[$key]];
            $key = $this->root[$key];
        }
        return $key;
    }

    /**
     * 判断两键值是否连接
     *
     * @param int $p 键值
     * @param int $q 键值
     * @return boolean
     */
    public function isConnected($p, $q){
        return $this->find($q) == $this->find($p);
    }

    /**
     * 并操作，无优化版
     *
     * @param int $p 键值
     * @param int $q 键值
     * @return void
     */
    public function unionElements($p, $q){
        $p_root = $this->find($p);
        $q_root = $this->find($q);
        if($p_root == $q_root){
            return;
        }
        $this->root[$p_root] = $q_root;
    }
}