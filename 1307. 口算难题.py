# -*- coding:utf-8 -*-

"""
给你一个方程，左边用 words 表示，右边用 result 表示。

你需要根据以下规则检查方程是否可解：

每个字符都会被解码成一位数字（0 - 9）。
每对不同的字符必须映射到不同的数字。
每个 words[i] 和 result 都会被解码成一个没有前导零的数字。
左侧数字之和（words）等于右侧数字（result）。 
如果方程可解，返回 True，否则返回 False。

 

示例 1：

输入：words = ["SEND","MORE"], result = "MONEY"
输出：true
解释：映射 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
所以 "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
示例 2：

输入：words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
输出：true
解释：映射 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
所以 "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
示例 3：

输入：words = ["THIS","IS","TOO"], result = "FUNNY"
输出：true
示例 4：

输入：words = ["LEET","CODE"], result = "POINT"
输出：false
 

提示：

2 <= words.length <= 5
1 <= words[i].length, results.length <= 7
words[i], result 只含有大写英文字母
表达式中使用的不同字符数最大为 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verbal-arithmetic-puzzle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# from typing import List
#
#
# class Solution:
#     def __init__(self):
#         self.d = 0
#         self.res = 0
#
#     def check(self, words, result, d):
#         l, r = 0, 0
#         for i in words:
#             t = 0
#             for j in i:
#                 t = t * 10 + d[j]
#             l += t
#         for i in result:
#             r = r * 10 + d[i]
#         if (l == r):
#             self.res = 1
#             return True
#         return False
#
#     def dfs(self, words, result, path, idx, n, d):
#         print(d)
#         if idx == n:
#             # print(idx,path, n, d)
#             self.check(words, result, d)
#             return
#         if not self.res:
#             for i in range(10):
#                 if i in d.values():
#                     continue
#                 d[self.s[idx]] = i
#                 self.dfs(words, result, path + [self.s[idx]], idx + 1, n, d)
#
#     def isSolvable(self, words: List[str], result: str) -> bool:
#         self.s = list(set(''.join(words) + result))
#         self.dfs(words, result, [], 0, len(self.s), {})
#         return self.res == 1
#
#
# words = ["SEND", "MORE"]
# result = "MONEY"
#
# s = Solution()
# print(s.isSolvable(words, result))
