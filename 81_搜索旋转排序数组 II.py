# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。
若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            print(L,mid,R)

            if nums[mid] == target or nums[R] == target or nums[L] == target:
                return True
            # 左边有序
            if nums[mid] > nums[L]:
                # target在左区间
                if nums[mid] > target and nums[L] < target:
                    R = mid - 1
                else:
                    L = mid + 1
            # 右边有序
            elif nums[mid] < nums[R]:
                # 右边有序 target在右区间
                if nums[mid] < target and nums[R] > target:
                    L = mid + 1
                else:
                    R = mid - 1
            else:
                # [1,1,3,1] 3
                # [1,3,1,1,1] 3
                if nums[mid] == nums[L]:
                    L += 1
                else:
                    R -= 1
            # print(L, mid, R)
        return False


nums = [1,3,1,1,1]
target = 3
s = Solution()
print(s.search(nums, target))
