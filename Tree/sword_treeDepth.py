"""
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
reference : https://blog.csdn.net/Strive_0902/article/details/79722579   NO.39
"""

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def treeDepth(root):
    if root is None:
        return 0
    return max(treeDepth(root.left), treeDepth(root.right)) + 1


if __name__ == "__main__":
    pNode1 = TreeNode(10)
    pNode2 = TreeNode(5)
    pNode3 = TreeNode(12)
    pNode4 = TreeNode(4)
    pNode5 = TreeNode(7)


    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5

    depth = treeDepth(pNode1)
