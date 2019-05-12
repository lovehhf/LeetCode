# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。


1. 按照定义，计算x的n次方是将n个x连乘，效率低，会超时。
2. 因为乘法具有结合律，考虑每次将一部分连乘批量计算好，作为最终答案的一部分。
3. 这就可以将n进行二进制拆分，若n的二进制位的第k位是1，则ans可以乘上x^(2^k)。
4. 而计算x^(2^k)，只需每次将自身做平方即可。

参考: https://leetcode.com/problems/powx-n/discuss/19563/Iterative-Log(N)-solution-with-Clear-Explanation
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """

        二进制拆分
        2^15 = 2^8*2^7 =
        1111=1000+111 -> 8=1000=((2*2)**2)**2(三次p=p*p)
        7=111 ->
        :param x:
        :param n:
        :return:
        """
        res = 1
        p = x
        t = abs(n)
        while t:
            print(t,p,res)
            if t & 1:
                res *= p  # p是提前计算好的批量连乘
            p *= p  # 每次更新p，自身平方
            t >>= 1  # 将n进行二进制拆分
        return res if n > 0 else 1 / res

    def myPow2(self, x: float, n: int) -> float:
        """
        正向乘方逼近
        :param x:
        :param n:
        :return:
        """
        res = 1
        p = x
        t = abs(n)
        cur = 1
        while cur <= t:
            if cur * 2 < t:
                p *= p
                cur *= 2
            else:
                t -= cur
                res *= p
                cur = 1
                p = x
        return res if n>0 else 1/res

x = 2
n = 10
s = Solution()
print(pow(x, n))
print(s.myPow(x, n))
