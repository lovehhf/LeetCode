# -*- coding:utf-8 -*-

"""
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。
 

示例 1：

输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
示例 2：

输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
示例 3：

输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3
示例 4：

输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-occurrences-of-a-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        如果长的字串满足条件，那么包含其中的字串也一定满足条件
        只需要关注最短的长度minSize
        """
        n = len(s)
        d = {}
        for i in range(minSize, n + 1):
            j = i - minSize
            k = s[j:i]
            if(len(set(k))) <= maxLetters:
                d[k] = d.get(k, 0) + 1

        return max(d.values()) if d.values() else 0
