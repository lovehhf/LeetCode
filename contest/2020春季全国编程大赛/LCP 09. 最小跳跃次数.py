# -*- coding:utf-8 -*-

"""
为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。
若小球在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。
也就是说，在编号为 i 弹簧处按动弹簧，小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。
小球位于编号 0 处的弹簧时不能再向左弹。
为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。

示例 1：
输入：jump = [2, 5, 1, 1, 1, 1]
输出：3

解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。

限制：
1 <= jump.length <= 10^6
1 <= jump[i] <= 10000

bfs
"""

from typing import List
import collections

class Solution:
    def minJump(self, jump: List[int]) -> int:
        n = len(jump)
        vis = [0] * (n + 100)
        queue = collections.deque([(0, 0)])

        j = 1  # 保存已经遍历过的点的的右边界, j 前面的肯定是已经访问过的点，把时间复杂度 O(n^2) 降到 O(2*n)
        while (queue):
            cur, res = queue.popleft()

            if cur >= n:
                return res

            if cur + jump[cur] >= n:
                return res + 1

            vis[cur] = 1
            if not vis[cur + jump[cur]]:   # 往右边跳
                queue.append((cur + jump[cur], res + 1))

            # 往左边跳
            for i in range(j, cur):
                if not vis[i]:
                    queue.append((i, res + 1))

            j = max(j, cur)

        return 0


sol = Solution()
jump = [1] * 10 ** 6
print(sol.minJump(jump))