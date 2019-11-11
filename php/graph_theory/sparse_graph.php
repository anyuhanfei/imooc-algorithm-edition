<?php
/**
 * 稀疏图--邻接表
 *
 * @param int $n_count 节点数
 * @param int $m_count 连接数
 * @param boolean $directed 是否是有向图
 * @param array $vector 图
 */
class SparseGraph{
    private $n_count = 0;
    private $m_count = 0;
    private $directed = false;
    private $vector = array();

    /**
     * 初始化数据
     *
     * @param array $init_list 节点合集
     * @param boolean $directed 有向图标识
     */
    public function __construct($init_list, $directed = false){
        $this->directed = $directed;
        $this->n_count = count($init_list);
        foreach($init_list as $v){
            $this->vector[$v] = array();
        }
    }

    /**
     * 返回节点数
     *
     * @return void
     */
    public function v(){
        return $this->n_count;
    }

    /**
     * 返回连接数
     *
     * @return void
     */
    public function e(){
        return $this->m_count;
    }

    /**
     * 添加连接
     * 将要连接的节点添加进本节点的数组中
     *
     * @param [type] $v
     * @param [type] $w
     * @return void
     */
    public function addEdge($v, $w){
        $this->hasEdge($v, $w);
        $this->m_count++;
        array_push($this->vector[$v], $w);
        if($this->directed == false){
            array_push($this->vector[$w], $v);
        }
    }

    /**
     * 判断两个节点是否已连接
     *
     * @param [type] $v
     * @param [type] $w
     * @return boolean
     */
    public function hasEdge($v, $w){
        assert(array_key_exists($v, $this->vector));
        assert(array_key_exists($w, $this->vector));
        if(in_array($w, $this->vector[$v])){
            return true;
        }
        return false;
    }

    /**
     * 返回图存储，便于类外读取并保证数据安全
     *
     * @return void
     */
    public function getVector(){
        return $this->vector;
    }

    /**
     * 返回一个节点的所有连接节点合集，简易的进行了拼接
     *
     * @param [type] $v
     * @return void
     */
    public function getEdge($v){
        assert(in_array($v, $this->vector));
        return '{'. $v . ': ' . implode($this->vector[$v]) . '}';
    }

    /**
     * 返回所有节点的连接节点合集，简易的进行了拼接
     *
     * @return void
     */
    public function getAllEdge(){
        $return_data = '';
        foreach($this->vector as $k => $v){
            $return_data .= '{'. $k . ': ' . implode($v, ',') . "}\n";
        }
        return $return_data;
    }
}