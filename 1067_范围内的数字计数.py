# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个在 0 到 9 之间的整数 d，和两个正整数 low 和 high 分别作为上下界。返回 d 在 low 和 high 之间的整数中出现的次数，包括边界 low 和 high。

示例 1：

输入：d = 1, low = 1, high = 13
输出：6
解释： 
数字 d=1 在 1,10,11,12,13 中出现 6 次。注意 d=1 在数字 11 中出现两次。
示例 2：

输入：d = 3, low = 100, high = 250
输出：35
解释：
数字 d=3 在 103,113,123,130,131,...,238,239,243 出现 35 次。
 

提示：

0 <= d <= 9
1 <= low <= high <= 2×10^8

12145,1
->
1215+122*10+12*100+46+2*1000+2146

12145,0
1214 + 121*10 + 12*100+1*1000

10000 -> 1000 + 99*10+1 + 9*100+1 +1
9999 -> 999+99*10+9*100

1080,2160,0
"""


class Solution(object):
    def get_num2(self, n, d):
        """
        :param n:
        :param d:
        :return:
        """
        return ''.join([str(x) for x in list(range(1, n + 1))]).count(str(d))

    def get_num(self, n, d):
        """
        计算1~n中d出现的次数 d>1
        :param d:
        :return:
        """
        k = 1
        res = 0
        t = 0
        if d > 0:
            while n:
                y = n % 10
                if y > d:
                    res += (n // 10 + 1) * k
                elif y == d:
                    res += (n // 10) * k + t + 1
                else:
                    res += (n // 10) * k
                n = n // 10
                t = k * y + t
                k *= 10
        else:
            if n % 10==0:
                while n >= 10:
                    y = n % 10
                    n //= 10
                    if k > 1 and y == 0:
                        res += (n - 1) * k + 1
                    else:
                        res += n * k
                    t = k * y + t
                    k *= 10
            else:
                while n >= 10:
                    y = n % 10
                    n //= 10
                    if k > 1 and y == 0:
                        res += t + 1
                    else:
                        res += n * k
                    t = k * y + t
                    k *= 10
        return res

    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        h = self.get_num(high, d)
        l = self.get_num(low - 1, d)
        return h - l


d, low, high = 0, 5000, 10000
s = Solution()
print(s.digitsCount(d, low, high))
# print(s.get_num2(1111, 0))
# print(s.get_num2(10000, 0))
# print(s.get_num(10000, 0))
