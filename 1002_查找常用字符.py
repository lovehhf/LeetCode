# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]

示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]
"""


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        def fun(x,y):
            res = []
            d = {}
            for i in x:
                d[i] = d.get(i,0)+1
            for i in y:
                if d.get(i, 0) > 0:
                    d[i] -= 1
                    res.append(i)
            return res

        from functools import reduce
        return list(reduce(fun,A))



A = ["cool","lock","cook"]
s = Solution()
print(s.commonChars(A))