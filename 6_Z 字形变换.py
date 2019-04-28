# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        思路

        按照与逐行读取 Z 字形图案相同的顺序访问字符串。
        算法

        首先访问 行 0 中的所有字符，接着访问 行 1，然后 行 2，依此类推...

        对于所有整数 kk，

        行 00 中的字符位于索引 k \; (2 \cdot \text{numRows} - 2)k(2⋅numRows−2) 处;
        行 \text{numRows}-1numRows−1 中的字符位于索引 k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1k(2⋅numRows−2)+numRows−1 处;
        内部的 行 ii 中的字符位于索引 k \; (2 \cdot \text{numRows}-2)+ik(2⋅numRows−2)+i 以及 (k+1)(2 \cdot \text{numRows}-2)- i(k+1)(2⋅numRows−2)−i 处;
        :type s: str
        :type numRows: int
        :rtype: str
        """
        m, n = len(s), 2 * numRows - 2
        res = ''
        if (numRows >= m or numRows <= 1):
            return s
        for i in range(numRows):
            for j in range(0, m - i, n):
                res += s[j + i]
                if (i != 0 and i != numRows - 1 and j + n - i < m):
                    res += s[j + n - i]
                j += n
        return res


s = "LEETCODEISHIRING"
numRows = 4
sol = Solution()
print(sol.convert(s, numRows))
