"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
references : https://blog.csdn.net/Strive_0902/article/details/79722579    No.61
"""

class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def zigzagPrint(root):
    if root is None:
        return []

    result, nodes = [], [root]
    right = True       #下一层是否从右向左,是的话先进左孩子，再进右孩子，最后反转输出（相当于一个栈）
    while nodes:
        curlayer = []
        nextlayer = []
        if right:      #下一层是否从右向左
            for node in nodes:
                curlayer.append(node.data)
                if node.left:
                    nextlayer.append(node.left)
                if node.right:
                    nextlayer.append(node.right)
        else:
            for node in nodes:
                curlayer.append(node.data)
                if node.right:
                    nextlayer.append(node.right)
                if node.left:
                    nextlayer.append(node.left)

        right = not right   #下一层相反
        result.append(curlayer)
        nextlayer.reverse()
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

    result = zigzagPrint(pNode1)
