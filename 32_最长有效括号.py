# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        动态规划四步走
        1.确认原问题与子问题: 原问题为求s中最长有效括号，子问题可拆解为前i个中最长有效括号。
        2.确认状态: 本题的动态规划状态单一，第i个状态即为前i个字符串中最长括号数。
        3.确认边界状态的值: dp[1]=0，从1开始
        4.确定状态转移方程: 对于(())适用dp[i] = dp[i - 1] + 2; 对于()()适用 dp[i] += dp[i - dp[i]];
        两者结合一起判断，防止()()(())这种情况
        :type s: str
        :rtype: int
        """
        s = s.lstrip(')').rstrip('(')
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(n):
            if s[i] == ')':
                # i - dp[i - 1] - 1 )对应的括号左边的索引,=='('说明有效 否则前面的字符加上)就无效了,后面需要重新计数
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                if i - dp[i] >= 0 and dp[i - dp[i]] > 0:
                    dp[i] += dp[i - dp[i]]
            res = max(dp[i], res)
        print(dp)
        return res


s = "()((()))()((())))((())))))()("
sol = Solution()
print(sol.longestValidParentheses(s))
