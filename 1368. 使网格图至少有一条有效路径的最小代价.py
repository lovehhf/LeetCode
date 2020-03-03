# -*- coding:utf-8 -*-

"""
给你一个 m x n 的网格图 grid 。 grid 中每个格子都有一个数字，对应着从该格子出发下一步走的方向。 grid[i][j] 中的数字可能为以下几种情况：

1 ，下一步往右走，也就是你会从 grid[i][j] 走到 grid[i][j + 1]
2 ，下一步往左走，也就是你会从 grid[i][j] 走到 grid[i][j - 1]
3 ，下一步往下走，也就是你会从 grid[i][j] 走到 grid[i + 1][j]
4 ，下一步往上走，也就是你会从 grid[i][j] 走到 grid[i - 1][j]
注意网格图中可能会有 无效数字 ，因为它们可能指向 grid 以外的区域。

一开始，你会从最左上角的格子 (0,0) 出发。我们定义一条 有效路径 为从格子 (0,0) 出发，每一步都顺着数字对应方向走，最终在最右下角的格子 (m - 1, n - 1) 结束的路径。有效路径 不需要是最短路径 。
你可以花费 cost = 1 的代价修改一个格子中的数字，但每个格子中的数字 只能修改一次 。
请你返回让网格图至少有一条有效路径的最小代价。

示例 1：
输入：grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
输出：3
解释：你将从点 (0, 0) 出发。
到达 (3, 3) 的路径为： (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) 花费代价 cost = 1 使方向向下 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 花费代价 cost = 1 使方向向下 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) 花费代价 cost = 1 使方向向下 --> (3, 3)
总花费为 cost = 3.

示例 2：
输入：grid = [[1,1,3],[3,2,2],[1,1,4]]
输出：0
解释：不修改任何数字你就可以从 (0, 0) 到达 (2, 2) 。

示例 3：
输入：grid = [[1,2],[4,3]]
输出：1

示例 4：
输入：grid = [[2,2,2],[2,2,2]]
输出：3

示例 5：
输入：grid = [[4]]
输出：0

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        暴力dfs, 需要遍历所有的路径才能确定最短路, 最多只能过个测试用例
        这里可以使用双向队列实现 0-1 bfs
        如果某条边权值为0, 就自然的作为下一次扩展的起点, 如果某条边权值为1, 就正常的放入队尾。
        这样就保证了在节点不重复入队的情况下，队头元素一定是权值最小的节点
        :param grid:
        :return:
        """
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0)])    # 双端队列, queue[i][j][k] 表示到(i,j)的距离为k
        ds = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = [[0] * n for _ in range(m)]
        vis[0][0] = 1
        while queue:
            i, j, cost = queue.popleft()

            # 记录已经遍历过的最短路的点
            vis[i][j] = 1

            if (i == m - 1 and j == n - 1):
                return cost
            for k in range(1, 5):
                dx, dy = ds[k]
                x = i + dx
                y = j + dy
                if (x < 0 or x >= m or y < 0 or y >= n or vis[x][y]):
                    continue
                if (grid[i][j] == k):
                    # 边权为0, 插到队头
                    queue.appendleft((x, y, cost))
                else:
                    # 边权为1, 插到队尾
                    queue.append((x, y, cost + 1))
        return 0
