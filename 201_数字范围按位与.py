# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0
(位运算特性) O(31)O(31)
求出m和n从高位到低位中第一次出现不一样的位置，即可得到答案，答案为该位置之前的二进制的累积和。
解释
因为出现了第一次不一样之后，从m上升到n的过程中，必定会经历xxx100000...和xxx011111...的一次变化，这次变化会将该位之后的所有数字按位和清零。

"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        这个题精髓在于n的二进制位比m二进制最左边的1高时，&的结果必然为0；
        由这个思想启发，二进制最高位相同时，这个1会保存，然后比较右一位，相同也保留... 所以只需要m n 同时右移到相等时 m n的值就是&后能保留的位数，然后左移回来就是最后的值。
        :param m: 
        :param n: 
        :return: 
        """
        a = bin(m)[2:]  # 转换为二进制字符串
        b = bin(n)[2:]
        if len(a) != len(b): return 0  # 字符串长度不相等，答案为0
        i = 0
        length = len(a)
        while i < length and a[i] == b[i]:  # 在m和n二进制长度相等的情况下，计算m和n最高位相等 有多少位
            i += 1
        n >>= (length - i)  # m,n 前i位都相同, n右移length - i位,把i位后面的都变为0,保留最高位相等的二进制数
        n <<= (length - i)  # 再左移length - i位 110100111,110111111 -> 110100000
        return n
    
    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        """
        :param m:
        :param n:
        :return:
        """
        ans = 0
        for i in range(30, -1, -1):
            if (m >> i & 1) ^ (n >> i & 1):
                break
            ans |= (m >> i & 1) << i
        return ans



    def rangeBitwiseAnd3(self, m: int, n: int) -> int:
        """
        爆内存了
        :param m:
        :param n:
        :return:
        """
        from functools import reduce
        return reduce(lambda x, y: x & y, list(range(m, n + 1)))


m, n = 20000, 2147483647
s = Solution()
print(s.rangeBitwiseAnd(m, n))
