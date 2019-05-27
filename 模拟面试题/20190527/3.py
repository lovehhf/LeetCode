# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

每次都要排除掉1/4不可能的数
1 2 3
1 3 4 5 6
ia = 1,ib = 2, 2<4 干掉4 5 6->

"""


class Solution(object):
    def kth(self, A, B, k):
        """
        找出两个排序数组第k小的数(k从0开始)
        """
        # print(A, B, k)
        if not A:
            return B[k]
        if not B:
            return A[k]
        m, n = len(A), len(B)
        ia, ib = m >> 1, n >> 1
        ma, mb = A[ia], B[ib]
        # print(ia, ib, ma, mb)
        if ma < mb:
            if k <= ia + ib:
                return self.kth(A, B[:ib], k)
            else:
                return self.kth(A[ia + 1:], B, k - ia - 1)
        else:
            if k <= ia + ib:
                return self.kth(A[:ia], B, k)
            else:
                return self.kth(A, B[ib + 1:], k - ib - 1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        mid = (m + n - 1) >> 1
        if (m + n) & 1:
            return self.kth(nums1, nums2, mid)
        else:
            return (self.kth(nums1, nums2, mid) + self.kth(nums1, nums2, mid + 1))/2


s = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(s.kth(nums1, nums2, 1))
print(s.findMedianSortedArrays(nums1, nums2))
