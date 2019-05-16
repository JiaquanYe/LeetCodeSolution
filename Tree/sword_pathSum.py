"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
reference : https://blog.csdn.net/Strive_0902/article/details/79722579  NO.25
            https://blog.csdn.net/u010059070/article/details/75530070
            https://www.cnblogs.com/bitpeng/p/4748148.html
"""

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
