"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
reference : https://blog.csdn.net/Strive_0902/article/details/79722579  NO.39
"""

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right =right

def treeDepth(root):
    if root is None:
        return 0
    return max(treeDepth(root.left), treeDepth(root.right)) + 1

def isAVL(root):
    if root is None:
        return True
    if treeDepth(root.left) - treeDepth(root.right) > 1:
        return False
    return isAVL(root.left) and isAVL(root.right)

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

    isavl = isAVL(pNode1)
