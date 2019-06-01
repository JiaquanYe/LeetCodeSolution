"""
包含min函数的栈

所以接下来我们用一个辅助栈来实现最小值的更新工作。

这个辅助栈工作原理：

入栈时，1）当数据栈为空时，进入栈的元素同时也进入辅助栈；
      2）当它不为空时，就把该入栈元素与辅助栈的栈顶元素进行比较，若入栈元素小，则该元素同时也进入辅助栈；若不是，则对辅助栈不进行操作

出栈时，1）当时辅助栈的栈顶元素等于处理数据的数据栈栈顶元素时，不经数据栈要弹出元素，辅助栈也要弹出栈顶元素，
       2)当不等时，只对数据栈进行出栈操作。

这样我们思路就很明确了：min函数只需返回辅助栈的栈顶源。
"""

class Stack():
    def __init__(self):
        self.stack = []
        self.minStack = []

    def enstack(self,elem):
        if len(self.stack)==0 and len(self.minStack)==0:
            self.stack.append(elem)
            self.minStack.append(elem)
        #就把该入栈元素与辅助栈的栈顶元素进行比较，若入栈元素小，则该元素同时也进入辅助栈；
        elif len(self.stack):
            if elem < self.minStack[-1]:
                self.stack.append(elem)
                self.minStack.append(elem)
            else:
                self.stack.append(elem)

    def destack(self):
        top = self.stack.pop(-1)
        if top == self.minStack[-1]:
            self.minStack.pop(-1)

    def getStackMin(self):
        return self.minStack[-1]
