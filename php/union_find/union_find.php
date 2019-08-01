<?php
/**
 * 经典并查集
 * 键为元素值，值为父节点，顶级节点的父节点指向自己
 */
class UnionFind{
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
     * 循环判断集中的键和值是否相同，不同则向上循环；
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
     * 并操作
     * 找出两键值的顶级节点；
     * 判断是否相同，如果相同则不操作；
     * 将一个顶级节点指向另一个顶级节点；
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