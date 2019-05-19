# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
示例：

输入：[2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 1000

感觉应该用回溯XXXX 

[31,26,33,21,40]->[21, 26, 31, 33, 40]
1.选21,40 -> 19,26,31,33
2.[19,26,31,33] -> [7,2]->5

经典背包问题。
问题类似于把所有的数分为2组，
两组数的和的最小差是多少
https://leetcode.com/problems/last-stone-weight-ii/discuss/294888/JavaC%2B%2BPython-Easy-Knapsacks-DP

所有的数都可以分别装进2个背包
最后剩下的石头价值等于这两个背包的差异

https://leetcode.com/problems/last-stone-weight-ii/discuss/295020/Python-solution-easy-to-understand
we could split the stones into two piles A and B, so that abs( A - B ) has a minimum value. Thus each stone is either in pile A or pile B. now we simply need to figure out how to spilt the stones.
as metioned above, each stone is only in one of the two piles, let's denote dp[i] as whether to put the i-th(starting from 0) stone in to A or B.

if we put it into A, then for all the results that before the i-th stone, we add the weight of i-th stone to them.
if we put it into B, then for all the results that before the i-th stone, we subtract the weight of i-th stone from them.
keep doing this until we put the last stone into calculation. at this point, we simply take a look at final results and the minimum abs value is the answer. below is the code:
"""


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        暂时看不懂
        :type stones: List[int]
        :rtype: int
        """
        dp = {0}
        for a in stones:
            dp = {a + i for i in dp} | {a - i for i in dp}
        # print(dp)
        return min(abs(i) for i in dp)

    def lastStoneWeightII2(self, stones):
        """
        看不懂+1
        :param stones:
        :return:
        """
        dp = [0] * 1501
        dp[0] = 1
        s = 0
        res = 100
        for a in stones:
            s += a
            for i in range(1500, a - 1, -1):
                dp[i] += dp[i - a]
        for i in range(1500):
            res = min(res, abs(s - dp[i] * i * 2))
        print(dp)
        return res


stones = [31, 26, 33, 21, 40]
s = Solution()
print(s.lastStoneWeightII2(stones))
