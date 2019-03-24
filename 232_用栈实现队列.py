# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
使用栈实现队列的下列操作:
push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue()

queue.push(1)
queue.push(2)  
queue.peek()  # 返回 1
queue.pop()   # 返回 1
queue.empty() # 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        栈:先进后出
        进:append()
        出:pop()
        """
        self.push_stack = []  # 栈1
        self.pop_stack = []   # 栈2

    def push(self, x):
        """
        如果栈2不为空,需要先将栈2的元素倒入栈1再执行push操作
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # if self.pop_stack:
        while self.pop_stack:
            self.push_stack.append(self.pop_stack.pop())
        self.push_stack.append(x)

    def pop(self):
        """
        如果栈1不为空，需要先将栈1的元素倒入栈2再pop
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.push_stack:
            return self.pop_stack[-1]
        if not self.pop_stack:
            return self.push_stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.push_stack and not self.pop_stack

# Your MyQueue object will be instantiated and called as such:
queue = MyQueue()
queue.push(1)
queue.push(2)  
param_1 = queue.peek()  # 返回 1
param_2 = queue.pop()   # 返回 1
param_3 = queue.empty() # 返回 false

print(param_1)
print(param_2)
print(param_3)