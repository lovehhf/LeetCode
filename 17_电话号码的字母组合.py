# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


def letterCombinations(digits):
    """
    递归
    :param digits:
    :return:
    """
    # print(digits)

    # 创建字母对应的字符列表的字典
    dic = {2: ['a', 'b', 'c'],
           3: ['d', 'e', 'f'],
           4: ['g', 'h', 'i'],
           5: ['j', 'k', 'l'],
           6: ['m', 'n', 'o'],
           7: ['p', 'q', 'r', 's'],
           8: ['t', 'u', 'v'],
           9: ['w', 'x', 'y', 'z'],
           }
    # 存储结果的数组
    ret_str = []

    if len(digits) == 0:
        return []

    # 递归出口，当递归到最后一个数的时候result拿到结果进行for循环遍历
    if len(digits) == 1:
        return dic[int(digits[0])]

    # 递归调用
    result = letterCombinations(digits[1:])

    # print(result)

    # result是一个数组列表，遍历后字符串操作，加入列表
    for r in result:
        for j in dic[int(digits[0])]:
            ret_str.append(j + r)

    return ret_str

def letterCombinations2(digits):
    maps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(maps[digits[0]])

    res = ['']
    for digit in digits: # 234
        new_res = []   # 初始化 new_res
        for ch in maps[digit]:  # abc def ghi
            l = [ele + ch for ele in res]
            # print(l)
            new_res.extend(l)
            print(new_res)
        res = new_res

    return res


print(letterCombinations2('234'))