# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在一排多米诺骨牌中，A[i] 和 B[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 该平铺的每一半上都有一个数字。）
我们可以旋转第 i 张多米诺，使得 A[i] 和 B[i] 的值交换。
返回**能使 A 中所有值或者 B 中**所有值都相同**的最小旋转次数**。
如果无法做到，返回 -1.

示例 1：
输入：A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
输出：2
解释：
图一表示：在我们旋转之前， A 和 B 给出的多米诺牌。
如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。
示例 2：

输入：A = [3,5,1,2,3], B = [3,6,3,3,4]
输出：-1
解释：
在这种情况下，不可能旋转多米诺牌使一行的值相等。
"""


class Solution:
    def minDominoRotations(self, A, B):
        n = len(A)
        for x in range(1,7):
            ca,cb = 0,0
            for i in range(n):
                print(A[i],B[i])
                if A[i]!=x and B[i]!=x:
                    break

            else:
                for i in range(n):
                    if A[i]!=x:
                        ca += 1
                    if B[i]!=x:
                        cb += 1
                return min(ca,cb)
        return -1

    def minDominoRotations2(self, A, B):
        for x in range(1, 7):
            # all: 列表或元组所有都为True 才为True
            # any: 列表或元组任一True 为True
            if all([x == a or x == b for a, b in zip(A, B)]):
                return min(len(A) - A.count(x), len(B) - B.count(x))
        return -1
A = [3,5,1,2,3]
B = [3,6,3,3,4]
s = Solution()
print(s.minDominoRotations2(A,B))