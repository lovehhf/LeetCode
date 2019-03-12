# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
"""


def convertToTitle(n):
    key_list = [x for x in range(1, 27)]
    value_list = [chr(ord('A') + x) for x in range(0, 26)]
    dic = dict(zip(key_list,value_list)) # 键值对字典
    ans = []
    a = n//26
    ans.append(a)
    # 辗转相除
    while  a!=0:
        a = a//26
        ans.append(a)

    print(ans)


if __name__ == '__main__':
    print(convertToTitle(888))