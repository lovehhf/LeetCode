# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
"""


class Solution(object):
    def candy(self, ratings):
        """
        和字节跳动2019春招第一轮笔试第三题基本一样
        还是要多刷leetcode 要是笔试做过这个就不拿到题的时候一脸懵逼了Orz

        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        res = [1] * n
        min_index = ratings.index(min(ratings))  # 最小分数的索引
        # 最小值右区间从左往右处理
        for i in range(min_index + 1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
            else:
                j = i
                while ratings[j] < ratings[j - 1]:
                    res[j - 1] = max(res[j - 1], res[j] + 1)
                    j -= 1

        # 最小值左区间开始从右往前处理
        for i in range(min_index - 1, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = res[i + 1] + 1
            else:
                j = i
                while ratings[j + 1] > ratings[j]:
                    res[j + 1] = max(res[j + 1], res[j] + 1)
                    j += 1
        return sum(res)

    def candy3(self, ratings):
        """
        先给每个人一个糖，初始化tmp数组为额外糖果。
        从左向右遍历，如果i+1分数高，tmp[i+1]=tmp[i]+1。
        再从后往前遍历，如果i比i+1分数高，那么比较tmp[i]和tmp[i+1]+1，如果tmp[i]小，更新。
        假如分数i-1<i，那么下一次继续检查，如果分数i-1>i，因为第一次tmp[i]>tmp[i-1]，从右往左更新tmp[i]只可能增加，依然满足大小关系
        :type ratings: List[int]
        :rtype: int
        """
        s = 0
        n = len(ratings)
        s += n
        tmp = [0] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                tmp[i] = tmp[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                tmp[i] = max(tmp[i], tmp[i + 1] + 1)
        s += sum(tmp)
        return s


ratings = []
s = Solution()
print(s.candy([3, 1, 1, 0]))
