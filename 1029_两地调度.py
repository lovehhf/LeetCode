# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。

 

示例：

输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
 

提示：
1 <= costs.length <= 100
costs.length 为偶数
1 <= costs[i][0], costs[i][1] <= 1000
"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        costs = sorted(costs,key=lambda x:abs(x[0]-x[1]),reverse=True) # 按差价从大到小排序
        A = []
        B = []

        for i in range(n//2):
            if costs[i][0]<costs[i][1]:
                A.append(costs[i][0])
            else:
                B.append(costs[i][1])

        for i in range(n//2,n):
            if costs[i][0]<costs[i][1]:
                if len(A)<n//2:
                    A.append(costs[i][0])
                else:
                    B.append(costs[i][1])
            else:
                if len(B)<n//2:
                    B.append(costs[i][1])
                else:
                    A.append(costs[i][0])
        # print(costs)
        # print(A,B)
        return sum(A)+sum(B)

s = Solution()
costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
print(s.twoCitySchedCost(costs))