# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32 
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内。

264_丑数2，升级版，多指针
"""


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        uglys = [1]
        idxs = [0] * k  #k指针列表
        for i in range(n - 1):
            next_ugly = min(uglys[idxs[j]] * primes[j] for j in range(k))
            uglys.append(next_ugly)
            for j in range(k):
                if uglys[idxs[j]] * primes[j] == next_ugly:
                    idxs[j] += 1
        #     print(uglys,idxs)
        # print(uglys,idxs)
        return uglys[-1]


n = 12
primes = [2, 7, 13, 19]
s = Solution()
print(s.nthSuperUglyNumber(n, primes))
