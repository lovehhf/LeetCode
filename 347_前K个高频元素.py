# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""



import collections
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        d存放元素出现的次数

        时间复杂度O(nlogk
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        for num in nums:
            d[num]+=1
        d = [(v,k) for k,v in d.items()]
        res = [x[1] for x in heapq.nlargest(k,d)]
        return res



nums = [1,1,1,2,2,3]
k = 2
s = Solution()
print(s.topKFrequent(nums,k))