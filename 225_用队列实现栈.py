# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""

from collections import deque


class MyStack(object):

    def __init__(self):
        """
        self.queue1:存放队列元素
        self.queue2:pop时用于暂时存放队列的前n-1个元素
        self.n:队列长度
        Initialize your data structure here.
        """
        self.queue1 = deque([])
        self.queue2 = deque([])

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        将队列1的元素除了最后一个以外都倒到队列2里面去
        遍历记录队列1最后的元素
        再将队列2的元素倒回队列1
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        top_element = self.queue1.popleft()
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        return top_element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue1[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.pop())
