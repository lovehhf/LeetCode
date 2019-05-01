# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。

示例:
CAAAAAGGGT
输入: s = "AAAAACCCCC AAAAACCCCCC AAAAAGGGTTT"

输出: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


class Solution:
    def findRepeatedDnaSequences(self, s):
        n = len(s)
        # if n<10:
        #     return []
        d = {}
        tmp = s[:10]
        d[tmp] = 1
        for i in range(n - 10):
            tmp = tmp[1:] + s[10 + i]
            d[tmp] = d.get(tmp, 0) + 1
        # res = []
        # for k, v in d.items():
        #     if v > 1:
        #         res.append(k)
        res = [k for k, v in d.items() if v > 1]
        return res


s = "AAA"
sol = Solution()
print(sol.findRepeatedDnaSequences(s))
