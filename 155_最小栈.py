# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   # 返回 -3.
minStack.pop()
minStack.top()      # 返回 0.
minStack.getMin()   # 返回 -2.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack != []:
            if self.stack[-1]==self.minstack[-1]:
                self.minstack.pop()
            self.stack.pop()
            
    def top(self):
        """
        :rtype: int
        """
        if self.stack != []:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack != []:
            return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   # 返回 -3.
minStack.pop()
print(minStack.top())      # 返回 0.
print(minStack.getMin())   # 返回 -2.