# -*- coding:utf-8 -*-

"""
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        乘 2 逼近, 一旦超过了重新从 1 开始乘
        :param x:
        :param n:
        :return:
        """
        sign = -1 if n < 0 else 1
        n *= sign

        m = 1
        t = x
        res = 1
        while n > 0:
            if m > n:
                m = 1
                t = x
            res = res * t
            n -= m
            m *= 2
            t = t * t
        return res if sign == 1 else 1 / res


x = 2
n = -10
s = Solution()
print(s.myPow(x, n))
print(x ** n)