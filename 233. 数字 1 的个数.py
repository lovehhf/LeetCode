# -*- coding:utf-8 -*-

"""
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        if n <= 0:
            return 0

        # 使用x, y 将数字n分隔为左半部分和右半部分, 如123 分隔成 12 3, 1 23
        x, y = n, 0

        # t存的是y的下一位, 如y是3是t是10, y是23是t是100
        t = 1
        res = 0
        while (x):
            # 预处理该位是1的情况, 如123的1, 此时x=12, y=23, 需要加上百位的24个1, 也就是 y+1
            if (x % 10 == 1):
                res += 1 + y
            # 该位 >1 的情况, 如的2, 10位是2,先加100~123的十位上的1,后面再加的是0~99的十位上的1
            elif (x % 10 > 1):
                res += t

            y = x % 10 * t + y
            x //= 10
            res += x * t
            t *= 10
        return res



s = Solution()
print(s.countDigitOne(123))
