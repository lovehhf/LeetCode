# -*- coding:utf-8 -*-

"""
在本问题中, 树指的是一个连通且无环的无向图。
输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

示例 1：
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3

示例 2：
输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
注意:
输入的二维数组大小在 3 到 1000。
二维数组中的整数在1到N之间，其中N是输入数组的大小。

并查集
出现环的条件是某条边，边的两个端点原本就是连通的，那么加上了这条边以后就产生了环，
因此我们在加入每条边的时候需要判断一下边的两个端点本身是不是连通的即可。
"""

from typing import List

class Solution:
    def __init__(self):
        self.father = []

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)

        ret = fa == fb  # a 和 b 是否是原来就是连通的

        self.father[fa] = fb
        return ret

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        for i in range(n + 1):
            self.father.append(i)

        for a, b in edges:
            if self.union(a, b):
                return [a, b]

s = Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(s.findRedundantConnection(edges))