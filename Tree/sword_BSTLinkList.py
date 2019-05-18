"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
比如输入下图中左边的二叉搜索树，则输出转换之后的排序双向链表。
reference : https://www.cnblogs.com/edisonchou/p/4793345.html
            https://blog.csdn.net/jiangjiang_jian/article/details/81637574
"""
"""
!!!
"""
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class solution():
    def __init__(self):
        self.listHead = None
        self.listTail = None

    def convert(self, root):
        if root is None:
            return

        self.convert(root.left)
        if self.listHead is None:
            self.listHead = root
            self.listTail = root
        else:
            self.listHead.right = root
            root.left = self.listTail
            self.listTail = root
        self.convert(root.right)
        return self.listHead
