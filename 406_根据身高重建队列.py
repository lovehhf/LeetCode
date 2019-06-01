# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 
编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

按照身高降序,k升序排序
K值定义为 排在h前面且身高大于或等于h的人数 
因为从身高降序开始插入，此时所有人身高都大于等于h
因此K值即为需要插入的位置
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
排序后: [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
一次插入到新的数组中:
[5, 0],[7, 0], [5, 2],[6, 1],[4, 4], [7, 1]
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        按照身高降序,k升序排序
        按照k的定义依次插入到新的数组中
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x:(-x[0],x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res



people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
s = Solution()
print(s.reconstructQueue(people))