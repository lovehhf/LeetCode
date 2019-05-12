# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出整数数组 A，将该数组分隔为长度最多为 K 的几个（连续）子数组。分隔完成后，每个子数组的中的值都会变为该子数组中的最大值。
返回给定数组完成分隔后的最大和。


示例：

输入：A = [1,15,7,9,2,5,10], K = 3
输出：84
解释：A 变为 [15,15,15,9,10,10,10]
 

提示：
1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
"""


class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        dp[i]: A[0]~A[i]的最大和
        状态转移方程:
        0~K-1: dp[i] = max(A[:i + 1])*(i+1)
        K~n: 从i-K遍历到i,找出最大的值就是dp[i]
        dp[i] = max(dp[i], dp[i - j] + max(A[i - j + 1:i + 1]) * j)
        eg:对于[1,15,7,9,2,5,10],第4个元素9,dp[0]=1,dp[2]=30,dp[3]=45
        遍历下标为1,2,3的元素,dp[3] = max(dp[0]+15*3,dp[1]+15*2,dp[2]+9*1)
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        dp = [0] * n
        for i in range(n):
            if i < K:
                dp[i] = max(A[:i + 1]) * (i + 1)
            else:
                dp[i] = max([dp[i - j] + max(A[i - j + 1:i + 1]) * j for j in range(K,0,-1)])
        return dp[-1]


A = [1, 15, 7, 9, 2, 5, 10]
K = 3
s = Solution()
print(s.maxSumAfterPartitioning(A, K))
