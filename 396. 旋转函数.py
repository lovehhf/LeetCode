# -*- coding:utf-8 -*-

"""
给定一个长度为 n 的整数数组 A 。
假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。
计算F(0), F(1), ..., F(n-1)中的最大值。

注意:
可以认为 n 的值小于 105。

示例:
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。

链接：https://leetcode-cn.com/problems/rotate-function

错位相减, 每次迭代除了最后一项变大了，其他项都减少了1

（1）F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-2) * Bk[n-2] + (n-1) * Bk[n-1]
（2）F(k+1) = 0 * Bk[n-1] + 1 * Bk[0] + 2 * Bk[2] + ... + (n-1) * Bk[n-2]
（2）-（1）得：F(k+1) - F(k) = (Bk[0] + Bk[1] + ... + Bk[n-2]) - (n-1)*Bk[n-1]
可得：F(k+1) - F(k) = (Bk[0] + Bk[1] + ... + Bk[n-2] + Bk[n-1]) - n*Bk[n-1]
有：F(k+1) = F(k) + S - n * Bk[n-1]
"""

from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        s = sum(A)
        ss = 0

        for i in range(n):
            ss += i * A[i]

        res = ss
        for i in range(n - 1):
            ss = ss + s - A[n - 1 - i] * n
            res = max(res, ss)

        return res


s = Solution()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(s.maxRotateFunction(A))
