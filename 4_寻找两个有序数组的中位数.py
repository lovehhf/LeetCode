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

参考: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
"""


class Solution(object):
    def kth(self, a, b, k):
        """
        寻找两个排序数组中第k小的数
        :param a: 数组1
        :param b: 数组2
        :param k:
        :return:
        """
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        # k 大于a和b的中间索引和
        if ia + ib < k:
            # a中间的数大于b中间数的情况
            # 去掉b的前半段递归,原问题转换成在a,和b[ib+1:]两个数组中找出第k-(ib+1)小的数
            # eg:[1,3,5,7,9] [3,4,5,6] 找第6小的数 ma=5,mb=4 则第6小的数不可能会存在b数组的4和前面的数中(由于ma>mb,第k小的数是可能存在于a的前半段的)
            # 原问题转化成[1,3,5,7,9]和[5,6]中找第4小的数
            # 有点像在64匹马8条赛道中找出最快的8匹马的思想
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # ia+ib>=k的情况 剔除中间数较大的后半段
        else:
            # eg:[1,3,5,7,9] [3,4,5,6] 找第2小的数,ia,ib=2,1,剔除a的后半段,原问题转化成[1,3],[3,4,5,6]找第2小的数
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        奇数: 找出nums1, nums2中的第m+n//2大的数
        偶数: eg: [1,2],[3,4,5,6] -> m+n=6, 中位数index:2,3 = (m+n)//2-1,(m+n)//2
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if (m + n) % 2:
            return self.kth(nums1, nums2, (m + n) // 2)
        else:
            a = self.kth(nums1, nums2, (m + n) // 2 - 1)
            b = self.kth(nums1, nums2, (m + n) // 2)
            return  (a+b)/2


nums1 = [1,2]
nums2 = [3,4]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
