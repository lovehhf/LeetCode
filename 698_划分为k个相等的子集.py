# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
 

注意:

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000

416. 分割等和子集
"""


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        回溯
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        def dfs(k, s, index):
            if s == target:
                return dfs(k - 1, 0, 0)
            if k == 1:
                return True
            for i in range(index, n):
                if i not in visted and nums[i] + s <= target:
                    visted.add(i)
                    if dfs(k, s + nums[i], i + 1):
                        return True
                    visted.remove(i)
            return False

        if sum(nums) % k:
            return False
        target = sum(nums) // k
        nums.sort(reverse=True)
        n = len(nums)
        visted = set()
        return dfs(k, 0, 0)


nums = [730, 580, 401, 659, 5524, 405, 1601, 3, 383, 4391, 4485, 1024, 1175, 1100, 2299, 3908]
k = 4
s = Solution()
print(s.canPartitionKSubsets(nums, k))
