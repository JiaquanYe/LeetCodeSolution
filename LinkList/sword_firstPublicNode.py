"""
输入两个链表，找出它们的第一个公共结点。
"""

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

def firstPublicNode(pHead1, pHead2):
    m = GetListLength(pHead1)
    n = GetListLength(pHead2)
    if m>n:
        pHeadlong = pHead1
        pHeadshort = pHead2
        diff = m-n
    else:
        pHeadlong = pHead2
        pHeadshort = pHead1
        diff = n-m
    for i in range(diff):
        pHeadlong = pHeadlong.next
    while pHeadlong and pHeadshort and pHeadlong.datat != pHeadshort:
        pHeadlong = pHeadlong.next
        pHeadshort = pHeadshort.next

    return pHeadlong  # commom Node



def GetListLength(pHead):
        nLength = 0
        while pHead != None:
            pHead = pHead.next
            nLength += 1
        return nLength
