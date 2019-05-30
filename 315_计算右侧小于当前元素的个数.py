# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

逆序对的数量,带上索引一起归并排序
[(2,1),(5,0)],[(1,3),(6,2)]->[1,0,1,0]

"""


class Solution(object):
    def merge(self, L, R):
        """
        归并2条带索引的有序数组
        :param L:
        :param R:
        :return:
        """
        # print(L, R)
        m, n = len(L), len(R)
        i, j = 0, 0
        ret = []
        # 时间复杂度高了
        while i < m and j < n:
            a, b = L[i], R[j]
            if a[0] <= b[0]:
                ret.append(a)
                i += 1
            else:
                ret.append(b)
                j += 1
                for k in range(i, m):
                    self.counts[L[k][1]] += 1
        if i == m:
            ret.extend(R[j:])
        if j == n:
            ret.extend(L[i:])
        # print(self.counts)
        return ret

    def mergeSort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        mid = n >> 1
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        self.counts = [0] * n
        nums = [(nums[i], i) for i in range(n)]
        self.mergeSort(nums)
        return self.counts


nums = [5, 2, 6, 1]
s = Solution()
print(s.countSmaller(nums))
