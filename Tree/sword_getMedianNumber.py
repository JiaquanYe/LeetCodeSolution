"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
references : https://blog.csdn.net/Strive_0902/article/details/79722579    NO.64
"""

def maxHeapify(tree, i, n):
    """
    以最大堆为例
    tree : 完全二叉树用数组表示
    i : 对结点i进行heapify
    n : len(tree)
    """
    left_child = 2*i+1
    right_child = 2*i+2
    maxIndex = i
    if left_child<n and tree[left_child]>tree[MaxIndex]:
        maxIndex = left_child
    if right_child<n and tree[right_child]>tree[maxIndex]:
        maxIndex = right_child
    if maxIndex != i:
        tree[i], tree[maxIndex] = tree[maxIndex], tree[i]
        maxHeapify(tree, maxIndex, n)

def minHeapify(tree, i, n):
    left_child = 2*i+1
    right_child = 2*i+2
    minIndex = i
    if left_child<n and tree[left_child]<tree[minIndex]:
        minIndex = left_child
    if right_child<n and tree[right_child]<tree[minIndex]:
        minIndex = right_child
    if minIndex != i:
        tree[i], tree[minIndex] = tree[minIndex], tree[i]
        minHeapify(tree, minIndex, n)

def getMedianNumber(left,right,data):
    """
    left is max heap, right is min heap.
    """
    n = len(left) + len(right)
    if n%2 == 0:
        left.append(data)
    else:
        right.append(data)

    maxHeapify(left,0,len(left))
    minHeapify(right,0,len(right))
    if left[0] > right[0]:
        left[0], right[0] = right[0], left[0]
        maxHeapify(left,0,len(left))
        minHeapify(right,0,len(right))

    if len(n+1) % 2 == 0:
        return (left[0]+right[0])/2.0
    else:
        return left[0]
