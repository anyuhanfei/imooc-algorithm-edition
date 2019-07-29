import random


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
        '''对二叉搜索树进行前序遍历（深度优先遍历）'''
        self._pre_order(self.root)

    def _pre_order(self, node):
        if node is not None:
            print(node.value)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def in_order(self):
        '''对二叉搜索树进行中序遍历'''
        self._in_order(self.root)

    def _in_order(self, node):
        if node is not None:
            self._in_order(node.left)
            print(node.value)
            self._in_order(node.right)

    def post_order(self):
        '''对二叉搜索树进行后序遍历'''
        self._post_order(self.root)

    def _post_order(self, node):
        if node is not None:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.value)

    def level_order(self):
        '''层序遍历（广度优先遍历）
        引入一个队列，将跟节点入队；
        while循环，判断队列是否为空，如果不为空则循环；
        循环中，将队首的元素拿出并出队，然后将它左右子节点入队，直至最后一层；
        '''

    def minimum(self):
        '''寻找最小值的键值
        向左查询，直到某个节点没有左节点
        可递归，可迭代
        maximum类似
        '''

    def remove_min(self):
        '''删除掉最小值所在的节点
        递归节点，判断左子节点是否存在，如果存在，则继续递归左子节点，并且，将递归结果赋值给节点的左子节点；
        如果左子节点不存在，则说明此节点即为最小节点，那么将右子节点取出，并删除掉左子节点，返回右子节点。
        递归的返回值会赋值到上一层的左子节点上，这样就实现了删除的节点的子节点移动到删除的节点的父节点上。
        删除最小值同理，查右子节点，删除右子节点，返回左子节点，赋值给父节点的右子节点。
        记得count--；
        递归迭代均可
        '''

    def print_root(self, node='root'):
        if node == 'root':
            node = self.root
        if node is not None:
            print('%s: %s' % (node.key, node.value))
            self.print_root(node.left)
            self.print_root(node.right)


if __name__ == "__main__":
    b = BinarySearchTree()
    for i in range(0, 10):
        value = random.randint(100, 1000)
        b[i] = value
    b.print_root()
    print(b[7])


# 用后序遍历析构类
