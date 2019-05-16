"""
题目描述：
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
references : https://blog.csdn.net/u010636181/article/details/78261445
"""

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def hasSubTree(rootA, rootB):
    #判断A当前节点开始，B是否为子结构，如果不是看下A的左子树节点，如果也不是再看下A的右子树。
    if not rootA or not rootB:
        return False
    return isSubTree(rootA, rootB) or isSubTree(rootA.left, rootB) or isSubTree(rootA.right, rootB)


def isSubTree(A,B):
    if not B:          #判断B是否匹配完了，如果匹配完了说明为子结构
        return True
    elif not A or A.data != B.data:   #如果A匹配完了，或者A的值和B和值不等，直接返回False
        return False
    else:              #如果当前点相同，那同时看一下左子树和右子树的情况。
        return isSubTree(A.left, B.left) and isSubTree(A.right, B.right)


if __name__ == "__main__":
