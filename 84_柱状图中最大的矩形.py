# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        使用单调栈,栈内只存储递增序列的索引
        遍历 heights
        1.栈顶元素>heights[i]的时候,不断弹出栈顶,计算以这个栈顶为高的矩形有多大
        2.使用for循环不管是height[i]与栈顶元素孰大孰小都要append[i]
        3.矩形宽为什么是i-stack[-1]-1 if stack else i呢
          - 如果stack为空说明弹出的元素是最小的0~i最小的了,此时矩形的宽就是i
          - 如果stack不为空,说明此时的栈顶元素是左边第一个比弹出元素小的数,i-(stack[-1]+1)就是矩形的宽
          - 为什么宽不是i-j而是i-stack[-1]-1 例: [0, 3, 2, 5,0],遍历到最后0的时候栈内元素有[0,2,5],i-j没有考虑到index为1的元素也就是3
        :param heights:
        :return:
        """
        heights.append(0)  # 最后添加一个0保证一定会计算,不需要再次处理遗留的stack
        stack = []
        res = 0
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                res = max(res, (i - j if stack else i) * heights[j])
            stack.append(i)
        return res

    def largestRectangleArea2(self, heights):
        """
        暴力解法 超时
        遍历每个元素,再往左右扩散遍历一遍寻找左边界和右边界
        时间复杂度O(n^2)
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        res = 0
        for i in range(n):
            j, k = i - 1, i + 1
            while j >= 0 and heights[j] >= heights[i]:
                j -= 1
            while k < n and heights[k] >= heights[i]:
                k += 1
            res = max(res, heights[i] * (k - j - 1))
        return res


heights = [0, 3, 2, 5]
s = Solution()
print(s.largestRectangleArea(heights))
