# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

n = 2:
["()()","(())"]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        回溯法
        只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是像方法一那样每次添加。
        我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
        如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。
        :param n:
        :return:
        """
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if left > right:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans

    def generateParenthesis3(self, n):
        """
        闭合数
        :param n:
        :return:
        """
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

    def generateParenthesis2(self, n: int):
        """
        暴力生成
        :param n:
        :return:
        """
        ans = []

        def valid(A):
            bal = 0
            for c in A:
                if c == "(":
                    bal += 1
                else:
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                # 使用递归生成所有序列
                A.append("(")
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        generate([])
        return ans


n = 3
s = Solution()
print(s.generateParenthesis3(n))
