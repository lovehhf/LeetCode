# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        和ThreeSum类似
        先排序,然后遍历，使用双指针扫描
        时间复杂度O(n^2)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = 0  # 三数之和
        min_diff = float('inf')  # 三数之和与target的最小差的绝对值
        for i in range(n):
            L, R = i + 1, n - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                if abs(s - target) < abs(min_diff):
                    min_diff = abs(s - target)
                    res = s
                if s > target:
                    R -= 1
                elif s < target:
                    L += 1
                else:
                    return s
        return res


# def threeSumClosest(nums, target):
#     """
#     :param nums: List
#     :param target: int
#     :return: int
#     """
#     len_nums = len(nums)
#     nums.sort()
#     res = nums[0] + nums[1] + nums[2]
#     for i in range(0, len_nums - 2):
#         left, right = i + 1, len(nums) - 1
#         while left < right:
#             threeSum = nums[i] + nums[left] + nums[right]
#             if threeSum > target:
#                 right -= 1
#             elif threeSum < target:
#                 left += 1
#             else:
#                 return target
#             # print(res)
#             res = threeSum if abs(threeSum - target) < abs(res - target) else res
#     return res
#

nums = [1,2,4,8,16,32,64,128]
target = 82

s = Solution()
print(s.threeSumClosest(nums, target))
