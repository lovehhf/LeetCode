# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        两数之和: 1, 167
        三数之和: 15
        四数之和: 18

        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif (nums[i] + nums[j] + nums[l] + nums[r]) < target:
                        l += 1
                    else:
                        r -= 1
        return res

        # d = {}
        # res = []
        # for i in nums:
        #     d[i] = d.get(i, 0) + 1
        # l = set([x for x in nums if x < 0])
        # r = set([x for x in nums if x > 0])
        # for i in l:
        #     for j in r:
        #         for k in nums:
        #             if k == i or k == j:
        #                 if d.get(k, 0) < 2:
        #                     continue
        #             n = target - i - j - k
        #             tmp = tuple(sorted([i,j,k,n]))
        #             if n in d:
        #                 if tmp in res:
        #                     continue
        #                 if n == k:
        #                     if n == i or n ==j:
        #                         if d.get(n,0)>=3:
        #                             res.append(tmp)
        #                     else:
        #                         if d.get(n,0)>=2:
        #                             res.append(tmp)
        #                 else:
        #                     if n==i or n==j:
        #                         if d.get(n, 0) >= 2:
        #                             res.append(tmp)
        #                     else:
        #                         res.append(tmp)
        # res = [list(x) for x in res]
        # return res


nums = [0, 0, 0, 0]
target = 1
s = Solution()
print(s.fourSum(nums, target))
