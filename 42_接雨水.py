# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


class Solution(object):
    def trap(self, height):
        """
        left_max[i] 表示i左边的最大值
        right_max[i] 表示i右边的最大值
        第i格能装的水为lefi_max[i]和right_max[i]中的最小值-height[i]
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        area = [0] * n
        for i in range(n):
            area[i] = min(left_max[i], right_max[i]) - height[i]
        # print(area)
        return sum(area)


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
print(s.trap(height))
