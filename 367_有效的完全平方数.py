# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        牛顿迭代法：
        牛顿逼近法本来就是求方程近似解的，只要这道题目本来就是f(x)=x*x - num = 0，有整数解。 那不断逼近整数解的Xn = Xm - f(Xm) / f'(Xm)。如果能得到这个Xn就可以返回True了。
        f'(X)是f(X)的导数，为2x，因此Xn=(Xm - num / Xm) / 2 持续迭代下去就好了。
        :param num:
        :return:
        """
        r = num
        while r*r > num:
            r = (r+num/r)/2
            print(r)
        if r*r == num:
            return True
        return False

    def isPerfectSquare3(self, num: int) -> bool:
        """
        二分区间
        :param num:
        :return:
        """
        if num == 0:
            return False
        # 高低指针
        left, right = 0, num
        while left <= right:
            mid = left+(right-left)//2
            tmp = mid*mid
            if  tmp == num:
                return True
            elif tmp>num:
                # mid的平方比num大 说明是sqrt(num)在左区间
                right = mid - 1
            else:
                # mid的平方比num小 说明sqrt(num)在右区间
                left = mid + 1
        return False

    def isPerfectSquare2(self, num: int) -> bool:
        """
        1+3+5+7+9+…+(2n-1)=n^2
        完全平方数肯定是前n个连续奇数的和
        :type num: int
        :rtype: bool
        """
        sum = 1
        while num>0:
            num -= sum
            sum += 2
        return num ==0


s = Solution()
print(s.isPerfectSquare3(9999999999999999**2))