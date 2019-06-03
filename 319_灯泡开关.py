# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 
第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 
对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。

示例:

输入: 3
输出: 1 
解释: 
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭].

第1->x轮中，为它的因数的轮次均可以翻转其开关。当翻转次数为奇数时，灯泡最终会亮
只有为可以恰好开方的数才具有奇数个因数，故搜索具有整数平方根的值即可。 
"""


class Solution(object):
    def bulbSwitch(self, n):
        return int(n**0.5)

    def bulbSwitch2(self, n):
        """
        暴力做法 用来看能不能找到规律
        遍历前1000个n 发现res = n**0.5
        :type n: int
        :rtype: int
        """
        l = [1 for _ in range(n)]
        for i in range(2, n + 1):
            for j in range(i - 1, n, i):
                l[j] ^= 1
        return l.count(1)


s = Solution()
n = 1000
print(s.bulbSwitch(n))
for i in range(2,n):
    print(i,s.bulbSwitch(i))
