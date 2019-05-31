# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = [1]
        idx = [0, 0, 0]
        for i in range(n - 1):
            next_ugly = min(uglys[idx[0]] * 2, uglys[idx[1]] * 3, uglys[idx[2]] * 5)
            uglys.append(next_ugly)
            if next_ugly == uglys[idx[0]] * 2:
                idx[0] += 1
            if next_ugly == uglys[idx[1]] * 3:
                idx[1] += 1
            if next_ugly == uglys[idx[2]] * 5:
                idx[2] += 1
        return uglys[-1]

n = 10
s = Solution()
print(s.nthUglyNumber(n))
