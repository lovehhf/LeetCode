# -*- coding:utf-8 -*-

__author__ = 'huanghf'

class Solution:
    def twoSum(self, nums, target):
        for i,v1 in enumerate(nums):
            for j,v2 in enumerate(nums):
                if (v1+v2 == target):
                    return [i,j]

if __name__ == '__main__':
    s = Solution()
    print (s.twoSum([2, 7, 11, 15],9))
