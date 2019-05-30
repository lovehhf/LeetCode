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
    def removeInvalidParentheses(self, s):
        """
        优化bfs 	28 ms
        从左往右扫描 确保 count["("]>=count[")"]
        再从右往左扫描 确保 count["("]<=count[")"]
        :param s:
        :return:
        """
        removed = 0
        results = {s}
        count = {"(": 0, ")": 0}
        for i, c in enumerate(s):
            if c == ")" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    new_results |= {result[:j] + result[j + 1:] for j in range(i - removed + 1) if result[j] == ")"}
                results = new_results
                removed += 1
            else:
                if c in count:
                    count[c] += 1
        count = {"(": 0, ")": 0}
        i = len(s)
        ll = len(s) - removed
        for ii in range(ll - 1, -1, -1):
            i -= 1
            c = s[i]
            if c == "(" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    new_results |= {result[:j] + result[j + 1:] for j in range(ii, ll) if result[j] == "("}
                results = new_results
                ll -= 1
            else:
                if c in count:
                    count[c] += 1
        return list(results)

    def removeInvalidParentheses2(self, s):
        """
        普通bfs 928 ms
        :type s: str
        :rtype: List[str]
        """

        def isValid(a):
            count = 0
            for i in a:
                if i == '(':
                    count += 1
                elif i == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if isValid(s):
            return [s]
        queue = {s}
        while queue:
            q = set()
            res = set()
            while queue:
                cur = queue.pop()
                t = {cur[:i] + cur[i + 1:] for i in range(len(cur)) if s[i] == '(' or s[i] == ')'}
                q |= t
                res |= {i for i in t if isValid(i)}
            queue = q
            if res:
                return res
        return [s]


s = 'a)b)c)d)e)f)g)h)i)j)k)l)m)n)o)p)(((((((((((((((((((('
sol = Solution()
print(sol.removeInvalidParentheses(s))
