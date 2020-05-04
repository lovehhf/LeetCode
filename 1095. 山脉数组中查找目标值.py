# -*- coding:utf-8 -*-

"""
1095. 山脉数组中查找目标值
链接：https://leetcode-cn.com/problems/find-in-mountain-array

（这是一个 交互式问题 ）
给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
如果不存在这样的下标 index，就请返回 -1。

何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
首先，A.length >= 3
其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度
 
注意：
对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。
为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。

示例 1：
输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。

示例 2：
输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。


提示：
3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation

class MountainArray:
    def __init__(self, nums):
        self.nums = nums

    def get(self, idx: int) -> int:
        return self.nums[idx]

    def length(self) -> int:
        return len(self.nums)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l, r = 0, n - 1

        # 二分寻找山顶(162，寻找峰值)
        while (l < r):
            mid = (l + r + 1) >> 1
            # 左边有序， 可以排除 0 ~ i -1
            if mountain_arr.get(mid) > mountain_arr.get(mid - 1):
                l = mid
            else:
                r = mid - 1

        top_idx = l

        # 在左边寻找 >= target 的左边界
        l, r = 0, top_idx
        while (l < r):
            mid = (l + r) >> 1
            if mountain_arr.get(mid) >= target:
                r = mid
            else:
                l = mid + 1

        # 刚好等于 target, 直接返回
        if (mountain_arr.get(l) == target):
            return l

        # 右边找 <= target 的左边界
        l, r = top_idx, n - 1
        while (l < r):
            mid = (l + r) >> 1
            if mountain_arr.get(mid) <= target:
                r = mid
            else:
                l = mid + 1

        return l if mountain_arr.get(l) == target else -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
        87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89,
        88, 87, 86, 85, 84, 83, 82]
target = 101
s = Solution()
mountain_arr = MountainArray(nums)
print(s.findInMountainArray(target, mountain_arr))
