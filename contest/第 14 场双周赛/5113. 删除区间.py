# -*- coding:utf-8 -*-

"""
给你一个 有序的 不相交区间列表 intervals 和一个要删除的区间 toBeRemoved， intervals 中的每一个区间 intervals[i] = [a, b] 都表示满足 a <= x < b 的所有实数  x 的集合。

我们将 intervals 中任意区间与 toBeRemoved 有交集的部分都删除。

返回删除所有交集区间后， intervals 剩余部分的 有序 列表。



示例 1：

输入：intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
输出：[[0,1],[6,7]]
示例 2：

输入：intervals = [[0,5]], toBeRemoved = [2,3]
输出：[[0,2],[3,5]]


提示：

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
"""

from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        x2, y2 = toBeRemoved
        for i in range(n):
            x1, y1 = intervals[i]
            if (y1 <= x2 or y2 <= x1):
                res.append([x1, y1])
            elif (x2 > x1):
                if(y1 <= y2):
                    res.append([x1, x2])
                else:
                    res.append([x1, x2])
                    res.append([y2, y1])
            else:
                if(y1 > y2):
                    res.append([y2, y1])
        return res

intervals = [[0,2],[3,4],[5,7]]
toBeRemoved = [1,6]
s = Solution()
print(s.removeInterval(intervals, toBeRemoved))