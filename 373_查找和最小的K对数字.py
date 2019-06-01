# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。

找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。

示例 1:

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
示例 3:

输入: nums1 = [1,2], nums2 = [3], k = 3 
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
"""

import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        优化堆
        :param nums1:
        :param nums2:
        :param k:
        :return:
        """
        if not nums1 or not nums2:
            return []
        m, n = len(nums1), len(nums2)
        heap = []
        res = []
        vis = [[0]*n for _ in range(m)]
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        while k and heap:
            x, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i < m - 1 and not vis[i+1][j]:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                vis[i+1][j] = 1
            if j < n - 1 and not vis[i][j+1]:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                vis[i][j+1] = 1
            k -= 1
        return res

    def kSmallestPairs2(self, nums1, nums2, k):
        """
        暴力做法
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [[x, y] for x in nums1 for y in nums2]
        return heapq.nsmallest(k, nums, key=lambda x: x[0] + x[1])


s = Solution()
nums1 = [1, 2, 4]
nums2 = [-1, 1, 2]
k = 100
print(s.kSmallestPairs(nums1, nums2, k))
print(s.kSmallestPairs2(nums1, nums2, k))
