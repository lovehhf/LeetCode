# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        python使用sorted的cmp_to_key参数自定义排序规则,python2可以直接用cmp参数。
        :type nums: List[int]
        :rtype: str
        """
        if any(nums):
            from functools import cmp_to_key
            # nums = sorted([str(x) for x in nums], key=cmp_to_key(lambda x, y: int(x + y) if int(x + y) > int(y + x) else int(x + y)),reverse=True)
            nums = sorted([str(x) for x in nums], key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)
            return ''.join(nums)
        return '0'

    def largestNumber2(self, nums):
        """
        三路快排
        :type nums: List[int]
        :rtype: str
        """
        def quickSort(nums):
            if not nums:
                return []
            l = quickSort([x for x in nums if int(x + nums[0]) < int(nums[0] + x)])
            m = [x for x in nums if int(x + nums[0]) == int(nums[0] + x)]
            r = quickSort([x for x in nums if int(x + nums[0]) > int(nums[0] + x)])
            return l + m + r

        if all(x == 0 for x in nums) or not nums:
            return '0'
        return ''.join(quickSort([str(x) for x in nums])[::-1])


nums = [0,9,8,7,6,5,4,3,2,1]
s = Solution()
print(s.largestNumber2(nums))
