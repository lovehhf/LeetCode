# -*- coding:utf-8 -*-

"""
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
你的目标是确切地知道 F 的值是多少。
无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

示例 1：
输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。

示例 2：
输入：K = 2, N = 6
输出：3

示例 3：
输入：K = 3, N = 14
输出：4

提示：
1 <= K <= 100
1 <= N <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

可以控制的情况: 在哪一层丢鸡蛋, 取最好情况
不能控制的情况: 鸡蛋碎不碎, 取最坏情况

状态表示: f[i][j]: 有 i 个鸡蛋, j 层楼 的最小移动次数
状态转移:

枚举 k 从 1 ~ j
1. 没碎: f[i][j] = f[i][j - k] + 1  (消耗了一次机会,可以排除前 i 层楼, 只剩下 k + 1 ~ n 层楼)
2. 碎了: f[i][j] = f[i - 1][k - 1] + 1  (消耗了一次移动机会和一个鸡蛋, 可以排除第 i 层及其以上的楼层)

f[i][j] = min(max(f[i][j - k], f[i - 1][k - 1])) + 1   k: 1..j
"""


class Solution:
    def superEggDrop(self, m: int, n: int) -> int:
        pass


class Plain_Solution:
    # 朴素解法, 时间复杂度O(k * n^2)
    def superEggDrop(self, m: int, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, n + 1):
            f[1][i] = i

        for i in range(1, m + 1):
            f[i][1] = 1

        for i in range(2, m + 1):  # i 个鸡蛋
            for j in range(2, n + 1):  # j 层楼
                f[i][j] = 10010
                for k in range(1, j):
                    # 枚举 0 ~ j - 1 层楼, 鸡蛋碎没碎的情况
                    # 碎: f[i - 1][k - 1] + 1, 没碎: f[i][j - k] + 1, 由于不知道会不会碎, 取两者的较大值
                    f[i][j] = min(f[i][j], max(f[i - 1][k - 1], f[i][j - k]) + 1)

        return f[m][n]


s = Solution()
k = 2
n = 2
print(s.superEggDrop(k, n))
