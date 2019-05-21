"""
反转链表
输入一个链表，反转链表后，输出链表的所有元素
"""

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

def reverseLinkListRecursion(pHead):
    if pHead is None or pHead.next is None:
        return pHead
    newHeader = reverseLinkListRecursion(pHead.next)
    pHead.next.next = pHead
    pHead.next = None
    return newHeader

def reverseLinkList(pHead):
    if pHead is None:
        return None
    prev = None
    cur = pHead
    nex = cur.next
    while cur.next:
        cur.next = prev
        nex.next = cur
        prev = cur
        cur = nex
        nex = cur.next
