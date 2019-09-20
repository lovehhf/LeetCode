# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
示例 1：
输入：text = "nlaebolko"
输出：1
示例 2：
输入：text = "loonbalxballpoon"
输出：2
示例 3：

输入：text = "leetcode"
输出：0

提示：

1 <= text.length <= 10^4
text 全部由小写英文字母组成
"""


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balon = [0, 0, 0, 0, 0]
        for i in text:
            if i == 'b':
                balon[0] += 1
            if i == 'a':
                balon[1] += 1
            if i == 'l':
                balon[2] += 1
            if i == 'o':
                balon[3] += 1
            if i == 'n':
                balon[4] += 1
        balon[3] //= 2
        balon[2] //= 2
        return min(balon)
