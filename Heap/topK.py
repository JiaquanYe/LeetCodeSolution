def minHeapify(topk, i, n):
    lchild = 2*i+1
    rchild = 2*i+2
    minIndex = i
    if (lchild < n and topk[minIndex]>topk[lchild]):
        minIndex = lchild
    if (rchild < n and topk[minIndex]>topk[rchild]):
        minIndex = rchild
    if (minIndex != i):
        topk[minIndex], topk[i] = topk[i], topk[minIndex]
        minHeapify(topk, minIndex, n)

def minHeapTopK(array, k):
    if len(array) <= k:
        topk = array
        return topk
    else:
        topk = array[:k]
        minHeapify(topk, 0, k)
        for idx in range(k, len(array)):
            if array[idx] > topk[0]:
                topk[0] = array[idx]
                minHeapify(topk, 0, k)
        return topk

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9,10]
    topk = minHeapTopK(array,5)
