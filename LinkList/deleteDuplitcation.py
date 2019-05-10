"""
删除链表中重复的节点
在一个排序，如何删除重复的节点？
例如：1 -> 2 -> 3 -> 3 -> 4
删除后是 1 -> 2 -> 4

solution :
采用三个指针来进行遍历，同时删除重复的节点，因为是有序的链表，我们就可以确定，重复的元素肯定是在一块链接;
如果cur与next的值相同，则next继续走，知道走到与cur不相同时，执行删除操作
"""

class Node():
    def __init__(self, elem, next=None):
        self.data = elem
        self.next = next

def getNewpHead(list):
    if list:
        node = Node(list.pop(0))
        node.next = getNewpHead(list)
        return node

def deleteDuplication(pHead):   #***
    if pHead is None or pHead.next is None:
        return pHead
    first = Node(-1)
    first.next = pHead
    last = first

    while pHead and pHead.next:
        if pHead.data == pHead.next.data:              # 如果相等说明有相同的节点
            value = pHead.data
            while pHead and value == pHead.data:       # 处理有重复的情况
                pHead = pHead.next
            last.next = pHead                          # 删除动作
        else:                                          # 如果相等说明没有相同的节点
            last = pHead
            pHead = pHead.next

    return first.next

if __name__ == "__main__":
    list = [2,2,3,4,4]
    pHead = getNewpHead(list)
    new_pHead = deleteDuplication(pHead)
    while new_pHead:
        print(new_pHead.data, end=" ")
        new_pHead = new_pHead.next
