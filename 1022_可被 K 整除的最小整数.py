# -*- coding:utf-8 -*-

__author__ = 'huanghf'

'''
给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。
返回 N 的长度。如果不存在这样的 N，就返回 -1。
 

示例 1：

输入：1
输出：1
解释：最小的答案是 N = 1，其长度为 1。
示例 2：

输入：2
输出：-1
解释：不存在可被 2 整除的正整数 N 。
示例 3：

输入：3
输出：3
解释：最小的答案是 N = 111，其长度为 3。
1+10+100+1000+10000+...


Assume that N = 1 to N = K, if there isn't 111...11 % K == 0
There are at most K - 1 different remainders: 1, 2, .... K - 1.

So this is a pigeon holes problem:
There must be at least 2 same remainders.

Assume that,
f(N) ≡ f(M), N > M
f(N - M) * 10 ^ M ≡ 0
10 ^ M ≡ 0, mod K
so that K has factor 2 or factor 5.

Proof by contradiction，
If (K % 2 == 0 || K % 5 == 0) return -1;
otherwise, there must be a solution N <= K.

Time Complexity:
Time O(K), Space O(1)

https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/260852/JavaC%2B%2BPython-O(1)-Space-with-Proves-of-Pigeon-Holes
https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/260875/Python-O(K)-with-Detailed-Explanations
'''


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        """
        偶数或者被5整除直接返回-1

        :param K:
        :return:
        """

        if K%2==0 or K%5==0:
            return -1
        res = 0
        for N in range(1,K+1):
            res = (res*10+1)%K
            if res==0:
                return N
        return -1

s = Solution()
print(s.smallestRepunitDivByK(557))