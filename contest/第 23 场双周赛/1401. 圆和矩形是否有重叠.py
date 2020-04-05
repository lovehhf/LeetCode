# -*- coding:utf-8 -*-

"""
给你一个以 (radius, x_center, y_center) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2)，其中 (x1, y1) 是矩形左下角的坐标，(x2, y2) 是右上角的坐标。
如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。
换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。

示例 1：
输入：radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
输出：true
解释：圆和矩形有公共点 (1,0)

示例 2：
输入：radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
输出：true

示例 3：
输入：radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
输出：true

示例 4：
输入：radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
输出：false

提示：
1 <= radius <= 2000
-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
x1 < x2
y1 < y2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/circle-and-rectangle-overlapping
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


将矩形分为9个区域，判定圆心的位置在哪个区域：
1. 如果圆心在矩形的内部，则一定相交；
2. 如果圆心位于矩形的上下左右四个区域当中，检测圆心到边的距离，判定是否相交；
3. 如果圆心位于四个角对应的区域，只要检测矩形的四个顶点是否在圆的内部即可。
"""


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # 1. 圆心在矩形内
        if (x1 <= x_center <= x2 and y1 <= y_center <= y2):
            return True

        # 2. 矩形的某个角在圆心内
        for x in (x1, x2):
            for y in (y1, y2):
                if (x - x_center) * (x - x_center) + (y - y_center) * (y - y_center) <= radius * radius:
                    return True

        # 3. 圆与矩形的某一条线相交 (圆心到线的距离)
        if (x1 <= x_center <= x2 and (abs(y_center - y1) <= radius or abs(y_center - y2) <= radius)):
            return True
        if (y1 <= y_center <= y2 and (abs(x_center - x1) <= radius or abs(x_center - x2) <= radius)):
            return True

        return False
