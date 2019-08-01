<?php
/**
 * 并查集rank优化版
 * 添加一个rank字典来统计此节点下级有多少层级，在并操作中，层级少的顶级节点指向层级多的顶级节点
 */
class UnionFindRank{
    public $root = array();
    public $rank = array();
    public $count = 0;

    public function __construct($init_list = array()){
        $this->count = count($init_list);
        foreach($init_list as $v){
            $this->root[$v] = $v;
            $this->rank[$v] = 1;
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
        return $this->find($p) == $this->find($q);
    }

    /**
     * 并操作
     * 找出两键值的顶级节点；
     * 判断是否相同，如果相同则不操作；
     * 判断两顶级节点的子节点层级，子节点层级少的顶级节点指向子节点层级多的顶级节点；
     * 如果相等，则随意指向，最终的顶级节点的层级统计加一；
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
        if($this->rank[$p_root] > $this->rank[$q_root]){
            $this->root[$q_root] = $p_root;
        }elseif($this->rank[$p_root] < $this->rank[$q_root]){
            $this->root[$p_root] = $q_root;
        }elseif($this->rank[$p_root] == $this->rank[$q_root]){
            $this->root[$p_root] = $q_root;
            $this->rank[$q_root]++;
        }
    }
}