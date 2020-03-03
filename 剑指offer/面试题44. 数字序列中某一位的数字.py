# -*- coding:utf-8 -*-

"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

示例 1：
输入：n = 3
输出：3

示例 2：
输入：n = 11
输出：0

限制：

0 <= n < 2^31
注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def check(self, n):
        s = "".join([str(x) for x in range(n + 1)])
        return s[n]

    def findNthDigit(self, n: int) -> int:
        """
        找规律:
        1 位数： 0 ~ 9, 10 位
        2 位数: 10 ~ 99, 2 * 90 位
        3 位数: 100 ~ 999, 3 * 900 位
        :param n:
        :return:
        """
        if n < 10:
            return n
        t = 10
        c = 10
        for i in range(2, 10):
            if n < c + 9 * i * t:
                n -= c
                a, b = t + n // i, n % i
                res = str(a)[b]
                return int(res)
            c += i * 9 * t
            t *= 10


s = Solution()
n = 45678
print(s.check(n))
print(s.findNthDigit(n))
