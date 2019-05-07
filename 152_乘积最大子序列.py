# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

# 应该是想复杂了
# f(i,j) i~j的最大值
# [-2,0,-1]:
# f(0,0)=-2 f(1,1) = 0 f(2,2) = -1
# f(0,1)=max(f(0)*-2,f(1,1)*0,(0,0),f(1,1))

0:截断dp
负数: 1个:记录,放弃 2个:乘
[2,3,-2,4]
使用栈记录上一个负数出现的位置,出现0的话栈置空,dp[i]置为0

"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        stack = [] if nums >= 0 else [0]
        for i in range(n):
            if nums[i] == 0:
                dp[i] = 0
                stack = []
            elif nums[i] < 0:
                if not stack:
                    stack.append(i)
                else:
                    pass
            else:
                if stack:



nums = [2, 3, -2, 0, 4, -3, 5]
s = Solution()
print(s.maxProduct(nums))
