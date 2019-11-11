<?php
/**
 * 稠密图--邻接矩阵
 *
 * @param int $n_count 节点数
 * @param int $m_count 连接数
 * @param boolean $directed 是否是有向图
 * @param array $vector 图
 */
class DenseGraph{
    private $n_count = 0;
    private $m_count = 0;
    private $directed = false;
    public $vector = array();

    /**
     * 初始化
     *
     * @param [type] $init_list
     * @param boolean $directed
     */
    public function __construct($init_list, $directed = false){
        $this->n_count = count($init_list);
        $this->directed = $directed;
        foreach($init_list as $v){
            $this->vector[$v] = array();
            foreach($init_list as $b){
                $this->vector[$v][$b] = false;
            }
        }
    }

    /**
     * 节点数
     *
     * @return void
     */
    public function v(){
        return $this->n_count;
    }

    /**
     * 连接数
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
        if($this->hasEdge($v, $w)){
            return;
        }
        $this->m_count++;
        $this->vector[$v][$w] = true;
        if($this->directed == false){
            $this->vector[$w][$v] = true;
        }
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
     * 判断两个节点是否已连接
     *
     * @param [type] $v
     * @param [type] $w
     * @return boolean
     */
    public function hasEdge($v, $w){
        assert(array_key_exists($v, $this->vector));
        assert(array_key_exists($w, $this->vector));
        return $this->vector[$v][$v];
    }

    /**
     * 返回一个节点的所有连接节点合集，简易的进行了拼接
     *
     * @param [type] $k
     * @return void
     */
    public function getEdge($k){
        assert(array_key_exists($k, $this->vector));
        $return_data = '';
        $return_data .= '{' . $k . ': ';
        foreach($this->vector[$k] as $key => $i){
            if($i == 1){
                $return_data .= $key . ', ';
            }
        }
        $return_data = substr($return_data, 0, strlen($return_data) - 2);
        $return_data .= "}\n";
        return $return_data;
    }

    /**
     * 返回所有节点的连接节点合集，简易的进行了拼接
     *
     * @return void
     */
    public function getAllEdge(){
        $return_data = '';
        foreach($this->vector as $k => $v){
            $return_data .= $this->getEdge($k);
        }
        return $return_data;
    }
}