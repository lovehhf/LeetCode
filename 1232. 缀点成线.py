# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回true，否则请返回false。

示例 1：
输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true
示例 2：

输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false

提示：

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates 中不含重复的点

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        求斜率公式相乘
        (y1-y0)/(x1-x0)=(yi-y0)/(xi-x0)
        防止除0，变换成相乘的形式
        (y1-y0)*(xi-x0)==(x1-x0)*(yi-y0)
        :param coordinates:
        :return:
        """

        n = len(coordinates)
        for i in range(1, n-1):
            a,b,c = coordinates[i-1], coordinates[i], coordinates[i+1]
            if (b[1] - a[1])*(c[0] - b[0]) != (b[0] - a[0])*(c[1] - b[1]):
                return False
        return True