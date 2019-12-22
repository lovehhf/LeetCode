# -*- coding:utf-8 -*-

"""
我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。

请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。

 

示例 1：

输出：low = 100, high = 300
输出：[123,234]
示例 2：

输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]
 

提示：

10 <= low <= high <= 10^9
"""


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        for i in range(2, 10):
            j = 1
            k = j + i
            while (k <= 10):
                num = int(''.join([str(x) for x in range(j, k)]))
                if (low <= num <= high):
                    res.append(num)
                j += 1
                k += 1

        return res
