# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""

用户通过次数 404
用户尝试次数 426
通过次数 411
提交次数 516
题目难度 Easy
有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。

如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。

给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。

对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。

 

示例 1：

输入："(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
示例 2：

输入："(()())(())(()(()))"
输出："()()()()(())"
解释：
输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
删除每隔部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
示例 3：

输入："()()"
输出：""
解释：
输入字符串为 "()()"，原语化分解得到 "()" + "()"，
删除每个部分中的最外层括号后得到 "" + "" = ""。
"""


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        res = ''
        for i in S:
            if i == '(':
                if len(stack)>=1:
                    res+=i
                stack.append(i)
            else:
                if len(stack)>1:
                    res += i
                stack.pop()
            # print(stack)
        # print(res)
        return res

    def removeOuterParentheses2(self, S: str) -> str:
        res = ''
        tmp = ''
        cnt = 0
        for c in S:
            tmp += c
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                res += tmp[1:-1]
                tmp = ''
        return res

S = "(()())(())(()(()))"
sol = Solution()
print(sol.removeOuterParentheses(S))