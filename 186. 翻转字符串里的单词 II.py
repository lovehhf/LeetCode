
"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例：
输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

注意：
单词的定义是不包含空格的一系列字符
输入字符串中不会包含前置或尾随的空格
单词与单词之间永远是以单个空格隔开的

进阶：使用 O(1) 额外空间复杂度的原地解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def reverse(self, s, i, j):
        """
        对 s[i] ~ s[j] 之间的字母进行翻转
        """
        while(i < j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
    def reverseWords(self, s: List[str]) -> None:
        """
        两次翻转, 第一次整体翻转, 第二次对单个单词进行翻转
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        self.reverse(s, 0, n - 1)
        j = 0
        for i in range(n + 1):
            if i == n or s[i] == ' ':
                self.reverse(s, j, i - 1)
                j = i + 1
        