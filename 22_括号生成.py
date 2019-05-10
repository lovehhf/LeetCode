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
        dfs添加所有有效括号
        剪枝:
        1. 每次可以放置左括号的条件是当前左括号的数目不超过n
        2. 每次可以放置右括号的条件是当前右括号的数目不超过左括号的数目
        :type n: int
        :rtype: List[str]
        """

        def dfs(left, right, n, path, res):
            if left == n and right == n:
                res.append(path)
                return
            if left < n:
                dfs(left + 1, right, n, path + '(', res)
            if right < left:
                dfs(left, right + 1, n, path + ')', res)

        res = []
        dfs(0, 0, n, '', res)
        return res

    def generateParenthesis3(self, n):
        """
        闭合数
        看不懂。
        :param n:
        :return:
        """
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
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
                print(A)
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
print(s.generateParenthesis(n))
