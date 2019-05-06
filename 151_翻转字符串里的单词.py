# -*- coding:utf-8 -*-

__author__ = 'huanghf'

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])


s = "  hello       world  "
sol = Solution()
print(sol.reverseWords(s))