#coding=utf-8
# video: https://www.bilibili.com/video/av33869443/?p=1
# blog:  https://www.cnblogs.com/kumata/p/9170519.html
class Node():
    def __init__(self, elem=None, lchild=None, rchild=None):
        self.data = elem
        self.lchild = lchild
        self.rchild = rchild

class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root

    def getMin(self, BST):
        if BST is None:
            return None
        while(BST.lchild):
            BST = BST.lchild
        return BST

    def getMax(self, BST):
        if BST is None:
            return None
        while(BST.rchild):
            BST = BST.rchild
        return BST


    def searchRecursion(self, BST, key):
        """
        key : the search elems, find key in BST
        """
        if BST is None:
            return None
        if key < BST.data:
            return self.searchRecursion(BST.lchild, key)
        elif key > BST.data:
            return self.searchRecursion(BST.rchild, key)
        else:
            return BST.data

    def searchIteration(self, BST, key):
        """
        key : the search elems, find key in BST
        """
        while(BST):
            if key < BST.data:
                BST = BST.lchild
            elif key > BST.data:
                BST = BST.rchild
            else:
                return BST.data
        return None  # No key in tree

    def insert(self, BST, elem):
        """
        elem : the insert number
        """
        if BST is None:
            return Node(elem)
        if elem < BST.data:
            BST.lchild = self.insert(BST.lchild, elem)
        elif elem > BST.data:
            BST.rchild = self.insert(BST.rchild, elem)
        else: # elem has in tree, pass
            pass
        return BST

    def remove(self, BST, elem):
        """
        elem : the remove number

        1. remove number has no child
        2. remove number has one child
        3. remove number has two children ***
        """
        if BST is None:  #empty tree
            return None
        if elem < BST.data:         #elem is smaller than root
            BST.lchild = self.remove(BST.lchild, elem)
        elif elem > BST.data:       #elem is bigger than root
            BST.rchild = self.remove(BST.rchild, elem)
        else:                       # this is the node to remove
            if BST.lchild and BST.rchild:  # remove node has two children
                TMP = self.getMin(BST.rchild)   # get max of lchild or min of rchild
                BST.data = TMP.data             # copy the data of replace Node ( max of lchild or min of rchild)
                BST.rchild = self.remove(BST.rchild, TMP.data) # convert the two children problem to one child problem
            else:                   # remove node has only one child
                if not BST.lchild :        # right child or no child
                    BST = BST.rchild
                elif not BST.rchild :      # left child or no child
                    BST = BST.lchild
        return BST

    def display(self, root):
        """
        利用队列实现层次遍历print (wrong.)
        """
        if root == None:
            return None
        myQueue = []
        myQueue.append(root)
        while(myQueue):
            tmp = myQueue.pop(0)
            print(tmp.data)
            if tmp.lchild is not None:
                myQueue.append(tmp.lchild)
            if tmp.rchild is not None:
                myQueue.append(tmp.rchild)

if __name__ == "__main__":
    root = Node(7)
    bst = BinarySearchTree(root)
    bst.insert(bst.root, 9)
    bst.insert(bst.root, 3)
    bst.insert(bst.root, 4)
    bst.insert(bst.root, 6)
    bst.insert(bst.root, 1)
    bst.insert(bst.root, 8)
    bst.display(bst.root)
    bst.remove(bst.root,9)
    bst.remove(bst.root,9)
    print("after remove")
    bst.display(bst.root)
