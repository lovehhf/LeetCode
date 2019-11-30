# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组 A，返回满足下面条件的 非空、连续 子数组的数目：
子数组中，最左侧的元素不大于其他元素。

示例 1：

输入：[1,4,2,5,3]
输出：11
解释：有 11 个有效子数组，分别是：[1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3]

示例 2：

输入：[3,2,1]
输出：3
解释：有 3 个有效子数组，分别是：[3],[2],[1]

示例 3：

输入：[2,2,2]
输出：6
解释：有 6 个有效子数组，分别为是：[2],[2],[2],[2,2],[2,2],[2,2,2] 。
 

提示：

1 <= A.length <= 50000
0 <= A[i] <= 100000
"""


class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # stack 用来存储顺序排列的 索引与数字
        stack = []
        res = 0
        n = len(nums)
        for i in range(n):
            # 当栈顶元素比i指向的数字大时,弹出栈顶元素并计算栈顶元素到i指向的数之间能组成的有效子数组的数目
            while stack and stack[-1][1] > nums[i]:
                res += i - stack.pop()[0]
            stack.append([i, nums[i]])
            # print(stack)
        while stack:
            res += n - stack.pop()[0]
        return res

    def validSubarrays2(self, nums):
        """
        超时
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] <= nums[j]:
                    res += 1
                else:
                    break
        return res

nums = [1, 4, 2, 5, 3]
s = Solution()
print(s.validSubarrays(nums))
