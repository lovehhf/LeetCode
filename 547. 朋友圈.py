# -*- coding:utf-8 -*-

"""
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。


示例 1:
输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。

示例 2:
输入:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。

注意：
N 在[1,200]的范围内。
对于所有学生，有M[i][i] = 1。
如果有M[i][j] = 1，则有M[j][i] = 1。

并查集求联通分量
"""

from typing import List


class UnionFind:
    def __init__(self, n):
        # 初始化, 每个节点都是自己的祖先节点
        self.father = [i for i in range(n)]

    def find(self, x):
        """
        查找 x 的祖先节点
        """
        if (self.father[x] == x):
            return x
        self.father[x] = self.find(self.father[x])  # 路径压缩, 查找的过程中的所有节点的祖先节点都指向
        return self.father[x]

    def union(self, a, b):
        """
        合并 a 和 b 所在的集合, a 的祖先节点指向 b 的祖先节点
        """
        fa = self.find(a)
        fb = self.find(b)
        self.father[fa] = fb


class UnionFind_Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    uf.union(i, j)

        # 并查集有多少个不同的集合, 等价于有多少个祖先节点指向自己的节点
        res = sum([x == uf.father[x] for x in range(n)])
        return res

class DFS_Solution:

    def dfs(self, i, M, visited):
        if visited[i]:
            return
        visited[i] = 1
        for j in range(len(M)):
            if not visited[j] and M[i][j] & 1:
                self.dfs(j, M, visited)

    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0] * n
        res = 0
        for i in range(n):
            if visited[i] & 1:
                continue
            # 无向图, 通过任何一个节点都可以 dfs 搜索到所有的连通节点
            self.dfs(i, M, visited)
            res += 1
        return res


s = UnionFind_Solution()
M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(s.findCircleNum(M))
