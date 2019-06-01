"""
包含min函数的栈
"""

class Stack():
    def __init__(self):
        self.stack = []
        self.minStack = []

    def enstack(self,elem):
        self.stack.append(elem)
        if len(self.minStack) is None:
            self.minStack.append(elem)
        elif elem < self.minStack.pop(-1):
            self.minStack.pop(-1)
            self.minStack.append(elem)

    def destack(self):
        
