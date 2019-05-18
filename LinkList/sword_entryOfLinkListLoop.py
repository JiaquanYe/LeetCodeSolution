"""
一个链表中包含环，请找出该链表的环的入口结点。
"""

class Node():
    def __init__(self,data,next):
        self.data = data
        self.next = next

def entryOfLinkListLoop(pHead):
    fast = pHead
    low = pHead

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    fast == pHead
    while fast:
        fast = fast.next
        slow = slow.next
        if fast == slow:
            return fast
    return None               #Not found loop
