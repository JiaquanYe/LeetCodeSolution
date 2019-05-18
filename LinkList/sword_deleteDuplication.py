"""
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

def deleteDuplication(pHead):
    if pHead is None or pHead.next is None:
        return pHead

    first = Node(-1)  #empty pHead
    pNode = pHead
    last = first      #before last is undeuplication

    if pNode.data == pNode.next.data:
        value = pNode.data
        while pNode and pNode.next.data == value:
            pNode = pNode.next
        last.next = pNode
    else:
        last = pNode
        pNode = pNode.next

    return first.next 
