# -*- coding:utf-8 -*-

"""
现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:
输入: 2, [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

示例 2:
输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

说明:
输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。

提示:
这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。


输出拓扑序列
思路:
bfs
1. 所有入度为 0 的点进队列
2. 队列中的点的出边的 入度 -1, 减到 0 再进队列, 如果减不到 0 说明有环
"""

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        res = []
        courses = [[] for _ in range(n)]
        indegrees = [0] * n  # 每个点的入度,  从入度为 0 的点开始遍历

        for a, b in prerequisites:
            courses[b].append(a)  # 存储图, courses[i] 表示 i 指向的点
            indegrees[a] += 1  # 入度 + 1

        queue = [i for i in range(n) if indegrees[i] == 0]

        while queue:
            cur = queue.pop(0)
            res.append(cur)
            for ne in courses[cur]:
                indegrees[ne] -= 1
                if indegrees[ne] == 0:
                    queue.append(ne)  # 减完之后入度为 0 才进下一轮的队列

        return res if len(res) == n else []

