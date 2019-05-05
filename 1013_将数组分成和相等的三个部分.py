# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
示例 1：

输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
"""


class Solution:
    def canThreePartsEqualSum(self, A):
        s = sum(A)
        if s % 3 != 0:
            return False
        s /= 3
        targets = [2 * s, s]
        acc = 0
        for a in A:
            acc += a
            if acc == targets[-1]:
                targets.pop()
            if not targets:
                return True
        return False

    def canThreePartsEqualSum2(self, A):
        sumA = sum(A)
        if sumA%3!=0:
            return False
        s = sumA//3
        acc = 0
        find_i,find_j = 0,0

        for i in range(len(A)):
            acc += A[i]
            if acc == s:
                find_i = i+1 # +1避免i=0的情况
                print(find_i)
            if acc == 2*s:
                find_j = i+1
                print(find_j)
            if find_i and find_j and find_j>find_i:
                return True
        return False

    def canThreePartsEqualSum3(self, A):
        """
        3等份的和一定是 sum(A)/3
        :param A:
        :return:
        """
        n = len(A)
        sumA = sum(A)
        if sumA%3!=0:
            return False
        i,j = 0,n-1
        # 时间爆炸 待优化
        while i+1<j:
            if sum(A[:i + 1]) == sumA // 3 and sum(A[j:]) == sumA // 3:
                return True
            elif sum(A[:i + 1]) == sumA // 3:
                j -= 1
            elif sum(A[j:]) == sumA // 3:
                i += 1
            else:
                i += 1
        return False

    def canThreePartsEqualSum4(self, A):
        """
        时间爆炸 待优化
        :param A:
        :return:
        """
        n = len(A)
        for i in range(0,n-1):
            for j in range(i+2,n):
                # print(A[:i+1],A[i+1:j],A[j:])
                left = sum(A[:i+1])
                mid = sum(A[i+1:j])
                right = sum(A[j:])
                if left == mid and mid==right:
                    return True
        return False


A = [12,-4,16,-5,9,-3,3,8,0]
s = Solution()
print(s.canThreePartsEqualSum(A))