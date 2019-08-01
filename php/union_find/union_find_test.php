<?php
require "../generated_data.php";
require "union_find_quick_select.php";
require "union_find.php";
require "union_find_sz.php";
require "union_find_rank.php";
require "union_find_path_compression.php";

class UnionFindTest{
    public function test_one($n){
        $start_time = time() + microtime(true);
        $data = orderly_array(0, $n + 1);
        $union = new UnionFindQuickSelect($data);
        for($i = 0; $i < $n; $i++){
            $union->unionElements(mt_rand(0, $n), mt_rand(0, $n));
        }
        for($i = 0; $i < $n; $i++){
            $union->isConnected(mt_rand(0, $n), mt_rand(0, $n));
        }
        $end_time = time() + microtime(true);
        print_r('快速查询版并查集运行时间:' . ($end_time - $start_time) . "\n");
    }

    public function test_two($n){
        $start_time = time() + microtime(true);
        $data = orderly_array(0, $n + 1);
        $union = new UnionFind($data);
        for($i = 0; $i < $n; $i++){
            $union->unionElements(mt_rand(0, $n), mt_rand(0, $n));
        }
        for($i = 0; $i < $n; $i++){
            $union->isConnected(mt_rand(0, $n), mt_rand(0, $n));
        }
        $end_time = time() + microtime(true);
        print_r('并查集运行时间:' . ($end_time - $start_time) . "\n");
    }

    public function test_three($n){
        $start_time = time() + microtime(true);
        $data = orderly_array(0, $n + 1);
        $union = new UnionFindSz($data);
        for($i = 0; $i < $n; $i++){
            $union->unionElements(mt_rand(0, $n), mt_rand(0, $n));
        }
        for($i = 0; $i < $n; $i++){
            $union->isConnected(mt_rand(0, $n), mt_rand(0, $n));
        }
        $end_time = time() + microtime(true);
        print_r('sz优化版并查集运行时间:' . ($end_time - $start_time) . "\n");
    }

    public function test_four($n){
        $start_time = time() + microtime(true);
        $data = orderly_array(0, $n + 1);
        $union = new UnionFindRank($data);
        for($i = 0; $i < $n; $i++){
            $union->unionElements(mt_rand(0, $n), mt_rand(0, $n));
        }
        for($i = 0; $i < $n; $i++){
            $union->isConnected(mt_rand(0, $n), mt_rand(0, $n));
        }
        $end_time = time() + microtime(true);
        print_r('rank优化版并查集运行时间:' . ($end_time - $start_time) . "\n");
    }

    public function test_five($n){
        $start_time = time() + microtime(true);
        $data = orderly_array(0, $n + 1);
        $union = new UnionFindPathCompression($data);
        for($i = 0; $i < $n; $i++){
            $union->unionElements(mt_rand(0, $n), mt_rand(0, $n));
        }
        for($i = 0; $i < $n; $i++){
            $union->isConnected(mt_rand(0, $n), mt_rand(0, $n));
        }
        $end_time = time() + microtime(true);
        print_r('路径压缩版并查集运行时间:' . ($end_time - $start_time) . "\n");
    }
}

$n = 100000;
$test = new UnionFindTest();
$test->test_one($n);
$test->test_two($n);
$test->test_three($n);
$test->test_four($n);
$test->test_five($n);