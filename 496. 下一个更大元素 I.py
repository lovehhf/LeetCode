# -*- coding:utf-8 -*-

"""
给你两个 没有重复元素 的数组nums1 和nums2，其中nums1是nums2的子集。
请你找出 nums1中每个元素在nums2中的下一个比其大的值。
nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
   对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
   对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
提示：

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
nums1和nums2中所有整数 互不相同
nums1 中的所有整数同样出现在 nums2 中

进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        单调栈 + 哈希表
        :param nums1:
        :param nums2:
        :return:
        """
        stk = []
        ht = {}

        for i in range(len(nums2) - 1, -1, -1):
            ht[nums2[i]] = i
            while stk and nums2[stk[-1]] <= nums2[i]:
                stk.pop()
            ht[nums2[i]] = nums2[stk[-1]] if stk else -1
            stk.append(i)

        res = [ht[x] for x in nums1]
        return res


nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))
