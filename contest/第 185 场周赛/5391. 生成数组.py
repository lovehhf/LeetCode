# -*- coding:utf-8 -*-

"""
链接：https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons

给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。
请你生成一个具有下述属性的数组 arr ：

arr 中有 n 个整数。
1 <= arr[i] <= m 其中 (0 <= i < n) 。
将上面提到的算法应用于 arr ，search_cost 的值等于 k 。
返回上述条件下生成数组 arr 的 方法数 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。

示例 1：
输入：n = 2, m = 3, k = 1
输出：6
解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

示例 2：
输入：n = 5, m = 2, k = 3
输出：0
解释：没有数组可以满足上述条件

示例 3：
输入：n = 9, m = 1, k = 1
输出：1
解释：可能的数组只有 [1, 1, 1, 1, 1, 1, 1, 1, 1]

示例 4：
输入：n = 50, m = 100, k = 25
输出：34549172
解释：不要忘了对 1000000007 取余

示例 5：
输入：n = 37, m = 17, k = 7
输出：418930126

提示：
1 <= n <= 50
1 <= m <= 100
0 <= k <= n

search_cost: 从前向后寻找最大值的过程中最大值更新了多少次

暴力dp,

状态表示:
  dp[i][j][k]: 前 i 个数字, search_cost = j, 当前最大值为 k 的方案数
"""


class Solution:

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0] * (55) for _ in range(55)] for _ in range(150)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):  # 从 1 到 n 递推
            for p in range(0, k + 1): # 前一个状态的 search_cost = p
                for l in range(0, m + 1): # 前一个状态的最大值 = l
                    for v in range(1, m + 1):  # 枚举当前状态的填 v, 可以是 1 到 m 之间的任意一个数
                        # 两种情况
                        # 1: v > l, 需要更新最大值，且search_cost要+1
                        # 2. v <= l, 不更新最大值
                        np = p
                        nv = max(v, l)
                        if (v > l):
                            np += 1
                        # 状态转移, 当前search_cost = np, 当前最大值 = nv 的方案数
                        # 从前 i - 1 个数, search_cost = p, 最大值 l 的情况下, 在后面接一个数字 v 转移
                        dp[i][np][nv] += (dp[i][np][nv] + dp[i - 1][p][l]) % MOD

        return sum(dp[n][k]) % MOD

s = Solution()
n, m, k = 37, 17, 7
print(s.numOfArrays(n, m, k))

