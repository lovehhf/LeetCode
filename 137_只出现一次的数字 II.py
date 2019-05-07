# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99

https://www.qingdujun.com/article/single-number-ii/
http://www.cnblogs.com/grandyang/p/4263927.html
http://liadbiz.github.io/leetcode-single-number-problems-summary/
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        时间复杂度不符合要求
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i - 1] != nums[i] and nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

    def singleNumber2(self, nums):
        """
        位运算骚方法
        看不懂 以后再看
        :param nums:
        :return:
        """
        a, b = 0, 0
        for i in nums:
            b = (b ^ i) & ~a
            a = (a ^ i) & ~b
        return b


nums = [0, 1, 0, 1, 0, 1, 99]
s = Solution()
print(s.singleNumber2(nums))
