# -*- coding:utf-8 -*-

"""
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""

from typing import List

from collections import defaultdict


class Solution:
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n

        res = 0
        for i in range(n):
            d = defaultdict(int)
            x1, y1 = points[i]
            t = 0
            for j in range(n):
                x2, y2 = points[j]
                if (x1, y1) == (x2, y2):
                    t += 1
                    continue
                if x1 == x2:
                    d[(0, 0)] += 1
                    continue
                g = self.gcd(y1 - y2, x1 - x2)
                k = ((y1 - y2) / g, (x1 - x2) / g)
                d[k] += 1
            res = max(res, max(d.values()) + t) if d else t

        return res
