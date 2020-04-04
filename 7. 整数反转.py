# -*- coding:utf-8 -*-

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

链接：https://leetcode-cn.com/problems/reverse-integer
"""


class Solution:
    def reverse(self, x: int) -> int:
        """

        :param x:
        :return:
        """
        INT_MAX, INT_MIN = 2147483647, -2147483648
        res = 0

        if x == INT_MIN:
            return 0

        sign = -1 if x < 0 else 1
        x = abs(x)
        while(x):
            t = x % 10

            # 提前判断溢出，溢出就返回 0
            if res > INT_MAX // 10:
                return 0

            res = res * 10 + t
            x //= 10

        return sign * res

s = Solution()
print(s.reverse(2147483647))
