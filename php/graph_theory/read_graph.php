<?php
include "dense_graph.php";
include "sparse_graph.php";


/**
 * 通过传入图连接类型和文件路径，来创建一个图，并传入数据
 */
class ReadGraph{
    private $graph = null;
    public function __construct($graph_type, $file_name){
        $file = fopen($file_name, 'r');
        $file_read = fread($file, filesize($file_name));
        $file_read = str_replace(" ", "\n", $file_read);
        $file_read_array = explode("\n", $file_read);
        $number = 1;
        $init_list = array();
        $len = count($file_read_array);
        for($i = 0; $i < $len; $i++){
            if($i == 0){
                for($ii = 0; $ii < $file_read_array[$i]; $ii++){
                    array_push($init_list, $ii);
                }
                $this->graph = $graph_type == 'sparse' ? new SparseGraph($init_list) : new DenseGraph($init_list);
                continue;
            }
            if($i % 2 == 0){
                $this->graph->addEdge(intval($file_read_array[$i - 1]), intval($file_read_array[$i]));
            }
        }
    }

    public function get_graph(){
        return $this->graph->getVector();
    }

    public function print_all_edge(){
        print_r($this->graph->getAllEdge());
    }
}

$rgd = new ReadGraph('dense', './testG1.txt');
$rgd->print_all_edge();
print_r("\n");
$rgs = new ReadGraph('sparse', './testG1.txt');
$rgs->print_all_edge();