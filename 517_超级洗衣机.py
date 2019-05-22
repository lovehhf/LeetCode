# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m （1 ≤ m ≤ n） 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数。如果不能使每台洗衣机中衣物的数量相等，则返回 -1。

 

示例 1：

输入: [1,0,5]

输出: 3

解释: 
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2   
示例 2：

输入: [0,3,0]

输出: 2

解释: 
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1     
示例 3:

输入: [0,2,0]

输出: -1

解释: 
不可能让所有三个洗衣机同时剩下相同数量的衣物。
 

提示：

n 的范围是 [1, 10000]。
在每台超级洗衣机中，衣物数量的范围是 [0, 1e5]。


解题思路:
逐一枚举所有的洗衣机，假设当前枚举的洗衣机编号为 i，则
统计该洗衣机左边的衣服总量 left_sum = [0, i - 1] 中
该洗衣机右边的洗衣机里面的衣服总量和 right_sum = [i + 1, n - 1]
如果发现left_sum < i * avg，即i左边的衣服数量少 需要经过这台洗衣机往左边运送i * avg-left_sum的衣服
如果发现right_sum < avg*(n-i-1) 说明右边的衣服少,需要经过这台洗衣机运动right_sum<avg*(n-i-1)的衣服到右边的洗衣机
这台洗衣机的工作量就是left_sum+right_sum 
由于多个洗衣机可以并行同时运送，工作量最大的洗衣机就是要求的答案
"""


class Solution(object):
    def findMinMoves(self, machines):
        """
        减少空间和计算量
        :param machines:
        :return:
        """
        n = len(machines)
        total = sum(machines)
        if total % n:
            return -1
        avg = total // n
        left_sum, right_sum = 0, total
        res = 0
        for i in range(n):
            right_sum -= machines[i]
            toLeft = max(avg * i - left_sum, 0)
            toRight = max(avg * (n - i - 1) - right_sum, 0)
            res = max(toLeft + toRight, res)
            left_sum += machines[i]
        return res

    def findMinMoves2(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n = len(machines)
        if sum(machines) % n == 0:
            avg = sum(machines) // n
        else:
            return -1
        dp = [0] * (n + 1)
        for i in range(n):
            left_sum = sum(machines[:i])
            right_sum = sum(machines[i + 1:])
            toLeft = avg * i - left_sum if left_sum < avg * i else 0
            toRight = avg * (n - i - 1) - right_sum if right_sum < avg * (n - i - 1) else 0
            dp[i] = toLeft + toRight
        return max(dp)


machines = [0, 3, 0]
s = Solution()
print(s.findMinMoves(machines))
