"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

class CQueue():
    def __init__(self,elems = None):
        if not elems:
            self.stack1 = []
        else:
            self.stack1 = elems
        self.stack2 = []

    def enqueue(self, elem):
        self.stack1.append(elem)

    def dequeue(self):
        # stack 1 and stack 2 is empty
        if not self.stack1 and not self.stack2:
            print("This queue is empty")
            return None
        # stack 2 has elem, pop
        if self.stack2:
            return self.stack2.pop(-1)
        # stack 2 has no elem, move stack1 to stack2, pop
        if not self.stack2:
            for s in self.stack1[::-1]:
                self.stack2.append(s)
                self.stack1.pop(-1)
            return self.stack2.pop(-1)

if __name__ == "__main__":
    init_elems = [1,2,3,4,5,6,7]
    cqueue = CQueue(init_elems)
    cqueue.enqueue(9)
    result = cqueue.dequeue()
