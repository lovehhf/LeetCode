# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""


class Solution:
    def sortColors(self, nums):
        """
        三路快排partition思想
        小于1的数移到左边,大于1的数移到右边
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = -1, n  # i:0的右边界,j:2的左边界
        cur = 0
        while cur < j:
            if nums[cur] == 0:
                nums[cur], nums[i + 1] = nums[i + 1], nums[cur]
                i += 1
            if nums[cur] == 2:
                nums[cur], nums[j - 1] = nums[j - 1], nums[cur]
                j -= 1
            else:
                cur += 1

    def sortColors2(self, nums):
        nums[:] = [x for x in nums if x == 0] + [x for x in nums if x == 1] + [x for x in nums if x == 2]

s = Solution()
nums = [1,2,0]
s.sortColors2(nums)
print(nums)
