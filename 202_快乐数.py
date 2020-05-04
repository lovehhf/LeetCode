# -*- coding:utf-8 -*-

"""
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1
"""


class SetSolution(object):
    def isHappy(self, n):
        """
        使用集合判重
        :type n: int
        :rtype: bool
        """
        s = set()
        while (not n in s):
            s.add(n)
            m = 0
            while (n):
                t = n % 10
                m += t * t
                n //= 10
            if m == 1:
                return True
            n = m
        return False


s = SetSolution()
print(s.isHappy(2))
