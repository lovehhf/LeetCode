# -*- coding:utf-8 -*-

"""
链接：https://leetcode-cn.com/problems/constrained-subset-sum

给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，
子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。
数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。

示例 1：
输入：nums = [10,2,-10,5,20], k = 2
输出：37
解释：子序列为 [10, 2, 5, 20] 。

示例 2：
输入：nums = [-1,-2,-3], k = 1
输出：-1
解释：子序列必须是非空的，所以我们选择最大的数字。

示例 3：
输入：nums = [10,-2,-10,-5,20], k = 2
输出：23
解释：子序列为 [10, -2, -5, 20] 。

提示：
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

dp + 单调队列

滑动窗口最大值
"""
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        f = [0] * n
        f[0] = nums[0]    # f[i]: 以 f[i] 结尾且选 nums[i] 时的最大子序列和
        queue = [0] # 单调队列， 维护 f[i] 前面 k 个最大值
        for i in range(1, n):

            if i - queue[0] > k:
                queue.pop(0)

            f[i] = max(f[queue[0]] + nums[i], nums[i])  # 在 f[i] 的前面 k 中选一个最大的 (单调队列队首元素), 或者不选

            while queue and f[queue[-1]] < f[i]:
                queue.pop()

            queue.append(i)

        return max(f)


nums = [10,2,-10,5,20]
k = 2
s = Solution()
print(s.constrainedSubsetSum(nums, k))