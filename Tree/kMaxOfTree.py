"""
二叉搜索树的第k个结点 (index from zero to end)
references : https://blog.csdn.net/Strive_0902/article/details/79722579   62
"""

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def getMidOrderList(root, midOrderList):
    if root.left is not None:
        getMidOrderList(root.left,midOrderList)
    midOrderList.append(root.data)
    if root.right is not None:
        getMidOrderList(root.right,midOrderList)

def kMaxOfTree(root,k):
    midOrderList = []
    getMidOrderList(root, midOrderList)
    if len(midOrderList) < k:
        return None
    return midOrderList[k]

if __name__ == "__main__":
    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7

    kmax = kMaxOfTree(pNode1,3)
