# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        借助字典实现
        :param ransomNote:
        :param magazine:
        :return:
        """
        d = {}
        for i in magazine:
            d[i] = d.get(i, 0) + 1
        for i in ransomNote:
            d[i] = d.get(i, 0) - 1
            if d[i] < 0:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        """
        使用replace函数
        replace(self, old, new, count=None)
        :param ransomNote:
        :param magazine:
        :return:
        """
        for i in ransomNote:

            if i in magazine:
                magazine = magazine.replace(i,'',1)
                ransomNote = ransomNote.replace(i,'',1)
        return ransomNote==''


ransomNote, magazine = "aa", "aab"
sol = Solution()
print(sol.canConstruct2(ransomNote, magazine))
