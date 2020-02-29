# -*- coding:utf-8 -*-

"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


贪心,
全部凑成 3, 余 1 的情况最后一个 3 和 1 凑成 4

1 2 3 可以合成任意数字

4 = 1 + 3 > 1 * 3 -> 4 不拆
4 = 2 + 2 = 2 * 2
5 = 2 + 3 < 2 * 3 -> 5 拆成 2 和 3
6 = 3 + 3 < 3 * 3 -> 6 拆成 3 和 3
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        a, b = n // 3, n % 3
        res = 3 ** a
        if b == 1:
            res = res // 3 * 4
        if b == 2:
            res *= 2
        return res



s = Solution()
print(s.cuttingRope(50))
