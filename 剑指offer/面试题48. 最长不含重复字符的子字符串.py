# -*- coding:utf-8 -*-

"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

提示：
s.length <= 40000
注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

哈希表 + 双指针 实现 滑动窗口
1. 左指针不动, 右指针往前移动
2. 一直移动到滑动窗口内出现重复字符, 右指针不动, 左指针往前移动, 直到滑动窗口内没有了重复字符 循环 1, 2
"""

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = collections.defaultdict(int)
        i, j = 0, 0
        res = 0
        for i in range(len(s)):
            d[s[i]] += 1
            while (d[s[i]] > 1):
                d[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res
