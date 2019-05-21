"""
输入一个链表，输出该链表中倒数第k个结点
需要注意：如果输入的链表为空；k大于链表的长度；k为0的情况。
"""

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def countDownKNode(root, k):
    if root is None or k < 1:
        return None

    fast = root
    slow = None
    for i in range(k-1):
        if fast.next:
            fast = fast.next
        else:
            return None       # k < Node number of LinkList
    slow = root
    while slow.next and fast.next:
        slow = slow.next
        fast = fast.next

    return slow

if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(11)
    node3 = Node(13)
    node1.next = node2
    node2.next = node3

    node = countDownKNode(node1,1)
