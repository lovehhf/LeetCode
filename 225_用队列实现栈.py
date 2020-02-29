# -*- coding:utf-8 -*-

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


class MyStack:

    def __init__(self):
        """
        队列的弹出队头元素和插入到队尾的时间复杂度均是O(1), 使用一个队列就可以实现栈, 没有必要用2个
        Initialize your data structure here.
        """
        self.queue = deque([])

    def push(self, x: int) -> None:
        """
        直接插入到队尾
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        将队头元素插入到队尾, 循环 n - 1 次, 最后弹出队头元素
        Removes the element on top of the stack and returns that element.
        """
        n = len(self.queue)
        for _ in range(n - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        """
        直接返回队尾元素
        Get the top element.
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.pop())
