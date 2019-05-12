# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。
paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。
另外，没有花园有 3 条以上的路径可以进入或者离开。
你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用1, 2, 3, 4表示。保证存在答案。
示例 1：

输入：N = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]
示例 2：

输入：N = 4, paths = [[1,2],[3,4]]
输出：[1,2,1,2]
示例 3：

输入：N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
输出：[1,2,3,4]


花的种只有1, 2, 3, 4,
G[i]表示与i相邻的花园有哪些
"""


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * N
        G = [[] for _ in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res

N = 6
paths = [[1,2],[3,4],[5,6]]
s = Solution()
print(s.gardenNoAdj(N, paths))