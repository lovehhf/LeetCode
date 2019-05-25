# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在二维平面上，我们将石头放置在一些整数坐标点上。每个坐标点上最多只能有一块石头。
现在，move 操作将会移除与网格上的某一块石头共享一列或一行的一块石头。
我们最多能执行多少次 move 操作？

示例 1：
输入：
stones = 
[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5

示例 2：
输入：
stones = 
[[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：
3

示例 3：
输入：stones = [[0,0]]
输出：0
提示：
1 <= stones.length <= 1000
0 <= stones[i][j] < 10000

画图分析
所有能横纵坐标连成线的,最后都可以消除到剩下一个元素
"""


class Solution(object):
    def removeStones(self, stones):
        """
        暴力 时间复杂度O(n^2)
        合并点的区间 写的太乱了
        用的bfs
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        move = 0
        r = [set() for _ in range(n)]
        for i in range(n):
            x1, y1 = stones[i]
            for j in range(n):
                x2, y2 = stones[j]
                if i != j and x1 == x2 or y1 == y2:
                    r[i].add(j)
        res = []
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            queue = r[i]
            t = set()
            while queue:
                cur = queue.pop()
                t.add(cur)
                if cur not in visited:
                    visited.add(cur)
                    queue |= r[cur]
            res.append(t)
        return n - len(res)
        # 下面的代码不对
        # for i in range(1, n):
        #     x1, y1 = stones[i]
        #     for j in range(i):
        #         x2, y2 = stones[j]
        #         if x1 == x2 or y1 == y2:
        #             move += 1

    def removeStones2(self, stones):
        """
        并查集
        :param stones:
        :return:
        """
        from collections import defaultdict
        stones = list(map(tuple, stones))
        graph = {x: x for x in stones}

        def find(g, x):
            while g[x] != x:
                g[x] = g[g[x]]
                x = g[x]
            return (x)

        for i in range(len(stones) - 1):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    if find(graph, stones[i]) != find(graph, stones[j]):
                        graph[find(graph, stones[i])] = find(graph, stones[j])
        con_comp = defaultdict(int)

        for x in stones:
            con_comp[find(graph, x)] += 1
        return (sum([i - 1 for i in con_comp.values()]))


stones = [[0, 0], [0, 2], [1, 1], [1, 5], [2, 0], [2, 2]]
s = Solution()
print(s.removeStones2(stones))
