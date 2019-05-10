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

0   6    12
1  57  1113
2 4 810  14
3   9    15

PAYPALISHIRING

P A H N
APLSIIG
Y I R

找规律: 
第一行和最后一行: 首项0和(n-1公差为2(n-1)的等差数列
2~n-1行 2个公差为2(n-1)的等差数列,首项分别为i,2(n-1)-i
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :param s:
        :param numRows:
        :return:
        """
        n = len(s)
        if numRows >= n or numRows < 1:
            return s
        m = 2 * numRows - 2
        res = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < n:
                    res += s[j]
                    j += m
            else:
                j = i
                k = 2 * numRows - 2 - i
                while j < n or k < n:
                    if j < n:
                        res += s[j]
                    if k < n:
                        res += s[k]
                    j += m
                    k += m
        return res

    # def convert(self, s, numRows):
    #     """
    #
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """
    #     m, n = len(s), 2 * numRows - 2
    #     res = ''
    #     if (numRows >= m or numRows <= 1):
    #         return s
    #     for i in range(numRows):
    #         for j in range(0, m - i, n):
    #             res += s[j + i]
    #             if (i != 0 and i != numRows - 1 and j + n - i < m):
    #                 res += s[j + n - i]
    #             j += n
    #     return res


s = "A"
numRows = 1
sol = Solution()
print(sol.convert(s, numRows))
