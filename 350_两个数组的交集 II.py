# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        不借助外部空间
        :param nums1:
        :param nums2:
        :return:
        """
        # 预排序处理
        nums1.sort()
        nums2.sort()
        # 双指针
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res

    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            # 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
            # 骚操作
            l += [i] * min(nums1.count(i), nums2.count(i))
        return l

    def intersect3(self, nums1, nums2):
        """
        借助字典
        :param nums1:
        :param nums2:
        :return:
        """
        d = {}
        res = []

        for i in nums1:
            d[i] = d.get(i,0) + 1

        for i in nums2:
            if d.get(i, 0) > 0:
                res.append(i)
                d[i] = d.get(i) - 1
        return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s = Solution()
print(s.intersect3(nums1, nums2))
