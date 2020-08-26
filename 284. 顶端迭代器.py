# -*- coding:utf-8 -*-

"""
给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。设计并实现一个支持 peek() 操作的顶端迭代器
-- 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。

示例:
假设迭代器被初始化为列表 [1,2,3]。

调用 next() 返回 1，得到列表中的第一个元素。
现在调用 peek() 返回 2，下一个元素。在此之后调用 next() 仍然返回 2。
最后一次调用 next() 返回 3，末尾元素。在此之后调用 hasNext() 应该返回 false。
进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？

链接：https://leetcode-cn.com/problems/peeking-iterator

变量保存顶端的元素
"""


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.num = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.num:
            self.num = self.iterator.next()
        return self.num

    def next(self):
        """
        :rtype: int
        """
        if self.num:
            tmp = self.num
            self.num = None
            return tmp
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.num != None or self.iterator.hasNext()
