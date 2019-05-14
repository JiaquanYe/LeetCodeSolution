"""
问题描述：判断二叉树是否为对称的二叉树，如果一棵二叉树和其镜像二叉树一样，那么它就是对称的

references : symmetrical Tree: https://blog.csdn.net/ustcer_93lk/article/details/80373736
             mirror Tree: https://blog.csdn.net/ustcer_93lk/article/details/80373690
"""

class TreeNode():
    def __init__(self, data=-1, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isSymmetrical(treeRoot1, treeRoot2):
    if treeRoot1.data == -1 and treeRoot2.data == -1:   #两个都是空，一样
        return True
    elif treeRoot1.data == -1 or treeRoot2.data == -1 : #一个都是空，一样
        return False
    elif treeRoot1.data != treeRoot2.data:              #根节点不一样
        return False
    else:
        return isSymmetrical(treeRoot1.left,treeRoot2.right) and isSymmetrical(treeRoot1.right, treeRoot2.left)
