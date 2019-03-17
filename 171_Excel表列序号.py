# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:

输入: "A"
输出: 1
"""


def titleToNumber(s):
    if not s:
        return 0
    n = len(s)
    key_list = [chr(ord('A') + x) for x in range(26)]
    val_list = list(range(1, 27))
    dic = dict(zip(key_list, val_list))
    res = 0
    for i in range(n):
        res += dic[s[n - 1 - i]] * 26 ** i
    return res

def titleToNumber2(s):
    """
    :type s: str
    :rtype: int
    思路：遍历s的每一位，利用ACSII码去求该位的数值，注意是26进制，
    每一位数值加一起即可。
    """
    n = len(s)
    sum = 0
    for i in range(n):
        sum += (ord(s[i]) - ord('A') + 1) * pow(26, n - i - 1)

    return sum

print(titleToNumber('ABC'))