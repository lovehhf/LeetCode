# -*- coding:utf-8 -*-

"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

限制：
0 <= 数组长度 <= 50000

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        l, r = 0, len(nums) - 1
        while (l < r):
            mid = (l + r) >> 1
            if (nums[mid] >= target):
                r = mid
            else:
                l = mid + 1
        if nums[l] != target:
            return 0

        left = l
        l, r = 0, len(nums) - 1
        while (l < r):
            mid = (l + r + 1) >> 1
            if (nums[mid] <= target):
                l = mid
            else:
                r = mid - 1
        return r - left + 1
