<?php
/**
 * 并查集sz优化版
 * 添加一个sz字典来统计此节点下级有多少个节点，在并操作中，节点少的顶级节点指向节点多的顶级节点
 */
class UnionFindSz{
    public $root = array();
    public $sz = array();
    public $count = 0;

    public function __construct($init_list = array()){
        $this->count = count($init_list);
        foreach($init_list as $v){
            $this->root[$v] = $v;
            $this->sz[$v] = 1;
        }
    }

    /**
     * 查操作
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
     * @return void
     */
    public function isConnected($p, $q){
        return $this->find($q) == $this->find($p);
    }

    /**
     * 并操作
     * 找出两键值的顶级节点；
     * 判断是否相同，如果相同则不操作；
     * 判断两顶级节点的子节点数量，数量少的顶级节点指向数量多的顶级节点；
     * 更新顶级节点的子节点数；
     *
     * @param int $p 键值
     * @param int $q 键值
     * @return void
     */
    public function unionElements($p, $q){
        $p_root = $this->find($p);
        $q_root = $this->find($q);
        if($q_root == $p_root){
            return;
        }
        if($this->sz[$p_root] > $this->sz[$q_root]){
            $this->root[$q_root] = $p_root;
            $this->sz[$p_root] += $this->sz[$q_root];
        }else{
            $this->root[$p_root] = $q_root;
            $this->sz[$q_root] += $this->sz[$p_root];
        }
    }
}