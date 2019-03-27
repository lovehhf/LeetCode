# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums):
        res = [[]]
        """
        从前往后遍历,遇到一个数则就把上一个的所有子集 加上该数组成新的子集
        [1]的子集: [[],[1]]
        [1,2]的子集: [[],[1]] + [[]+[2],[1]+[2]]
        ...
        """
        for i in nums:
            res += [t+[i] for t in res]
        return res
        # for i in range(n): #循环次数
        #     # 方法不对,没有考虑间隔大于1的情况
        #     l = 0    # 列表切片的左边界
        #     r = n-i  # 列表切片的右边界
        #     while r<=n:
        #         res.append(nums[l:r])
        #         l+=1
        #         r+=1
        # return res

nums = [1,2,3,4]
s = Solution()
print(s.subsets(nums))
