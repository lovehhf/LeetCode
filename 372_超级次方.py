# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1:

输入: a = 2, b = [3]
输出: 8
示例 2:

输入: a = 2, b = [1,0]
输出: 1024

涉及到同余，欧拉定理，欧拉函数，快速幂
 a ^ b % c = (a % c) ^ b % c
           = ((a % c) ^ (b - t) * (a % c) ^ t) % c
           
都不会 直接pow.
"""


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        t = 0
        for i in b:
            t = t * 10 + i
        return pow(a, t, 1337)


a = 2
b = [1, 0, 0]
s = Solution()
print(s.superPow(a, b))
