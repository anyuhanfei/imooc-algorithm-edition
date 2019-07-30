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

    public function __destruct(){
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

    /**
     * 深度优先遍历
     * 对二叉搜索树进行后序遍历，引用方法
     *
     * @return void
     */
    public function pre_order(){
        $this->_pre_order($this->root);
    }

    /**
     * 对二叉搜索树进行前序遍历，执行方法
     * 如果节点不为空，则打印自身并以此递归左子节点和右子节点
     *
     * @param obj $node 节点
     * @return void
     */
    private function _pre_order($node){
        if($node != null){
            print_r("{key: " . $node->key . ", value: " . $node->value . "}\n");
            $this->_pre_order($node->left);
            $this->_pre_order($node->right);
        }
    }

    /**
     * 深度优先遍历
     * 对二叉搜索树进行中序遍历，引用方法
     *
     * 从小到大依次遍历，可应用于排序情景;
     *
     * @return void
     */
    public function in_order(){
        $this->_in_order($this->root);
    }

    /**
     * 对二叉搜索树进行中序遍历，执行方法
     * 如果节点不为空，则递归左子节点，然后打印自身，最后递归右子节点
     *
     * @param obj $node 节点
     * @return void
     */
    private function _in_order($node){
        if($node != null){
            $this->_in_order($node->left);
            print_r("{key: " . $node->key . ", value: " . $node->value . "}\n");
            $this->_in_order($node->right);
        }
    }

    /**
     * 深度优先遍历
     * 对二叉搜索树进行后序遍历，引用方法
     *
     * 从底层到顶层遍历，可用于删除情景;
     *
     * @return void
     */
    public function post_order(){
        $this->_post_order($this->root);
    }

    /**
     * 对二叉搜索树进行后序遍历，执行方法
     * 如果节点不为空，则递归左子节点，然后递归右子节点，最后打印自身
     *
     * @param obj $node 节点
     * @return void
     */
    private function _post_order($node){
        if($node != null){
            $this->_post_order($node->left);
            $this->_post_order($node->right);
            print_r("{key: " . $node->key . ", value: " . $node->value . "}\n");
        }
    }

    /**
     * 广度优先遍历
     * 层序遍历
     *
     * 引入一个队列，将跟节点入队；
     * while循环，判断队列是否为空，如果不为空则循环；
     * 循环中，将队首的元素拿出并出队，然后将它左右子节点入队，直至最后一层；
     *
     * @return void
     */
    public function level_order(){
        $queue = array($this->root);
        while($queue != array()){
            $node = array_shift($queue);
            print_r("{key: " . $node->key . ", value: " . $node->value . "}\n");
            if($node->left != null){
                array_push($queue, $node->left);
            }
            if($node->right != null){
                array_push($queue, $node->right);
            }
        }
    }

    /**
     * 寻找最小值的键值，引用方法
     *
     * @param string $type 执行方法
     * @return null or string
     */
    public function minimum($type = "recursion"){
        if($this->root == null){
            return null;
        }
        if($type == "recursion"){
            return $this->_minimum_recursion($this->root);
        }else{
            return $this->_minimum_iteration($this->root);
        }
    }

    /**
     * 寻找最小值的键值，执行方法，递归版
     * 向左查询，直到某个节点没有左节点，那么此节点即为最小值的节点；
     *
     * @param obj $node 节点
     * @return void
     */
    private function _minimum_recursion($node){
        if($node->left == null){
            return $node->key;
        }
        return $this->_minimum_recursion($node->left);
    }

    /**
     * 寻找最小值的键值，执行方法，迭代版
     * 如果节点的左子节点不为空，则一直循环，直到节点的左子节点为空；
     *
     * @param obj $node 节点
     * @return void
     */
    private function _minimum_iteration($node){
        while($node->left != null){
            $node = $node->left;
        }
        return $node->key;
    }

    /**
     * 寻找最大值的键值，引用方法
     *
     * @param string $type 执行方法
     * @return void
     */
    public function maximum($type = "recursion"){
        if($this->root == null){
            return null;
        }
        if($type == "recursion"){
            return $this->_maximum_recursion($this->root);
        }else{
            return $this->_maximum_iteration($this->root);
        }
    }

    /**
     * 寻找最大值的键值，执行方法，递归版
     * 判断节点的右子节点是否为空，如果是则返回节点的键值；否则递归节点的右子节点；
     *
     * @param obj $node 节点
     * @return void
     */
    private function _maximum_recursion($node){
        if($node->right == null){
            return $node->key;
        }
        return $this->_maximum_recursion($node->right);
    }

    /**
     * 寻找最大值的键值，执行方法，迭代版
     * 如果节点的右子节点不为空，则执行循环，将右子节点替换为当前节点继续进行判断，直到节点的右子节点为空
     *
     * @param obj $node 节点
     * @return void
     */
    private function _maximum_iteration($node){
        while($node->right != null){
            $node = $node->right;
        }
        return $node->key;
    }

    /**
     * 删除掉最小值所在的节点，引用方法
     *
     * @param string $type 执行方法
     * @return void
     */
    public function remove_min($type = "recursion"){
        if($this->root != null){
            if($type == "recursion"){
                $this->_remove_min_recursion($this->root);
            }else{
                $this->_remove_min_iteration($this->root);
            }
        }
    }

    /**
     * 删除掉最小值所在的节点，执行方法，递归版
     * 判断节点的左子节点是否为空，如果为空则获取此节点的右子节点并删除此节点，树的元素个数减一，返回右子节点；
     * 如果节点不为空，则递归节点的左子节点，并且将结果赋值给节点的左子节点，返回此节点；
     *
     * @param obj $node 节点
     * @return void
     */
    private function _remove_min_recursion(&$node){
        if($node->left == null){
            $right = $node->right;
            unset($node);
            $this->count--;
            return $right;
        }
        $node->left = $this->_remove_min_recursion($node->left);
        return $node;
    }

    /**
     * 删除掉最小值所在的节点，执行方法，迭代版
     * while循环，判断节点是否为空，为空则跳出循环；
     * 循环中，判断节点的左子节点的左子节点是否为空，如果是则将节点的左子节点的右子节点移动到节点的左子节点上(删除最小值，将最小值所在的节点的右字节移动)；
     * 树的节点数减一；
     *
     * @param obj $node 节点
     * @return void
     */
    private function _remove_min_iteration($node){
        while($node != null){
            if($node->left->left == null){
                $node->left = $node->left->right;
                $this->count--;
                break;
            }
            $node = $node->left;
        }
    }

    /**
     * 删除掉最大值所在的节点，引用方法
     *
     * @param string $type 执行方法
     * @return void
     */
    public function remove_max($type = "recursion"){
        if($this->root != null){
            if($type == "recursion"){
                $this->_remove_max_recursion($this->root);
            }else{
                $this->_remove_max_iteration($this->root);
            }
        }
    }

    /**
     * 删除掉最大值所在的节点，执行方法，递归版
     * 原理同删除最小值所在的节点方法
     *
     * @param obj $node 节点
     * @return void
     */
    private function _remove_max_recursion($node){
        if($node->right == null){
            $left = $node->left;
            unset($node);
            $this->count--;
            return $left;
        }
        $node->right = $this->_remove_max_recursion($node->right);
        return $node;
    }

    /**
     * 删除掉最大值所在的节点，执行方法，迭代版
     * 原理同删除最小值所在的节点方法
     *
     * @param obj $node 节点
     * @return void
     */
    private function _remove_max_iteration($node){
        while($node != null){
            if($node->right->right == null){
                $node->right = $node->right->left;
                $this->count--;
                break;
            }
            $node = $node->right;
        }
    }

    public function remove($key){
        $this->root = $this->_remove($this->root, $key);
    }

    private function _remove($node, $key){
        if($node == null){
            return null;
        }elseif($key < $node->key){
            $node->left = $this->_remove($node->left, $key);
            return $node;
        }elseif($key > $node->key){
            $node->right = $this->_remove($node->right, $key);
            return $node;
        }else{
            if($node->left == null){
                $right = $node->left;
                $this->count--;
                return $right;
            }
            if($node->right == null){
                $left = $node->right;
                $this->count--;
                return $left;
            }
            $temp_node = $node->right;
            while($temp_node->left != null){
                $temp_node = $temp_node->left;
            }
            $successor = new TreeNode($temp_node->key, $temp_node->value);
            $this->_remove_min_recursion($node->right);
            $successor->left = $node->left;
            $successor->right = $node->right;
            return $successor;
        }
    }
}


$tree = new BinarySearchTree();
$tree->insert(28, 'a');
$tree->insert(16, 'b');
$tree->insert(30, 'c');
$tree->insert(13, 'd');
$tree->insert(22, 'e');
$tree->insert(29, 'f');
$tree->insert(42, 'g');
$tree->insert(14, 'h');
$tree->insert(41, 'i');
$tree->remove(28);
print_r($tree->root);