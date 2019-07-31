'''
二叉搜索树中更多的查询

指定键值的 ceil 和 floor 查询（错误）
'''


class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.child_node_count = 1


class BinarySearchTreeMore():
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._insert(self.root, key, value)
        self.count += 1

    def _insert(self, node, key, value):
        node.child_node_count += 1
        if node.key >= key:
            if node.left is None:
                node.left = TreeNode(key, value)
            else:
                self._insert(node.left, key, value)
        else:
            if node.right is None:
                node.right = TreeNode(key, value)
            else:
                self._insert(node.right, key, value)

    def __setitem__(self, key, value):
        return self.insert(key, value)

    def print_root(self):
        if self.root is not None:
            self._print_root(self.root)

    def _print_root(self, node, level=0):
        if node is not None:
            level += 1
            self._print_root(node.left, level)
            self._print_root(node.right, level)
            print('%s%s---%s(%s)' % ('---' * level, node.key, node.value, node.child_node_count))

    def ceil_and_floor(self, key):
        if self.root is None:
            return None
        node = self.root
        ceil = None
        floor = None
        while node is not None:
            if ceil is not None and floor is not None:
                return [floor, ceil]
            if node.key == key:
                return [node.key, node.key]
            elif node.key > key:
                ceil = node.key
                node = node.left
            else:
                floor = node.key
                node = node.right


if __name__ == "__main__":
    tree = BinarySearchTreeMore()
    tree[28] = 'a'
    tree[16] = 'b'
    tree[30] = 'c'
    tree[13] = 'd'
    tree[22] = 'e'
    tree[29] = 'f'
    tree[42] = 'g'
    tree[41] = 'h'
    print(tree.ceil_and_floor(33))
    tree.print_root()
