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


【笔记】一次遍历法，车能开完全程需要满足两个条件：

车从i站能开到i+1。所有站里的油总量要>=车子的总耗油量。
那么，假设从编号为0站开始，一直到k站都正常，在开往k+1站时车子没油了。这时，应该将起点设置为k+1站。

问题1: 为什么应该将起始站点设为k+1？
因为k->k+1站耗油太大，0->k站剩余油量都是不为负的，每减少一站，就少了一些剩余油量。
所以**如果从k前面的站点作为起始站，剩余油量不可能冲过k+1站**, 

问题2: 为什么如果k+1->end全部可以正常通行，且rest>=0就可以说明车子从k+1站点出发可以开完全程？

因为，起始点将当前路径分为A、B两部分。其中，必然有 (1)A部分剩余油量<0。(2)B部分剩余油量>0。
所以，无论多少个站，都可以抽象为两个站点（A、B）。(1)从B站加满油出发，(2)开往A站，车加油，(3)再开回B站的过程。
重点：B剩余的油>=A缺少的总油。必然可以推出，B剩余的油>=A站点的每个子站点缺少的油。


I have thought for a long time and got two ideas:

- If car starts at A and can not reach B. Any station between A and B
can not reach B.(B is the first station that A can not reach.)
- If the total number of gas is bigger than the total number of cost. There must be a solution.
        
Proof of idea 1:
- Assume A is reachable to any points before B.
- The gas on car when it is at station A is 0.
- When the car reaches station x (x is between A and B), the gas on car is g (and g >= 0).
- If starting from x with gas amount g could not reach B, then starts from x with gas amount 0 could not reach B.
- For cases when there are stations between A and B that are not reachable from A, we can reduce these cases to the above situation.

Proof of idea 2:
- We assume that a car could run even when there is negative amount of oil and the oil dash board would goes down to the negative space. (let's imagine that would happen)
- Then we start from station 0, and keep track of the amount of oil. When we go to the end of station, our oil dash board amount would be g (g >= 0)
- There would be a toughest time that the oil dash board shows the minimum amount of oil. Assume the position is x;
- We start from x and goes to the end of station. Then we will never come to the situation that our oil dash board goes below 0.
- We go from end of station to station 0. We have oil g left.
- We start from station 0 and then to x. We will never come to the situation that our oil dash board goes below 0;
Approved
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """

        :param gas:
        :param cost:
        :return:
        """
        rest, run, start = 0, 0, 0
        for i in range(len(gas)):
            run += (gas[i] - cost[i])
            rest += (gas[i] - cost[i])
            print(i, run, rest, start)
            if run < 0:
                start = i + 1
                run = 0
        return -1 if rest < 0 else start

    def canCompleteCircuit2(self, gas, cost):
        """
        暴力解法,超时
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        for i in range(n):
            s = gas[i]  # 初始油量
            flag = True
            for j in range(i, i + n + 1):
                index = j % n
                s = s - cost[index]  # 到下一站还剩的油量
                # print(i, gas[index], cost[index], s)
                if s < 0:
                    flag = False
                    break
                s += gas[(index + 1) % n]  # 成功到达下一站,加油
                # print(i, gas[index], cost[index], s)
            if flag:
                return i
        return -1

    def canCompleteCircuit3(self, gas, cost):
        """
        :param gas:
        :param cost:
        :return:
        """
        n = len(gas)
        dp = [0] * n
        dp[0] = gas[0] - cost[0]
        for i in range(1,n):  # # dp[i] stores the left gas at position i, assume -1 is zero
            dp[i] = dp[i - 1] + gas[i] - cost[i]
        # print(dp)
        if dp[-1] >= 0: # gas - cost of the whole trip
            pos = dp.index(min(dp)) + 1
            if pos >= n:
                return 0
            else:
                return pos
        else:
            return -1


s = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print(s.canCompleteCircuit3(gas, cost))
