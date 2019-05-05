# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数。

 
示例 1：

输入：20
输出：1
解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。
示例 2：

输入：100
输出：10
解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。
示例 3：

输入：1000
输出：262

Count res the Number Without Repeated Digit
Then the number with repeated digits = N - res

Similar as
788. Rotated Digits
902. Numbers At Most N Given Digit Set

Explanation:
Transform N + 1 to arrayList
Count the number with digits < n
Count the number with same prefix
For example,
if N = 8765, L = [8,7,6,6],
the number without repeated digit can the the following format:
XXX
XX
X
1XXX ~ 7XXX
80XX ~ 86XX
870X ~ 875X
8760 ~ 8765

Time Complexity:
the number of permutations A(m,n) is O(1)
We count digit by digit, so it's O(logN)



https://leetcode.com/problems/numbers-with-repeated-digits/discuss/256725/JavaPython-Count-the-Number-Without-Repeated-Digit
"""


class Solution:
    def numDupDigitsAtMostN(self, N):
        """

        :param N:
        :return:
        """
        L = list(map(int, str(N + 1)))
        res, n = 0, len(L)

        def A(m, n):
            return 1 if n == 0 else A(m, n - 1) * (m - n + 1)

        for i in range(1, n):
            res += 9 * A(9, i - 1)
        s = set()
        for i, x in enumerate(L):
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += A(9 - i, n - i - 1)
            if x in s:
                break
            s.add(x)
        return N - res

    def numDupDigitsAtMostN2(self, N):
        """
        超时
        :param N:
        :return:
        """
        count = 0

        for i in range(N+1):
            if len(set(str(i)))!=len(str(i)):
                count+=1
        return count

s = Solution()
print(s.numDupDigitsAtMostN(725799))
