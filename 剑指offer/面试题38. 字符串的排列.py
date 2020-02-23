# -*- coding:utf-8 -*-

"""
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

限制：
1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:   # 去重
                continue
            self.dfs(s[:i] + s[i + 1:], path + s[i], res)

    def permutation(self, s: str) -> List[str]:
        s = sorted(s)
        res = []
        self.dfs(s, "", res)
        return res
