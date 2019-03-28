# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
返回一对观光景点能取得的最高分。


示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
"""


class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        bestPrev = 0
        result = 0
        for index, value in enumerate(A):
            result = max(result, value - index + bestPrev)
            bestPrev = max(bestPrev, value + index)
        return result

    def maxScoreSightseeingPair3(self, A) -> int:
        """
        :param A:
        :return:
        """
        n = len(A)
        tidx = 0
        maxSum = 0
        for i in range(1,n):
            # print(maxSum)
            maxSum = max(A[i]+A[tidx]+tidx-i, maxSum)
            if A[tidx]-A[i]<i-tidx:
                tidx=i
        return maxSum

    def maxScoreSightseeingPair2(self, A) -> int:
        """
        超时  待优化
        :param A:
        :return:
        """
        n = len(A)
        max_s = A[1]-A[0]-1
        for i in range(n-1):
            for j in range(i+1,n):
                s = A[j] + A[i]  + i - j
                if max_s<s:
                    max_s = s
        return max_s


A = [8,1,5,2,6]
s=Solution()
print(s.maxScoreSightseeingPair3(A))