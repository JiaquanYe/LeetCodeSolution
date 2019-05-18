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

def pathSum(root, target, cursum, path, result):
    path.append(root.data)
    cursum += root.data

    isLeaf = root.left==None and root.right==None
    if isLeaf and cursum==target:
        result.append(path[:]) # 这里这一步要千万注意啊，假如是:ret.append(path), 结果是错的。因为Python可变对象都是引用传递啊。
    if root.left:
        pathSum(root.left, target, cursum, path, result)
    if root.right:
        pathSum(root.right, target, cursum, path, result)

    #如果是叶子结点又不满足要求，退回到父结点，删除当前节点
    #如果加入到result，也要pop，回到父节点继续搜索
    path.pop(-1)

def findAllPath(root, target):
    if root is None:
        return []
    cursum = 0
    path = []
    result = []
    pathSum(root, target, cursum, path, result)
    return result

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
    result = findAllPath(pNode1, 22)
