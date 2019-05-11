# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        旋转数组最少有一边是有序的, 分各种情况讨论
        mid>L: 左边有序(再分mid>target(再讨论L小于target的情况) 和 mid<target )
        mid<L: 左边无序(必有右边有序,再分各种情况讨论)
        20190511
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        L, R = 0, n - 1
        while L <= R:
            mid = (L + R) >> 1
            # print(L, mid, R)
            # print('NUMS: ', nums[L], nums[mid], nums[R])
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[L]:
                if nums[L] < target:
                    if nums[mid] > target:
                        R = mid - 1
                    else:
                        L = mid + 1
                elif nums[L] > target:
                    L = mid + 1
                else:
                    return L
            else:
                if nums[R] > target:
                    if nums[mid] < target:
                        L = mid + 1
                    else:
                        R = mid - 1
                elif nums[R] < target:
                    R = mid - 1
                else:
                    return R
        return -1

    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, mid, r)
            if nums[mid] == target:
                return mid
            # 中间值大于目标值的情况
            if nums[mid] > target:
                # 左边有序
                if nums[mid] > nums[l]:
                    # 左边有序 中间值和最左边的值都大于目标值的情况 不可能在左区间  从右区间找
                    if nums[l] > target:
                        l = mid + 1
                    # 左边有序 中间值大于目标值 最左边的值小于目标值的情况 在左区间
                    elif nums[l] < target:
                        r = mid - 1
                    else:
                        return l
                # 右边有序 且中间值大于目标值 只可能在左区间
                elif nums[mid] < nums[l]:
                    r = mid - 1
                # [3,1] 1 l:0 mid:0 r:1
                else:
                    l = mid + 1
            # 中间值小于目标值的情况
            else:
                # 右边有序
                if nums[mid] < nums[r]:
                    # 右边有序 中间值小于目标值且最右边的值大于目标值 在右区间
                    if nums[r] > target:
                        l = mid + 1
                    # 右边有序 中间值小于目标值且最右边的值小于于目标值 不可能在右区间 可能在左区间
                    elif nums[r] < target:
                        r = mid - 1
                    else:
                        return r
                else:
                    l = mid + 1
        return -1


nums = [3,1]
target = 3
s = Solution()
print(s.search(nums, target))
