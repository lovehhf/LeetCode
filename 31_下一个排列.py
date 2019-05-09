# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


1. 从右往左遍历 找到第一个不是顺序排列的数字,而不是第一个比最右的数小的数
2. 找到了这个数i之后再最后的数开始往右遍历,找到第一个比i大的数j与i交换,然后再对i后面的所有数重新排序
eg: 2302431 -> 2303124
从右往左遍历先找到第一个比右边小的数字2,然后找到从右往左找到第一个比2大的数字3，交换这两个数字，然后421重新排序为124
最后得到2303124
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                for j in range(n - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        break
                break
            i -= 1
        if i == 0:
            nums.sort()
        else:
            # tmp = sorted(nums[i:])
            # for j in range(i,n):
            #     nums[j] = tmp[j-i]
            nums[i:] = sorted(nums[i:])

    def nextPermutation2(self, nums):
        n = len(nums)
        i = n - 1
        if sorted(nums)[::-1] == nums:  # 逆序
            nums[:] = sorted(nums)
            return
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i + 1:] = sorted(nums[i + 1:])
                        break
                break
        nums[i + 1:] = sorted(nums[i + 1:])


nums = [2, 3, 0, 2, 4, 1]
s = Solution()
s.nextPermutation(nums)
print(nums)
