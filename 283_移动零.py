# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        R = L+1
        # 快慢指针
        # 快指针指向0后面的数 且往后寻找
        # 慢指针指向第一个0
        while R<len(nums):
            # 快指针!=0 且慢指针=0时 则交换
            # 快指针=0时 且慢指针=0时 快指针+1 慢指针不动
            if nums[R] != 0:
                if nums[L] == 0:
                    nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R += 1
            else:
                if nums[L] != 0:
                    L += 1
                R += 1



nums = [1,0,1]
s = Solution()
s.moveZeroes(nums)
print(nums)