import queue


class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        '''初始化二叉树'''
        self.root = None
        self.count = 0

    def __del__(self):
        '''删除所有节点，释放内存'''
        self._remove_post_order(self.root)
        self.count = 0

    def insert(self, key, value, type="iteration"):
        '''向二叉树中添加节点，引用方法
        如果root是空则直接将添加至root节点上，否则执行执行方法；
        二叉树节点总数加一；

        Arge：
            key：要添加的键
            value：要添加的值
            type：方法选择
                iteration：迭代版执行方法
                recursion：递归版执行方法
        '''
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            if type == "iteration":
                self._insert_iteration(self.root, key, value)
            else:
                self._insert_recursion(self.root, key, value)
        self.count += 1

    def _insert_recursion(self, node, key, value):
        '''向二叉树中添加节点，执行方法（递归版）
        如果有相同的键则修改值，并且树的元素总数减一（因为提前加一，而此情况没有添加新节点）；
        如果添加节点的key小于当前节点，则向左递归，如果左子节点不存在则直接添加至左子节点上；
        右子节点的判断与左子节点相同；
        注意：不能直接修改节点本身（这样做只是修改了局部变量的值），只能修改当前节点的左右节点；

        Arge：
            node：当前节点
            key：要添加的键
            value：要添加的值
        '''
        if node.key == key:
            node.value = value
            self.count -= 1
        elif node.key > key:
            if node.left is None:
                node.left = TreeNode(key, value)
            else:
                self._insert_recursion(node.left, key, value)
        else:
            if node.right is None:
                node.right = TreeNode(key, value)
            else:
                self._insert_recursion(node.right, key, value)

    def _insert_iteration(self, node, key, value):
        '''向二叉树中添加节点，执行方法（迭代版）
        如果节点不为空则一直循环；
        如果有相同的键则修改值，并且树的元素总数减一（因为提前加一，而此情况没有添加新节点）；
        如果添加节点的key小于当前节点，则向左递归，如果左子节点不存在则直接添加至左子节点上；
        右子节点的判断与左子节点相同；
        注意：不能直接修改节点本身（这样做只是修改了局部变量的值），只能修改当前节点的左右节点；

        Arge：
            node：当前节点
            key：要添加的键
            value：要添加的值
        '''
        while node is not None:
            if node.key == key:
                node.value = value
                self.count -= 1
                return
            elif node.key > key:
                if node.left is None:
                    node.left = TreeNode(key, value)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(key, value)
                    return
                else:
                    node = node.right

    def __setitem__(self, key, value):
        return self.insert(key, value)

    def get(self, key, type="iteration"):
        '''查找二叉树中的某个节点，引用方法

        Arge:
            key：要添加的键
            type：方法选择
                iteration：迭代版执行方法
                recursion：递归版执行方法
        return：
            None或节点的值
        '''
        if self.root is not None:
            res = self._get_iteration(self.root, key) if type == 'iteration' else self._get_recursion(self.root, key)
            return None if res is None else res.value
        else:
            return None

    def _get_recursion(self, node, key):
        '''查找二叉树中的某个节点，执行方法，递归版
        如果当前节点为None则返回None；
        如果当前节点的键等于指定的键则返回这个节点；
        如果当前节点的键大于指定的键则向左子节点递归；
        如果当前节点的键小于指定的键则向右子节点递归；
        没有符合要求的值返回None；

        Agre：
            node：当前节点
            key：要查找的键
        return：
            None或节点对象
        '''
        if node is None:
            return None
        if node.key == key:
            return node
        elif node.key > key:
            return self._get_recursion(node.left, key)
        else:
            return self._get_recursion(node.right, key)
        return None

    def _get_iteration(self, node, key):
        '''查找二叉树中的某个节点，执行方法，迭代版
        如果节点不为空则持续循环；
        如果当前节点的键等于指定的键则返回这个节点；
        如果当前节点的键大于指定的键则向左子节点递归；
        如果当前节点的键小于指定的键则向右子节点递归；
        没有符合要求的值返回None；

        Agre：
            node：当前节点
            key：要查找的键
        return：
            None或节点对象
        '''
        while node is not None:
            if node.key == key:
                return node
            elif node.key > key:
                node = node.left
            else:
                node = node.right
        return None

    def __getitem__(self, key):
        return self.get(key)

    def pre_order(self):
        '''深度优先遍历
        对二叉搜索树进行前序遍历，引用方法
        '''
        self._pre_order(self.root)

    def _pre_order(self, node):
        '''对二叉搜索树进行前序遍历，执行方法
        如果节点不为空，则打印自身并以此递归左子节点和右子节点

        Agre:
            node: 节点
        '''
        if node is not None:
            print('{key: %s, value: %s}' % (node.key, node.value))
            self._pre_order(node.left)
            self._pre_order(node.right)

    def in_order(self):
        '''深度优先遍历
        对二叉搜索树进行中序遍历，引用方法

        从小到大依次遍历，可应用于排序情景;
        '''
        self._in_order(self.root)

    def _in_order(self, node):
        '''对二叉搜索树进行中序遍历，执行方法
        如果节点不为空，则递归左子节点，然后打印自身，最后递归右子节点

        Agre:
            node: 节点
        '''
        if node is not None:
            self._in_order(node.left)
            print('{key: %s, value: %s}' % (node.key, node.value))
            self._in_order(node.right)

    def post_order(self):
        '''深度优先遍历
        对二叉搜索树进行后序遍历，引用方法

        从底层到顶层遍历，可用于删除情景;
        '''
        self._post_order(self.root)

    def _post_order(self, node):
        '''对二叉搜索树进行后序遍历，执行方法
        如果节点不为空，则递归左子节点，然后递归右子节点，最后打印自身

        Agre:
            node: 节点
        '''
        if node is not None:
            self._post_order(node.left)
            self._post_order(node.right)
            print('{key: %s, value: %s}' % (node.key, node.value))

    def _remove_post_order(self, node):
        '''使用后序遍历删除树中的所有节点，析构函数的执行方法

        Agre:
            node: 节点
        '''
        if node is not None:
            self._remove_post_order(node.left)
            self._remove_post_order(node.right)
            del node

    def level_order(self):
        '''广度优先遍历
        层序遍历

        引入一个队列，将跟节点入队；
        while循环，判断队列是否为空，如果不为空则循环；
        循环中，将队首的元素拿出并出队，然后将它左右子节点入队，直至最后一层；
        '''
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            print('{key: %s, value: %s}' % (node.key, node.value))
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

    def minimum(self, type="recursion"):
        '''寻找最小值的键值，引用方法

        Agre:
            type: 执行方法
        return:
            None或节点的键值
        '''
        if self.root is None:
            return None
        if type == 'recursion':
            return self._minimum_recursion(self.root)
        else:
            return self._minimum_iteration(self.root)

    def _minimum_recursion(self, node):
        '''寻找最小值的键值，执行方法，递归版
        向左查询，直到某个节点没有左节点，那么此节点即为最小值的节点；

        Agre:
            node: 节点
        return:
            节点的键值
        '''
        if node.left is None:
            return node.key
        return self._minimum_recursion(node.left)

    def _minimum_iteration(self, node):
        '''寻找最小值的键值，执行方法，迭代版
        如果节点的左子节点不为空，则一直循环，直到节点的左子节点为空；

        Agre:
            node: 节点
        return:
            节点的键值
        '''
        while node.left is not None:
            node = node.left
        return node.key

    def maximum(self, type="recursion"):
        '''寻找最大值的键值，引用方法

        Agre:
            type: 执行方法
        return:
            None或节点的键值
        '''
        if self.root is None:
            return None
        if type == "recursion":
            return self._maximum_recursion(self.root)
        else:
            return self._maximum_iteration(self.root)

    def _maximum_recursion(self, node):
        '''寻找最大值的键值，执行方法，递归版
        判断节点的右子节点是否为空，如果是则返回节点的键值；否则递归节点的右子节点；

        Agre:
            node: 节点
        return:
            节点的键值
        '''
        if node.right is None:
            return node.key
        return self._maximum_recursion(node.right)

    def _maximum_iteration(self, node):
        '''寻找最大值的键值，执行方法，迭代版
        如果节点的右子节点不为空，则执行循环，将右子节点替换为当前节点继续进行判断，直到节点的右子节点为空

        Agre:
            node: 节点
        return:
            节点的键值
        '''
        while node.right is not None:
            node = node.right
        return node.key

    def remove_min(self, type="recursion"):
        '''删除掉最小值所在的节点，引用方法

        Agre:
            type: 执行方法
        '''
        if self.root is not None:
            if type == 'recursion':
                self._remove_min_recursion(self.root)
            else:
                self._remove_min_iteration(self.root)

    def _remove_min_recursion(self, node):
        '''删除掉最小值所在的节点，执行方法，递归版
        判断节点的左子节点是否为空，如果为空则获取此节点的右子节点并删除此节点，树的元素个数减一，返回右子节点；
        如果节点不为空，则递归节点的左子节点，并且将结果赋值给节点的左子节点，返回此节点；
        Agre:
            node: 节点
        return:
            node节点
        '''
        if node.left is None:
            right = node.right
            del node
            self.count -= 1
            return right
        node.left = self._remove_min_recursion(node.left)
        return node

    def _remove_min_iteration(self, node):
        '''删除掉最小值所在的节点，执行方法，迭代版
        while循环，判断节点是否为空，为空则跳出循环；
        循环中，判断节点的左子节点的左子节点是否为空，如果是则将节点的左子节点的右子节点移动到节点的左子节点上(删除最小值，将最小值所在的节点的右字节移动)；
        树的节点数减一；

        Agre:
            node: 节点
        '''
        while node is not None:
            if node.left.left is None:
                right = node.left.right
                node.left = right
                self.count -= 1
                break
            node = node.left

    def remove_max(self, type="recursion"):
        '''删除掉最大值所在的节点，引用方法

        Agre:
            type: 执行方法
        '''
        if self.root is not None:
            if type == 'recursion':
                self._remove_max_recursion(self.root)
            else:
                self._remove_max_iteration(self.root)

    def _remove_max_recursion(self, node):
        '''删除掉最大值所在的节点，执行方法，递归版
        原理同删除最小值所在的节点方法

        Agre:
            node: 节点
        return:
            节点
        '''
        if node.right is None:
            left = node.left
            del node
            self.count -= 1
            return left
        node.right = self._remove_max_recursion(node.right)
        return node

    def _remove_max_iteration(self, node):
        '''删除掉最大值所在的节点，执行方法，迭代版
        原理同删除最小值所在的节点方法

        Agre:
            node: 节点
        '''
        while node is not None:
            if node.right.right is None:
                node.right = node.right.left
                self.count -= 1
                break
            node = node.right

    def print_root(self):
        if self.root is not None:
            self._print_root(self.root)

    def _print_root(self, node, level=0):
        if node is not None:
            level += 1
            self._print_root(node.left, level)
            self._print_root(node.right, level)
            print('%s%s---%s' % ('---' * level, node.key, node.value))


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree[28] = 'a'
    tree[16] = 'b'
    tree[30] = 'c'
    tree[13] = 'd'
    tree[22] = 'e'
    tree[29] = 'f'
    tree[42] = 'g'
    tree.remove_max('iteration')
    tree.print_root()
