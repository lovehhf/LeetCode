# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。
如果满足以下条件，则称子数组(P, Q)为等差数组：
元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。
函数要返回数组 A 中所有为等差数组的子数组个数。

示例:

A = [1, 2, 3, 4]
返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        dp[i] 表示比A[:i]到A[:i+1]新增加的等差数列子数组个数
        拿[1,2,3,4]来说 1,2,3是等差数列，所有dp[2]=1,2,3,4相比于1,2,3来说增加了[2,3,4],[1,2,3,4]两个等差数列
        对于[1,2,3,4,5],dp[4]新增加了[2,3,4,5],[3,4,5],[1,2,3,4,5],所以dp[5]=dp[4]+1=5
        对于[1,2,3,4,5,7] 由于在7这里中断了前面等差数列,没有增加子等差数组,后面又就需要重新计数了
        对于整个序列A,最后结果的就是sum(dp)
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [0 for _ in range(n)]
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)

    def numberOfArithmeticSlices2(self, A):
        """
        优化空间复杂度
        dp[i]只跟dp[i-1]有关,可以使用变量代替dp
        :param A:
        :return:
        """
        n = len(A)
        res,tmp = 0,0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                tmp = tmp + 1
                res += tmp
            else:
                tmp  = 0
        return res


A = [1, 2, 3, 4, 5, 4, 3]
s = Solution()
print(s.numberOfArithmeticSlices2(A))
