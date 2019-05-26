# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

示例 1：

输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]
示例 2：

输入：[1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]

提示：

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""

import collections


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        n = len(barcodes)
        res = [0] * n
        count = collections.Counter(barcodes)
        d = sorted([v, k] for k, v in count.items())[::-1]
        i = 0
        for v, k in d:
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n:
                    i = 1
        return res

        # d = {}
        # for i in barcodes:
        #     d[i] = d.get(i, 0) + 1
        # d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        # n = len(barcodes)
        # res = [0] * n
        # visit = list(range(n))
        # print(d)
        # for i in range(len(d)):
        #     k, v = d[i]
        #     j = visit[0]
        #     while v > 0:
        #         print(j, k, res, visit)
        #         res[j] = k
        #         visit.remove(j)
        #         j += 2
        #         v -= 1
        # return res


s = Solution()
barcodes = [1, 1, 1, 2, 2, 2, 3, 3]
print(s.rearrangeBarcodes(barcodes))
