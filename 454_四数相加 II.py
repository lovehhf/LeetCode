# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        分别合并A+B的所有制和C+D的所有值
        在用字典存储,AB中出现的次数,遍历CD,看target-CD[i]是否在字典中
        时间复杂度O(n^2)
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = [x + y for x in A for y in B]
        CD = [x + y for x in C for y in D]
        # res = [x + y for x in AB for y in CD].count(0)
        res = 0
        d = {}
        for i in AB:
            d[i]=d.get(i,0) + 1
        for i in CD:
            if -i in d:
                res += d[-i]
        return res


A = [-1, -1]
B = [-1, 1]
C = [-1, 1]
D = [1, -1]

s = Solution()
print(s.fourSumCount(A, B, C, D))
