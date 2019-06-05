# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        time = [x % 60 for x in time]
        t = [0] * 61
        n = len(time)
        for i in range(n):
            t[-1] += t[(60 - time[i]) % 60]
            t[time[i]] += 1
        return t[-1]


time = [1, 59, 60]
s = Solution()
print(s.numPairsDivisibleBy60(time))
