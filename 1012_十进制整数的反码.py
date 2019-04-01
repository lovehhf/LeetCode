# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
1012. 十进制整数的补码  显示英文描述  
用户通过次数 0
用户尝试次数 0
通过次数 0
提交次数 0
题目难度 Easy
每个非负整数 N 都有其二进制表示。例如， 5 可以被表示为二进制 "101"，11 可以用二进制 "1011" 表示，依此类推。注意，除 N = 0 外，任何二进制表示中都不含前导零。

二进制的补码表示是将每个 1 改为 0 且每个 0 变为 1。例如，二进制数 "101" 的二进制补码为 "010"。

给定十进制数 N，返回其二进制表示的补码所对应的十进制整数。
"""


def bitwiseComplement(N):
    """
    :type N: int
    :rtype: int
    """
    res_bin = bin(N)[2:]
    res_bin = res_bin.replace('1','t')
    res_bin = res_bin.replace('0','1')
    res_bin = res_bin.replace('t','0')
    return int(res_bin,2)

print(bitwiseComplement(7))