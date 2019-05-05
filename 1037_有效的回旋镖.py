# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。

给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。

示例 1：

输入：[[1,1],[2,3],[3,2]]
输出：true
示例 2：

输入：[[1,1],[2,2],[3,3]]
输出：false
 

提示：

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
"""


class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # 判断有重复点
        points = [tuple(x) for x in points]
        if len(set(points)) < len(points):
            return False

        if points[0][0] == points[1][0] and points[1][0] == points[2][0]:
            return False
        if points[0][0] == points[1][0] or points[1][0] == points[2][0]:
            return True
        k1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        k2 = (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])
        if abs(k1 - k2) > 1e-6:
            return True
        return False


points = [[0,1],[2,0],[1,1]]
s = Solution()
print(s.isBoomerang(points))
