# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。

1:
0 1
2:
00 01 11 10 = 0[0 1] + 1[1 0]
3:
000,001,011,010,110,111,110,100 = 0[00 01 11 10] + 1[10 11 01 00]
f(n) = ['0'+x for x in f(n-1)] + ['1'+x for x in reversed(n-1)]
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        res = [['0','1']]
        for i in range(1,n):
            res_i = ['0'+x for x in res[i-1]] + ['1'+x for x in reversed(res[i-1])]
            res.append(res_i)

        # print(res)
        return list(map(lambda x:int(x,2),res[-1]))

if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(2))