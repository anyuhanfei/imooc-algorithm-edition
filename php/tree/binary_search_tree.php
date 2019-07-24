<?php
class TreeNode{
    public function __construct($key, $value, $left = null, $right = null){
        $this->key = $key;
        $this->value = $value;
        $this->left = $left;
        $this->right = $right;
    }
}

class BinarySearchTree{
    /**
     * 初始化数据
     *
     * @param array|null root 树
     * @param int count 二叉树中的节点总数
     */
    public function __construct(){
        $this->root = null;
        $this->count = 0;
    }

    /**
     * 在二叉树上添加节点，引用方法
     *
     * @param string $key 键
     * @param string|array $value 值
     * @param string $type 执行方法
     * @return void
     */
    public function insert($key, $value, $type = "iteration"){
        if($this->root == null){
            $this->root = new TreeNode($key, $value);
        }else{
            if($type == "iteration"){
                $this->_insert_iteration($this->root, $key, $value);
            }else{
                $this->_insert_recursion($this->root, $key, $value);
            }
        }
        $this->count++;
    }

    /**
     * 在二叉树上添加节点，执行方法，迭代版
     *
     * @param object $node 当前节点
     * @param string $key 键
     * @param string $value 值
     * @return void
     */
    private function _insert_iteration($node, $key, $value){
        while($node != null){
            if($node->key == $key){
                $node->value = $value;
                $this->count--;
                return;
            }elseif($node->key > $key){
                if($node->left == null){
                    $node->left = new TreeNode($key, $value);
                    return;
                }else{
                    $node = $node->left;
                }
            }else{
                if($node->right == null){
                    $node->right = new TreeNode($key, $value);
                    return;
                }else{
                    $node = $node->right;
                }
            }
        }
        return;
    }

    /**
     * 在二叉树上添加节点，执行方法，递归版
     *
     * @param object $node 当前节点
     * @param string $key 键
     * @param string $value 值
     * @return void
     */
    private function _insert_recursion($node, $key, $value){
        if($node->key == $key){
            $node->value = $value;
            $this->count--;
        }elseif($node->key > $key){
            if($node->left == null){
                $node->left = new TreeNode($key, $value);
                return;
            }else{
                $this->_insert_recursion($node->left, $key, $value);
            }
        }else{
            if($node->right == null){
                $node->right = new TreeNode($key, $value);
                return;
            }else{
                $this->_insert_recursion($node->right, $key, $value);
            }
        }
    }

    /**
     * 获取一个键对应的值，引用方法
     *
     * @param string $key 键
     * @param string $type 执行方法选择，iteration：迭代版；recursion：递归版
     * @return string|null
     */
    public function get($key, $type = "iteration"){
        if($this->root != null){
            if($this->root->key == $key){
                return $this->root->value;
            }else{
                if($type == "iteration"){
                    $res = $this->_get_iteration($this->root, $key);
                }else{
                    $res = $this->_get_recursion($this->root, $key);
                }
                return $res != null ? $res->value : null;
            }
        }else{
            return null;
        }
    }

    /**
     * 获取一个键对应的值，执行方法，递归版
     *
     * @param object $node 当前节点
     * @param string $key 键
     * @return object|null
     */
    private function _get_recursion($node, $key){
        if($node == null){
            return null;
        }
        if($node->key == $key){
            return $node;
        }elseif($node->key > $key){
            return $this->_get_recursion($node->left, $key);
        }else{
            return $this->_get_recursion($node->right, $key);
        }
        return null;
    }

    /**
     * 获取一个键对应的值，执行方法，迭代版
     *
     * @param object $node 当前节点
     * @param string $key 键
     * @return void
     */
    private function _get_iteration($node, $key){
        while($node != null){
            if($node->key == $key){
                return $node;
            }elseif($node->key > $key){
                $node = $node->left;
            }else{
                $node = $node->right;
            }
        }
        return null;
    }
}


$b = new BinarySearchTree();
for($i=0;$i<10;$i++){
    $value = $i + 100;
    $b->insert($i, $value, 'recursion');
}
print_r($b->root);
print_r($b->get(4, 'iteration'));