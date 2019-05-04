# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""


class Solution(object):

    def rotate(self, nums, k):
        """
        方法一:
        对前n-k个和后k个数组进行局部翻转,然后整体翻转
        [1,2,3,4,5,6,7]
        ->
        [4,3,2,1,7,6,5]
        ->
        [5,6,7,1,4,3,2]

        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse_list(nums, 0, n - k - 1)
        self.reverse_list(nums, n - k, n - 1)
        self.reverse_list(nums, 0, n - 1)

    def reverse_list(self, nums, l, r):
        """
        列表的局部翻转
        :param l:
        :param r:
        :return:
        """
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate2(self, nums, k):
        """
        方法二:
        双重循环
        [1,2,3,4,5,6,7] -> [1,1,2,3,4,5,6] -> [7,1,2,3,4,5,6]
        ...
        """
        n = len(nums)
        k = k % n
        for i in range(k):
            tmp = nums[n - 1]
            for j in range(n - 1, -1, -1):
                nums[j] = nums[j - 1]
            nums[0] = tmp
        return list(reversed(nums[:n - k][::-1] + nums[n - k:][::-1]))

    def rotate3(self, nums, k):
        n = len(nums)
        nums[:] = nums[n - k % n:] + nums[:n - k % n]

    def rotate4(self, nums, k):
        k = k%len(nums)
        for _ in range(k):
            nums.insert(0,nums.pop())

    def rotate5(self, nums, k):
        k = k%len(nums)
        nums.reverse()
        nums[:] = list(reversed(nums[:k])) + list(reversed(nums[k:]))

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s = Solution()
s.rotate5(nums, k)
print(nums)
