# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
示例 :

输入: n = 10, pick = 6
输出: 6
"""


class Solution(object):
    def __init__(self,pick):
        self.pick = pick

    def guess(self,n):
        if n == self.pick:
            return 0
        elif n < self.pick:
            return 1
        else:
            return -1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = 0
        R = n+1
        while L<R:
            mid = L+(R-L)//2
            print(mid)
            res = self.guess(mid)
            if res==0:
                return mid
            elif res == 1:
                L = mid
            else:
                R = mid

n = 3
pick = 1
s = Solution(pick)
print(s.guessNumber(10))