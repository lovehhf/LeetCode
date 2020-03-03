# -*- coding:utf-8 -*-

"""
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:

输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

动态规划 + 排列组合

状态转移方程: f[i] = f[i - 1] + [10^(i - 1), 10^i)中的各位数字都不同的数字数量

排列组合如何求 [10^(i - 1), 10^i) 中的数量:
9, i = 1
9*9*8*7...(11-i), i >= 2


class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;

        int res = 10;
        int t = 9;
        n = n > 10 ? 10 : n;
        for(int i = 2; i <= n; i ++) {
            t *= 11 - i;
            res += t;
        }

        return res;
    }
};
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n > 10:
            n = 10

        t = 9
        res = 0
        for i in range(2, n + 1):
            t *= (11 - i)
            res += t

        return res
