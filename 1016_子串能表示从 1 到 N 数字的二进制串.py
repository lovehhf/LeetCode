# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
1023. 子串能表示从 1 到 N 数字的二进制串  显示英文描述  
用户通过次数 104
用户尝试次数 118
通过次数 105
提交次数 189
题目难度 Medium
给定一个二进制字符串 S（一个仅由若干 '0' 和 '1' 构成的字符串）和一个正整数 N，如果对于从 1 到 N 的每个整数 X，其二进制表示都是 S 的子串，就返回 true，否则返回 false。

示例 1：

输入：S = "0110", N = 3
输出：true
示例 2：

输入：S = "0110", N = 4
输出：false
"""


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N,0,-1):
            bin_n = bin(i)[2:]
            if bin_n not in S:
                return False
        return True

S = '110101011011000011011111000000'
N = 15
s =Solution()
print(s.queryString(S,N))