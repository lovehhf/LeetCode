# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出数字 N，返回由若干 "0" 和 "1"组成的字符串，该字符串为 N 的负二进制（base -2）表示。

除非字符串就是 "0"，否则返回的字符串中不能含有前导零。

 

示例 1：

输入：2
输出："110"
解释：(-2) ^ 2 + (-2) ^ 1 = 2
示例 2：

输入：3
输出："111"
解释：(-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
示例 3：

输入：4
输出："100"
解释：(-2) ^ 2 = 4

for each number, we first consider its binary mode, then we check 10,1000,100000,... one by one
for example, 6 = '110', so for the second '1', in base -2, it makes the initial number decrease 4(+2 -> -2)
so we jusr make the initial number add 4, then 6 -> 10 = '1010', later we consider the first '1', it makes the initial number decrease 16(+8 -> -8), then we add 16, 10 -> 26 = '11010', now we get the answer.

https://leetcode.com/problems/convert-to-base-2/discuss/265507/JavaC%2B%2BPython-2-lines-Exactly-Same-as-Base-2
https://leetcode.com/problems/convert-to-base-2/discuss/265688/4-line-python-clear-solution-with-explanation
"""


class Solution(object):
    def baseNeg2(self, N):
        """
        1 = 1
        2 = 4-2 = 110
        3 = 4-2+1 = 111

        :type N: int
        :rtype: str
        """
        neg = [1 << i for i in range(1, 33, 2)]
        for mask in neg:
            if N & mask:
                N += mask*2
        return bin(N)[2:]


N = 4
s = Solution()
print(s.baseNeg2(N))