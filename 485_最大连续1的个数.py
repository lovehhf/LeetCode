# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        计数
        :type nums: List[int]
        :rtype: int
        """
        res, tmp = 0, 0
        for i in nums:
            if i == 1:
                tmp += 1
            if i == 0:
                tmp = 0
            if tmp > res:
                res = tmp
        return res

    def findMaxConsecutiveOnes2(self, nums):
        """
        使用re
        :type nums: List[int]
        :rtype: int
        """
        import re
        if 1 not in nums:
            return 0
        nums_str = ''.join([str(x) for x in nums])
        return max([len(x) for x in re.findall('1+', nums_str)])

    def findMaxConsecutiveOnes3(self, nums):
        """
        以字符0分隔字符串
        :type nums: List[int]
        :rtype: int
        """
        nums_str = ''.join([str(x) for x in nums])
        res = max([len(x) for x in nums_str.split('0')])
        return res


nums = [1, 1, 0, 1, 1, 1]
s = Solution()
print(s.findMaxConsecutiveOnes3(nums))
