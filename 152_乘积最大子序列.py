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

# 还是想复杂了
# 0:截断列表
# 负数: 1个:记录,放弃 2个:乘
# [2,3,-2,4]
# 使用栈记录上一个负数出现的位置,出现0的话栈置空,ls[i]置为0
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        动态规划
        :param nums:
        :return:
        """
        n = len(nums)
        f, g = [0] * n, [0] * n  # f[i]表示以i结尾的子数组能产生的最大值,g[i]表示以i结尾的子数组能产生的最小值
        f[0], g[0] = nums[0], nums[0]
        for i in range(1, n):
            f[i] = max(max(f[i - 1] * nums[i], g[i - 1] * nums[i]), nums[i])
            g[i] = min(min(f[i - 1] * nums[i], g[i - 1] * nums[i]), nums[i])
        return max(f)

    def maxProduct2(self, nums):
        """
        暴力解法
        求最大值，可以看成求被0拆分的各个子数组的最大值。
        当一个数组中没有0存在，则分为两种情况：
        1.负数为偶数个，则整个数组的各个值相乘为最大值；
        2.负数为奇数个，则从左边开始，乘到最后一个负数停止有一个“最大值”，从右边也有一个“最大值”，比较，得出最大值。
        :param nums:
        :return:
        """
        m = 1
        res = nums[0]
        for i in nums:
            m *= i
            if res < m:
                res = m
            if i == 0:
                m = 1
        m = 1
        for i in nums[::-1]:
            m *= i
            if res < m:
                res = m
            if i == 0:
                m = 1
        return res

    # def maxProduct(self, nums):
    #     """
    #     不太行 [2,-5,-2,-4,3] 过不去
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     ls = [0] * n
    #     ls[0] = nums[0]
    #     stack = [] if nums[0] >= 0 else [0]
    #     for i in range(1, n):
    #         if nums[i] == 0:
    #             ls[i] = 0
    #             stack = []
    #         elif nums[i] < 0:
    #             if not stack:
    #                 stack.append(i)
    #                 ls[i] = nums[i]
    #             else:
    #                 j = stack.pop()
    #                 ls[i] = 1
    #                 print(j)
    #                 for k in range(j, i + 1):
    #                     ls[i] *= nums[k]
    #                 if j > 0 and ls[j - 1] > 0:
    #                     ls[i] *= ls[j - 1]
    #         else:
    #             if ls[i - 1] > 0:
    #                 ls[i] = ls[i - 1] * nums[i]
    #             else:
    #                 ls[i] = nums[i]
    #     print(ls)
    #     return max(ls)


nums = [2, -5, -2, -4, 3]
s = Solution()
print(s.maxProduct(nums))
