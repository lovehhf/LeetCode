

"""
有 n 个城市，按从 0 到 n-1 编号。给你一个边数组 edges，其中 edges[i] = [fromi, toi, weighti] 代表 fromi 和 toi 两个城市之间的双向加权边，距离阈值是一个整数 distanceThreshold。
返回能通过某些路径到达其他城市数目最少、且路径距离 最大 为 distanceThreshold 的城市。如果有多个这样的城市，则返回编号最大的城市。
注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和。

 

示例 1：
输入：n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
输出：3
解释：城市分布图如上。
每个城市阈值距离 distanceThreshold = 4 内的邻居城市分别是：
城市 0 -> [城市 1, 城市 2] 
城市 1 -> [城市 0, 城市 2, 城市 3] 
城市 2 -> [城市 0, 城市 1, 城市 3] 
城市 3 -> [城市 1, 城市 2] 
城市 0 和 3 在阈值距离 4 以内都有 2 个邻居城市，但是我们必须返回城市 3，因为它的编号最大。

示例 2：
输入：n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
输出：0
解释：城市分布图如上。 
每个城市阈值距离 distanceThreshold = 2 内的邻居城市分别是：
城市 0 -> [城市 1] 
城市 1 -> [城市 0, 城市 4] 
城市 2 -> [城市 3, 城市 4] 
城市 3 -> [城市 2, 城市 4]
城市 4 -> [城市 1, 城市 2, 城市 3] 
城市 0 在阈值距离 4 以内只有 1 个邻居城市。
 

提示：

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
所有 (fromi, toi) 都是不同的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def dijkstra(self, n, g, t, dist):
        res = -1
        vis = [0] * n

        for i in range(n):
            # 找出没有访问过的点中距离起点最近的点
            k = -1
            for j in range(n):
                if (not vis[j] and (k == -1 or dist[k] > dist[j])):
                    k = j

            if (dist[k] > t):
                return res

            vis[k] = 1
            res += 1

            # 更新没有访问过的点的距离
            for j in range(n):
                dist[j] = min(dist[j], dist[k] + g[k][j])

        return res

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = 0x3f3f3f3f
        g = [[INF] * n for _ in range(n)]

        # 邻接矩阵存稠密图
        for a, b, w in edges:
            g[a][b] = w
            g[b][a] = w

        res = -1
        min_v = n
        for i in range(n):
            dist = [INF] * n
            dist[i] = 0
            t = self.dijkstra(n, g, distanceThreshold, dist)
            # print(i, t)

            if t <= min_v:
                res = i
                min_v = t

        return res