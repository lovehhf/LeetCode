# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
示例 1:

输入: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:

输入: 
gas  = [2,3,4]
cost = [3,4,3]

输出: -1

解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。


什么时候能开到下一个加油站: 
    油箱的油 >= 到下一站消耗的油
    油箱的油: 上一站剩下的油 + 这一站加的油
    到下一站消耗的油: cost[i]
    
性质： 
如果以A为起点, 刚好到点B无法开到B的下一个节点, 那么A~B中的任一起点都不可能作为起点

反证： 
  假设 A到B 之间存在点C可以作为起点
  那么从C到B的下一个点(B+1)剩下的油>=0
  A到C 剩下的油肯定要>=0 (A到B途中有途不能<0, 否则就走不到B了)
  A到B+1 剩下的油肯定也会>=0
  与A为起点到不了B+1矛盾  
所以 如果以A为起点, 刚好到点B无法开到B的下一个节点, 那么A~B中的任一起点都不可能作为起点
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            # g 表示剩余油量
            g = gas[i]
            for j in range(i, i + n):
                # 模拟开车和加油
                g -= cost[j % n]
                # 中间油量不够开到下一站, gg
                if g < 0:
                    i = j + 1
                    break
                g += gas[(j + 1) % n]
            # 正常结束for循环 表示能循环走一圈, 返回 i
            else:
                return i
        return -1

    # def canCompleteCircuit2(self, gas, cost):
    #     """
    #     暴力解法,超时
    #     :type gas: List[int]
    #     :type cost: List[int]
    #     :rtype: int
    #     """
    #     n = len(gas)
    #     for i in range(n):
    #         s = gas[i]  # 初始油量
    #         flag = True
    #         for j in range(i, i + n + 1):
    #             index = j % n
    #             s = s - cost[index]  # 到下一站还剩的油量
    #             # print(i, gas[index], cost[index], s)
    #             if s < 0:
    #                 flag = False
    #                 break
    #             s += gas[(index + 1) % n]  # 成功到达下一站,加油
    #             # print(i, gas[index], cost[index], s)
    #         if flag:
    #             return i
    #     return -1


s = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print(s.canCompleteCircuit3(gas, cost))
