# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m （1 ≤ m ≤ n） 台洗衣机，与此同时**将每台洗衣机的一件衣服送到相邻的一台洗衣机**。

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

res = max(res, toLeft, toRight, toLeft + toRight)
Let's say toLeft = 3 and toRight = -4, which means that this machine must give 3 cloths to its left (this must be done in at least 3 turns) and receive 4 cloths from its right (we don't care since another machine will deal with it).
 Therefore, res = max(res, 3, -4, -1) = max(res, 3).
Then let's say toLeft = 3 and toRight = 4, which means that this machine must give 3 cloths to its left, and also give 4 cloths to its right. 
This can be done in at least 3+4 turns. Therefore, res = max(res, 3, 4, 7) = max(res, 7).


解题思路: 有四个洗衣机，装的衣服数为[0, 0, 11, 5]，最终的状态会变为[4, 4, 4, 4]，那么我们将二者做差，
得到*[-4, -4, 7, 1]，这里负数表示当前洗衣机还需要的衣服数，正数表示当前洗衣机多余的衣服数。我们要做的是*要将这个差值数组每一项都变为0，
对于第一个洗衣机来说，需要四件衣服可以从第二个洗衣机获得，那么就可以 把-4移给二号洗衣机，那么差值数组变为[0, -8, 7, 1]，
此时二号洗衣机需要八件衣服，那么至少需要移动8次。然后二号洗衣机把这八件衣服从三号洗衣机处获得，那么差值数组变为[0, 0, -1, 1]，
此时三号洗衣机还缺1件，就从四号洗衣机处获得，此时差值数组成功变为了[0, 0, 0, 0]，成功。那么移动的最大次数就是差值 数组中出现的绝对值最大的数字，8次
"""


class Solution(object):
    def findMinMoves(self, machines):
        """
        逐一枚举洗衣机，假设当前枚举的洗衣机编号为 i，则
        统计该洗衣机左边的衣服总量 left_sum = [0, i - 1] 中
        该洗衣机右边的洗衣机里面的衣服总量和 right_sum = [i + 1, n - 1]
        如果发现left_sum < i * avg，即i左边的衣服数量少 需要经过这台洗衣机往左边运送i * avg-left_sum的衣服
        如果发现right_sum<avg*(n-i-1) 说明右边的衣服少,需要经过这台洗衣机运动right_sum<avg*(n-i-1)的衣服到右边的洗衣机
        由于多个洗衣机可以并行同时运送，工作量最大的洗衣机就是要求的答案
        :param machines:
        :return:
        """
        n = len(machines)
        total = sum(machines)
        if total % n != 0:
            return -1
        avg = total // n
        left_sum, right_sum = 0, total
        dp = [0] * n
        for i in range(n):
            right_sum -= machines[i]
            toleft = max(avg * i - left_sum, 0)
            toright = max(avg * (n - i - 1) - right_sum, 0)
            dp[i] = toleft + toright
            left_sum += machines[i]
        print(dp)

    def findMinMoves2(self, machines):
        """
        toLeft 这台洗衣机需要移到左边去的衣服数量
        toRight 这台洗衣机需要移到右边去的衣服数量
        :type machines: List[int]
        :rtype: int
        """
        n = len(machines)
        total = sum(machines)
        if total % n != 0:
            return -1
        target = total // n
        toLeft = 0
        res = 0

        for i in range(n):
            toRight = machines[i] - target - toLeft
            res = max(res, toLeft, toRight, toLeft + toRight)
            toLeft = -toRight
        return res

machines = [0, 0, 11, 5]
s = Solution()
print(s.findMinMoves(machines))
print(s.findMinMoves2(machines))
