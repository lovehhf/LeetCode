# -*- coding:utf-8 -*-

"""
447. 回旋镖的数量
https://leetcode-cn.com/problems/number-of-boomerangs/

给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:
输入:
[[0,0],[1,0],[2,0]]
输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
"""

import collections


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        哈希 + 组合数
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(points)
        for i in range(n):
            # 以 i 为 基点, 统计其他点到 i 的距离
            ht = collections.defaultdict(int)
            for j in range(n):
                if j == i:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dis = dx * dx + dy * dy
                ht[dis] += 1

            # 对所有的距离的值求组合数 C(n, 2) * 2,
            res += sum([v * (v - 1) for v in ht.values() if v >= 2])
        return res
