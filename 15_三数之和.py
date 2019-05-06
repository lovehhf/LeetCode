# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif (nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    r -= 1
        return res

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        d = {}
        res = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        # print(d)
        if d.get(0, 0) >= 3:
            res.append([0, 0, 0])
        l = set([x for x in nums if x < 0])
        r = set([x for x in nums if x > 0])
        for i in l:
            for j in r:
                k = -(i + j)
                if k in d:
                    if k == i or k == j:
                        if d[k] >= 2:
                            res.append([i, k, j])
                    else:
                        # k<i or k>j，意味着只取一边的，以防止重复
                        if k < i or k > j or k == 0:
                            res.append([i, k, j])
        return res

    # def threeSum2(nums):
    #     """
    #     https://leetcode-cn.com/submissions/detail/14040532/
    #     超出时间限制
    #     :param nums:
    #     :return:
    #     """
    #     # ans = []
    #     # len_muns = len(nums)
    #     # nums = sorted(nums)
    #     # # print(nums)
    #     # for i in range(0,len_muns):
    #     #     for j in range(i+1,len_muns):
    #     #         for k in range(j+1,len_muns):
    #     #             if nums[i]+nums[j]+nums[k]==0:
    #     #                 ans.append(sorted([nums[i],nums[j],nums[k]]))
    #     #
    #     # from functools import reduce
    #     # # ans = list(reduce(lambda x,y:x if y else [x,y],ans))
    #     # # print(ans)
    #     # #
    #     # # from itertools import groupby
    #     # # for k,g in groupby(ans):
    #     # #     print(k)
    #     # ans = list(map(tuple,ans))   # 将list转为tuple类型,不然set会报错,tuple不可更改
    #     # ans = set(ans)
    #     # return list(list(map(list,ans)))    # 转回list
    #
    #     dic = {}
    #     for ele in nums:
    #         if ele not in dic:
    #             dic[ele] = 0
    #         dic[ele] += 1
    #
    #     if 0 in dic and dic[0] > 2:
    #         rst = [[0, 0, 0]]
    #     else:
    #         rst = []
    #
    #     pos = [p for p in dic if p > 0]  # 正数列表
    #     neg = [n for n in dic if n < 0]  # 负数列表
    #
    #     print(dic)
    #
    #     for p in pos:
    #         for n in neg:
    #             # print(n,p)
    #             inverse = -(p + n)
    #             if inverse in dic:
    #                 if inverse == p and dic[p] > 1:
    #                     rst.append([n, p, p])
    #                 elif inverse == n and dic[n] > 1:
    #                     rst.append([n, n, p])
    #                 # 这里的inverse < n or inverse > p很trick，意味着只取一边的，以防止重复
    #                 elif inverse < n or inverse > p or inverse == 0:
    #                     rst.append([n, inverse, p])
    #     return rst
    #


s = Solution()
nums = [3, 0, -2, -1, 1, 2]
print(s.threeSum(nums))
