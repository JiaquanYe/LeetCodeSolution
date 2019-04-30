#coding=utf-8
"""

其实我们在学习图论或者图相关的算法的时候会遇到两个基本的算法，
深度优先遍历和广度优先遍历，在树中，前序遍历类似于深度优先遍历，
后序遍历类似于广度优先遍历，而一般通常使用栈来实现深度，队列实现广度。
我们可以使用递归或者非递归的方法实现。
将使用Python实现树的构造和几种遍历算法
树的构造
递归实现先序遍历、中序遍历、后序遍历
非递归实现先序遍历，中序遍历，后序遍历
队列实现层次遍历

"""
class Node(object):
    """节点类"""
    def __init__(self, element=-1, lchild=None, rchild=None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self,element):
        node = Node(element)
        # 如果树是空的，则对根节点赋值，赋值之后树一直不为空
        if self.root.element == -1:
            self.root = node
            self.myQueue.append(self.root)
        #此节点的子树没有齐，在此节点上插入左右子节点
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            elif treeNode.rchild == None:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。(该结点已满不能再插入)

    def preorder_recursive(self, root):
         """利用递归的先序遍历 根左右"""
         print(root.element)
         if root.lchild is not None:  #不是叶结点才递归
             self.preorder_recursive(root.lchild)
         if root.rchild is not None:  #不是叶结点才递归
             self.preorder_recursive(root.rchild)

    def midorder_recursive(self, root):
        """利用递归的中序遍历 左根右"""
        if root.lchild is not None:
            self.midorder_recursive(root.lchild)
        print(root.element)
        if root.rchild is not None:
            self.midorder_recursive(root.rchild)

    def laterorder_recursive(self, root):
        """利用递归的后序遍历 左右根"""
        if root.lchild is not None:
            self.laterorder_recursive(root.lchild)
        if root.rchild is not None:
            self.laterorder_recursive(root.rchild)
        print(root.element)

    """!!!"""
    def preorder_stack(self, root):
        """ 利用堆栈实现先序遍历 """
        if root == None:
            return -1
        myStack = []
        node = root
        while node or myStack:
            while node:
                print(node.element)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            node = node.rchild

    def midorder_stack(self, root):
        """ 利用堆栈实现中序遍历 """
        if root == None:
            return -1
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            print (node.element)
            node = node.rchild

    def laterorder_stack(self, root):
        """
        利用两个栈实现后序遍历 左右根
        """
        if root == None:
            return -1

        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            node = myStack1.pop() # 弹出顺序是根右左
            if node.lchild:
                myStack1.append(node.lchild) #加入顺序是左右，弹出顺序就是右左
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node) # 与Stack1弹出顺序一致

        while myStack2:
            print (myStack2.pop().element)

    def level_queue(self, root):
        """
        利用队列实现层次遍历
        """
        if root == None:
            return -1
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            # 先进先出，pop第一个元素，pop默认是弹出最后一个元素
            node = myQueue.pop(0)
            print(node.element)
            if node.lchild:
                myQueue.append(node.lchild)
            if node.rchild:
                myQueue.append(node.rchild)

    def maxDepth(self, root):
        """利用递归实现二叉树的最大深度"""
        if root == None:
            return 0
        else:
            l = 1 + self.maxDepth(root.lchild)
            r = 1 + self.maxDepth(root.rchild)
            return max(l,r)







if __name__ == '__main__':
    elems = range(10)
    tree = Tree()
    for elem in elems:
        tree.add(elem)

    print("队列实现层次遍历:")
    tree.level_queue(tree.root)

    print("\n\n利用堆栈实现先序遍历:")
    tree.preorder_stack(tree.root)

    print("\n\n利用堆栈实现中序遍历:")
    tree.midorder_stack(tree.root)

    print("\n\n利用堆栈实现后序遍历:")
    tree.laterorder_stack(tree.root)

    print("\n\n利用递归的先序遍历:")
    tree.preorder_recursive(tree.root)

    print("\n\n利用递归的中序遍历:")
    tree.midorder_recursive(tree.root)

    print("\n\n利用递归的后序遍历:")
    tree.laterorder_recursive(tree.root)

    print("\n\n利用递归实现二叉树的最大深度:")
    maxdepth = tree.maxDepth(tree.root)
    print(maxdepth)
