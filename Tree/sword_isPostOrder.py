"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点

references : https://blog.csdn.net/Hqxcsdn/article/details/88395093
             https://blog.csdn.net/Strive_0902/article/details/79722579    NO.24
"""

def isPostOrder(tree):
    if tree is None:
        return False

    index = 0
    root = tree[-1]
    for idx in range(len(tree)-1):
        index = idx
        if tree[index] > root:       #index is right tree begin index
            break

    for i in range(index,len(tree)-1):
        if tree[i] < root:
            return False

    left = True
    if index > 0 :
        left = isPostOrder(tree[:index])

    right = True
    if index < len(tree)-1:
        right = isPostOrder(tree[index:len(tree)-1])

    return left and right

if __name__ == "__main__":
    array = [5, 7, 6, 9, 11, 10, 8]
    array2 = [4, 6, 7, 5]
    array3 = [1, 2, 3, 4, 5]
    print(isPostOrder(array3))
