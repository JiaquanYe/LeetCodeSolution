"""
给定一棵二叉查找树，以及某个结点的值。查找该结点的下一个结点。如果该结点是最大的，则返回 null
对于二叉查找树而言，它是中序遍历有序的。某结点的下一个结点 就是：中序遍历输出的下一个结点。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
references : https://blog.csdn.net/hewenjing8168/article/details/79762099
"""
class TreeNode():
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


def NextTreeNode(node):
    cur = TreeNode(-1)   #new a TreeNode

    #如果该节点有右孩子，右孩子的最左边的叶子节点就是下一个结点
    if (node.right is not None):
        cur = node.right
        while (cur.left):
            cur = cur.left
        return cur
    #node节点没有右孩子时，node节点是其父结点的左孩子,父结点就是下一个结点
    elif (node.parent is not None):
        if (node == node.parent.left):
            return node.parent
    #node 节点没有右孩子时，node节点是其父结点的右孩子,向上找父节点，直到父节点是父节点的父节点的左孩子
    pcur = node.parent
    while(pcur):
        if (pcur.parent.left == pcur):
            return pcur
        pcur = pcur.parent

    return None


if __name__ == "__main__":
