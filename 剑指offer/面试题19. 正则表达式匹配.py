# -*- coding:utf-8 -*-

"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



f[i][j]: s 前 i 个字符是否能被 p 前 j 个字符匹配

正常转移:
    f[i][j] = f[i - i][j - 1] if s[i] = p[j] || p[j] = .
非正常转移:
    p[j] = *
    1. 使用 0 次*: f[i][j] = f[i][j - 2]
    2. 使用 n 次*: f[i][j] = f[i][j - 1], s[i] = p[j - 1] || p[j - 1] = *
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = " " + s
        p = " " + p
        m, n = len(s), len(p)
        f = [[0] * n for _ in range(m)]
        f[0][0] = 1

        for j in range(2, n):
            if p[j] == "*":
                f[0][j] = f[0][j - 2]


        for i in range(1, m):
            for j in range(1, n):
                if s[i] == p[j] or p[j] == '.':
                    f[i][j] = f[i - 1][j - 1]
                if p[j] == "*":
                    if j >= 2:
                        f[i][j] = f[i][j - 2]
                    if p[j - 1] == s[i] or p[j - 1] == ".":
                        f[i][j] |= f[i - 1][j]

        return f[m - 1][n - 1] == 1


sol = Solution()
s = "mississippi"
p = "mis*is*ip*."
print(sol.isMatch(s, p))
