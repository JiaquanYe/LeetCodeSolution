#coding=utf-8

def swap(tree, i, j):
    tmp = tree[i]
    tree[i] = tree[j]
    tree[j] = tmp

def heapify(tree, i, n):
    """
    以最大堆为例
    tree : 完全二叉树用数组表示
    i : 对结点i进行heapify
    n : len(tree)
    """
    left = 2*i+1
    right = 2*i+2
    maxIndex = i
    if (left<n and tree[left]>tree[maxIndex]): # n = (0, len(n)-1)
        maxIndex = left
    if (right<n and tree[right]>tree[maxIndex]):
        maxIndex = right
    if (maxIndex != i):
        tree[maxIndex], tree[i] = tree[i], tree[maxIndex]
        #swap(tree, i, maxIndex)
        heapify(tree, maxIndex, n)

def buildHeap(tree):
    """
    建堆从第一个非叶子结点开始（即倒数第二层最左）,
    每个数据从上往下做一次heapify
    """
    for idx in range(0, len(tree)//2)[::-1]: # 0 ~ len(tree)//2 -1
        heapify(tree, idx, len(tree))


def heapSort(tree):
    """
    以最大堆为例
    1.先建堆
    2.再排序操作
    """
    buildHeap(tree)
    n = len(tree)
    for idx in range(0,n)[::-1]:
        tree[0], tree[idx] = tree[idx], tree[0]
        heapify(tree, 0, idx)


if __name__ == "__main__":
    tree = [1,5,8,2,6,9,7]
    buildHeap(tree)
    heapSort(tree)
    print(tree)
