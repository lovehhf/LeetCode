# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        类快排
        :param nums:
        :param k:
        :return:
        """

        def partition(nums, L, R, n):
            """
            三路快排partition,左:>n的数 中:n 右:<n的数
            :param nums: 数组
            :param L: 需要partition的数组的左边界下标
            :param R: 数组右边界下标
            :param n:
            :return: =n的数的左区间索引和右区间索引
            """
            left, right = L - 1, R + 1  # >n区域的右边界,<n区域左边界
            cur = L
            while cur < right:
                if nums[cur] > n:  # 当前数比n大,left+1与cur交换 左边界右移
                    nums[left + 1], nums[cur] = nums[cur], nums[left + 1]
                    cur += 1
                    left += 1
                elif nums[cur] < n:  # 当前数比n小,right-1与cur交换,右边界左移
                    nums[cur], nums[right - 1] = nums[right - 1], nums[cur]
                    right -= 1
                else:
                    cur += 1
            return left + 1, right - 1

        def quickSort(nums, L, R, k, i):
            """
            类三路快排 1940 ms
            :param nums: 数组
            :param L: 排序左边界
            :param R: 排序右边界
            :param k: 要找的第k个数
            :param i: 快排需要比较的的数索引
            :return:  要找的数
            """
            p, q = partition(nums, L, R, nums[i])
            # [3, 2, 3, 1, 2, 4, 5, 5, 6] -> [6, 5, 5, 4, 3, 3, 2, 1, 2] -> (4,5)
            if p > k:  # p>k 在前半边找,q<k在后半边找
                return quickSort(nums, L, p - 1, k, L)
            elif q < k:
                return quickSort(nums, q + 1, R, k, R)
            else:
                return nums[k]

        return quickSort(nums, 0, len(nums) - 1, k - 1, 0)

    def findKthLargest2(self, nums, k):
        """
        建立一个k个大小的小根堆
        从第k+1个元素开始从左往右遍历,如果遇到的元素比堆顶大,则与堆顶元素交换,调整小根堆
        :param nums:
        :param k:
        :return:
        """
        pass

    def findKthLargest3(self, nums, k):
        """
        首先想到的方法  76 ms
        """
        return sorted(nums)[-k]


nums = [3, 2, 1, 5, 6, 4]
k = 2
s = Solution()
print(s.findKthLargest2(nums, k))
