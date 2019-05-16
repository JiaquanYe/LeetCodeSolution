"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printTree(root):
    if root is None:
        return []

    result, nodes = [], [root]
    while nodes:
        curlayer = []
        nextlayer = []
        for node in nodes:
            curlayer.append(node.data)
            if node.left:
                nextlayer.append(node.left)
            if node.right:
                nextlayer.append(node.right)
        result.append(curlayer)
        nodes = nextlayer
    return result

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

    result = printTree(pNode1)
