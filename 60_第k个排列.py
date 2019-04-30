# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"->1
"132"->2
"213"->3
"231"->4
"312"->5
"321"->6

给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

1234 -> 2314

想法1：计算出(1,n)的所有全排列，再选取第K个（超时）

想法2：既然所有的全排列是从小到大，那么可以对每一位的数字进行定位。
例如，
假如给定题目为（5,46）。固定第一位数，后面4位的全排列数为24，math.ceil(46/24)=2,即处于第1位数的第二个循环中，即第一位数为2.
同理，对于固定第二位数，math.ceil(（46-24）/6)=4,即处于第2位数的第四个循环中（此时列表移除了已确定的数字2），即第2位数为5.
同理，可依次推理出最后结果为“25341”.总时间复杂度为O（n）.


"""

import math

class Solution(object):
    def getPermutation(self, n: int, k: int) -> str:
        l = list(range(1, n + 1))
        res = []
        while l:
            a = math.factorial(len(l) - 1)
            tmp = math.ceil(k / a) - 1
            value = l[tmp]
            res.append(value)
            l.remove(value)
            k = k - tmp * a
        res = list(map(str, res + l))
        return ''.join(res)

    def recursive(self, nums, k):
        l = len(nums)
        if l == 1:
            return str(nums[0])
        temp = math.factorial(l - 1)
        idx = (k - 1) // temp
        offset = (k - 1) % temp + 1
        first = str(nums.pop(idx))
        return first + self.recursive(nums, offset)

    def getPermutation3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.recursive(list(range(1, n + 1)), k)


    def getPermutation2(self, n: int, k: int) -> str:
        """
        超时
        生成全排列
        :param n:
        :param k:
        :return:
        """
        from itertools import permutations
        res = sorted(permutations(list(range(1,n+1))))
        print(res)
        return ''.join([str(x) for x in res[k-1]])

n = 9
k = 353955
s = Solution()
print(s.getPermutation(n,k))