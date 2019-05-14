# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        使用一个栈存储需要删除的元素的索引
        insert_index存储插入元素的索引
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        n = len(intervals)
        pop_stack = []
        insert_index = 0
        for i in range(n):
            if (intervals[i][1] >= newInterval[0] and newInterval[1] >= intervals[i][0]):
                pop_stack.append(i)
            if i > 0 and intervals[i][0] >= newInterval[0] and intervals[i - 1][0] < newInterval[0]:
                insert_index = i
        if intervals[-1][0] < newInterval[0]:
            insert_index = n
        # print(pop_stack)
        # print(insert_index)
        if pop_stack:
            insert_index = pop_stack[0]
            newInterval = [min(intervals[pop_stack[0]][0], newInterval[0]),
                           max(intervals[pop_stack[-1]][1], newInterval[1])]
        while pop_stack:
            intervals.pop(pop_stack.pop())
        intervals.insert(insert_index, newInterval)
        return intervals


intervals = [[1, 15]]
newInterval = [13, 18]
s = Solution()
print(s.insert(intervals, newInterval))
