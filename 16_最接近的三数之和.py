# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def threeSumClosest(nums, target):
    """
    :param nums: List
    :param target: int
    :return: int
    """
    len_nums = len(nums)
    nums.sort()
    res = nums[0]+nums[1]+nums[2]
    for i in range(0, len_nums - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            threeSum = nums[i] + nums[left] + nums[right]
            if threeSum > target:
                right -= 1
            elif threeSum < target:
                left += 1
            else:
                return target
            # print(res)
            res = threeSum if abs(threeSum - target) < abs(res - target) else res
    return res


nums = [-1, 2, 1, -4]
target = 1

print(threeSumClosest(nums, target))
