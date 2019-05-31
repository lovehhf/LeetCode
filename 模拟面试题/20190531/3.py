# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6


"""

import collections


class Solution(object):
    def maxPoints(self, points):
        """
        斜率float不适合作为字典键，有精度损失,使用(y2-y1),(x2-x1)的除最大公约数的tuple作为键
        使用欧几里得算法求最大公约数
        :type points: List[List[int]]
        :rtype: int
        """

        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        if not points:
            return 0
        points.sort()
        n = len(points)
        res = 0
        for i in range(n):
            d = collections.defaultdict(int)
            cover = 0
            t_max = 0
            for j in range(i+1,n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0 and y == 0: # 2个点重合
                    cover += 1
                    continue
                g = gcd(x, y)
                dx, dy = (x // g, y // g) if g else (x, y)
                d[(dx, dy)] += 1
                t_max = max(t_max, d[(dx, dy)])
            res = max(res, t_max+cover+1)
        return res


points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
s = Solution()
print(s.maxPoints(points))
