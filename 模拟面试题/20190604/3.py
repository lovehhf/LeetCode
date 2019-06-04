# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]
"""


class Solution(object):
    def check(self, s):
        c = 0
        for i in s:
            if i == '(':
                c += 1
            elif i == ")":
                c -= 1
            if c < 0:
                return False
        return c == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if self.check(s):
            return [s]
        res = set()
        queue = {s}
        while queue:
            q = set()
            while queue:
                cur = queue.pop()
                t = {cur[:i]+cur[i+1:] for i in range(len(cur)) if cur[i]=='(' or cur[i]==')'}
                q|=t
                res |= {i for i in t if self.check(i)}
            if res:
                return res
            queue = q
        return res



s = "()())))()"
sol = Solution()
print(sol.removeInvalidParentheses(s))
