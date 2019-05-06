# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定 N，想象一个凸 N 边多边形，其顶点按顺时针顺序依次标记为 A[0], A[i], ..., A[N-1]。

假设您将多边形剖分为 N-2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 N-2 个三角形的值之和。

返回多边形进行三角剖分后可以得到的最低分。
 

示例 1：

输入：[1,2,3]
输出：6
解释：多边形已经三角化，唯一三角形的分数为 6。

示例 2：
输入：[3,7,4,5]
输出：144
解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。

示例 3：
输入：[1,3,1,4,1,5]
输出：13
解释：最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。
 
提示：
3 <= A.length <= 50
1 <= A[i] <= 100

https://www.bilibili.com/video/av51556138

大问题转化成小问题
dp[i][j]表示从第i个点到第j个点得到的最优解

https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/286705/JavaC%2B%2BPython-DP
while there is edge connect A[i] and A[j].
We enumerate all points A[k] with i < k < j to form a triangle.
The score of this triangulation is dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k]

从底向下的dp过程

对于 六边形 [1,3,1,4,1,5] 
先划分为 [1,3,1],[3,1,4],[1,4,1],[4,1,5] 4个小三角形 分别计算分数为 3 12 4 20
再划分为 [1,3,1,4], [3,1,4,1],[1,4,1,5] 3个四边形 计算出四个四边形的分数为
1*3*4+[1,3,1]构成的三角形分数和 1*1*4+[3,1,4]构成的三角形的分数中的较小值
即dp[0][3] = min(dp[0][2] + A[0]*A[3]*A[2],dp[1][3]+A[0]*A[3]*A[1]) = min(7,24) = 7
同理可以算出dp[1][4]=7  dp[2][5] = 9 
这就求出了所有划分出来的三边形和四边形的最优解, 再对六边形划分为 [1,3,1,4,1] 和[3,1,4,1,5] 2个5边型
求出dp[0][4] = min(dp[0][3]+1*4*1,dp[0][2]+dp[2,4]+1*1*1,dp[1][3]+1*1*3) = 8
同理dp[1][5] = 22
上面就求出了所有的三、四、五边型所有划分的最优解
对于六边形[1,3,1,4,1,5] k遍历3,1,4,1划分成的所得到的最小值就是最优解
六边形的最优解就是上面这三种划分的最小值
"""

import sys


class Solution(object):
    def minScoreTriangulation(self, A):
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        for d in range(2, n):  # 三边形 - n边型 自底向上
            for i in range(0, n - d):  # n边型可以划分的i+1边型的个数遍历
                j = d + i  # i,j 表示i~j组成的多边形
                dp[i][j] = sys.maxsize  # 初始为最大整数
                for k in range(i + 1, j):  # 用k划分多边形
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])
        print(dp)
        return dp[0][n-1]

    # def minScoreTriangulation2(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     n = len(A)
    #     dp = [[0 for _ in range(n)] for _ in range(n)]
    #
    #     for d in range(2, n):
    #         for i in range(0, n - d):
    #             j = i + d
    #
    #             dp[i][j] = min(dp[i][k] + dp[k][j] + A[i] * A[j] * A[k] for k in range(i + 1, j))
    #             print(i,j,dp[i][j])
    #
    #             # dp[i][j] = sys.maxsize
    #             # for k in range(i + 1, j):
    #             #     dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])
    #     print(dp)
    #     return dp[0][n - 1]


A = [1, 3, 1, 4, 1, 5]
s = Solution()
print(s.minScoreTriangulation(A))
