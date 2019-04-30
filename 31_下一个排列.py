# -*- coding:utf-8 -*-

__author__ = 'huanghf'

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while i > 0:
            if nums[i-1] < nums[i]:
                for j in range(n - 1, i - 1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1],nums[j] = nums[j],nums[i-1]
                        break
                break
            i -= 1
        print(i)
        if i == 0:
            nums.sort()
        else:
            # tmp = sorted(nums[i:])
            # for j in range(i,n):
            #     nums[j] = tmp[j-i]
            nums[i:] = sorted(nums[i:])

nums = [1,2,3]
s = Solution()
s.nextPermutation(nums)
print(nums)