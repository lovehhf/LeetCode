# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给你一个整数数组 arr 和一个整数 difference，请你找出 arr 中所有 相邻元素之间的差等于给定 difference 的等差子序列，并返回其中最长的等差子序列的长度。

示例 1：

输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
示例 2：

输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。
示例 3：

输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。
 

提示：

1 <= arr.length <= 10^5
-10^4 <= arr[i], difference <= 10^4
"""


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        n = len(arr)
        d = {}
        for i in range(n):
            d[arr[i]] = d.get(arr[i] - difference, 0) + 1
        return max(d.values())



arr = [1,5,7,8,5,3,4,2,1]
difference = -2
s = Solution()
print(s.longestSubsequence(arr,difference ))