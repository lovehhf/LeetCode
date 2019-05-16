# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。

Rectangle Area

示例:

输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45
说明: 假设矩形面积不会超出 int 的范围。
"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        (-3,0),(3,0),(3,4),(-3,4)
        (0,-1),(9,-1),(9,2),(0,2)
        (-3,3)(0,9)->(0,3) 宽:(C和G中的小值-A和E的大值)
        (-1,2)(0,4)->(0,2) 高:(D和H的小值-B和F的大值)
        """
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)
        h = min(D, H) - max(B, F)
        l = min(C, G) - max(A, E)
        s3 = h * l if h > 0 and l > 0 else 0
        return s1 + s2 - s3


s = Solution()
print(s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
