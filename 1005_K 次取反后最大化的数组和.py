# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组 A，我们只能用以下方法修改该数组：
我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。

 

示例 1：

输入：A = [4,2,3], K = 1
输出：5
解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
示例 2：

输入：A = [3,-1,0,2], K = 3
输出：6
解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
示例 3：

输入：A = [2,-3,-1,5,-4], K = 2
输出：13
解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
"""


class Solution:
    def largestSumAfterKNegations(self, A, K):
        A1 = sorted(list(filter(lambda x:x<0,A)))
        A2 = sorted(list(filter(lambda x:x>=0,A)))
        # print(A1,A2)
        # K的长度大于负数个数的情况
        if K>=len(A1):
            # 负数全部取反
            A1 = [-x for x in A1]
            t = K-len(A1)
            if t%2!=0:
                if A1 and A1[-1]<A2[0]:
                    A1[-1] = -A1[-1]
                else:
                    A2[0] = -A2[0]
        else:
            # 最小的K个数取反
            A1[:K] = [-x for x in A1[:K]]
        # print(A1, A2)
        return sum(A1+A2)



A = [-8,3,-5,-3,-5,-2]
K = 6
s = Solution()
print(s.largestSumAfterKNegations(A,K))