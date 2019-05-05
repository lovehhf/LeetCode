# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。
假设两个玩家都以最佳状态参与游戏。

 

示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
"""


class Solution(object):

    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # dp[i] 表示N=i+1时Alice是否能赢
        dp = [False]*N

        dp[0] = False
        for i in range(1,N):
            t = []

            # t用来存储i+1的所有除数
            for j in range(1,i//2+1):
                if (i+1) % j == 0:
                    t.append(j)

            for j in t:
                # 如果Alice选择了这个除数后,N-这个除数后剩下的数为False的话则表示Alice能赢
                if dp[i-j] == False:
                    dp[i] = True
                    break
        return dp[-1]

    def divisorGame2(self, N):
        if N%2==0:
            return True
        return False

N = 1000
s = Solution()
print(s.divisorGame2(N))