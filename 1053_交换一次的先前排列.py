# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给你一个正整数的数组 A（其中的元素不一定完全不同），
请你返回可在 一次交换（交换两数字 A[i] 和 A[j] 的位置）后得到的、按字典序排列小于 A 的最大可能排列。
如果无法这么操作，就请返回原数组。
示例 1：

输入：[3,2,1]
输出：[3,1,2]
解释：
交换 2 和 1
 
示例 2：

输入：[1,1,5]
输出：[1,1,5]
解释： 
这已经是最小排列
 

示例 3：

输入：[1,9,4,6,7]
输出：[1,7,4,6,9]
解释：
交换 9 和 7
 

示例 4：

输入：[3,1,1,3]
输出：[1,1,3,3]
 

提示：

1 <= A.length <= 10000
1 <= A[i] <= 10000

[1,6,9,4,6,7]
1 6 7 4 6 9

1 2 5 3 2 4 -> 1 2 5 2 3 4
 
5 4 3 2 1 -> 5 4 3 1 2 


最后一个比它右边的值大的数字就是左边需要交换的数字
使用单调栈存储正常排列的数字索引
"""


class Solution(object):
    def prevPermOpt1(self, A):
        """
        只能进行一次交换
        交换后的构成的数组的元素字典序要小于A
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        stack = []
        L = -1
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                L = max(L, stack.pop())
            stack.append(i)
        if L == -1:
            return A
        while A[stack[-1]] >= A[L]:
            stack.pop()
        R = stack[-1]
        A[L], A[R] = A[R], A[L]
        return A

        # B = sorted(A)
        # if B == A:
        #     return A
        # 下面代码有错 [3,2,1] -> [3,1,2]
        # i = 0
        # while A[i] == B[i]:
        #     i += 1
        # t, k = A[i + 1], i + 1  # 存储需要交换的值和索引
        # for j in range(i + 2, n):
        #     if A[j] < A[i] and A[j] > t:
        #         t,k = A[j],j
        # A[i], A[k] = A[k], A[i]
        # return A


s = Solution()
A = [3, 1, 1, 3]
print(s.prevPermOpt1(A))
