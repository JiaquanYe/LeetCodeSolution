"""
输入一个链表，从尾到头打印链表每个节点的值。
"""

class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def printLinkList(pHead):
    if pHead is None:
        return None

    #pHead has data
    while pHead:
        print(pHead.data)
        pHead = pHead.next

if __name__ == "__main__":
    node0 = Node(1)
    node1 = Node(2)
    node2 = Node(3)

    node0.next = node1
    node1.next = node2

    printLinkList(node0)
