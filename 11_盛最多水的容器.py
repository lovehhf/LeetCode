# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。



示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_s = 0  # 记录最大面积
        l = 0
        r = n-1
        while(l<r):
            # 比较上一个记录和当前面积的大小
            max_s =max(max_s, min(height[l],height[r])*(r-l))
            # 比较左指针和右指针指向的数 值小的向内移动
            # 因为面积取决于指针的距离与值小的值乘积
            # 如果值大的值向内移动，距离一定减小，而求面积的另外一个乘数一定小于等于值小的值，因此面积一定减小

            # 只有值小的指针向内移动 才有可能凑出比原来的面积更大的矩形
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return max_s

    def maxArea2(self, height):
        """
        暴力法 超时
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_s = 0
        for i in range(n-1):
            for j in range(i+1,n):
                s = (j-i)*min(height[i],height[j])
                if s>max_s:
                    max_s = s
        return max_s

height = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(height))