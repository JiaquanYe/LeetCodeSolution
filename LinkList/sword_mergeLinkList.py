"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def mergeLinkList(pHead1, pHead2):
    if pHead1 is None and pHead2:
        return pHead2
    if pHead2 is None and pHead1:
        return pHead1
    if pHead1 is None and pHead2 is None:
        return None

    if pHead1.data < pHead2.data:
        pMergeHead = pHead1
        pMergeHead.next = mergeLinkList(pHead1.next, pHead2)
    else #pHead1.data == pHead2.data or pHead1.data > pHead2.data
        pMergeHead = pHead2
        pHead2.next = mergeLinkList(pHead2.next, pHead1)

    return pMergeHead
