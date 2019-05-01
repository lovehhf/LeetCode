# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]:
        #     return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 处理最后一列
        for i in range(m - 1, -1, -1):
            if obstacleGrid[i][-1] == 0:
                dp[i][-1] = 1
            if obstacleGrid[i][-1] == 1:
                break
        # 处理最后一行
        for i in range(n - 1, -1, -1):
            if obstacleGrid[-1][i] == 0:
                dp[-1][i] = 1
            if obstacleGrid[-1][i] == 1:
                break

        # 从倒数第二行开始从后往前处理
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


obstacleGrid = [[0, 0], [1, 0]]
s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid))
