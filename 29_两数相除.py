# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3

示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""


class Solution(object):

    def divide(self, dividend, divisor):
        """
        :param dividend:
        :param divisor:
        :return:
        """
        positive = (dividend < 0) is (divisor < 0)  # 符号
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        c, sub = 1, divisor
        while (dividend >= divisor):
            """
            for example, if we want to calc (17/2)
            ret = 0
            17-2 ,ret+=1 left=15
            15-4 ,ret+=2 left=11
            11-8 ,ret+=4 left=3
            3-2 ,ret+=1 left=1

            ret=8
            """
            print(dividend,c, sub,res)

            if (dividend >= sub):
                dividend -= sub
                res += c
                sub <<= 1
                c <<= 1
            else:
                sub >>= 1
                c >>= 1

        if not positive:
            res = -res
        return min(max(-2**31, res), 2**31-1)
    
    def divide2(self, dividend, divisor):
        """
        效率低
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        res = 0
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            dividend,divisor = abs(dividend),abs(divisor)
            for i in range(0,dividend):
                dividend -= divisor
                res += 1
                if dividend==0:
                    return -res
                if dividend<0:
                    return 1-res
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            dividend,divisor = abs(dividend),abs(divisor)
            for i in range(0,dividend):
                dividend -= divisor
                res += 1
                if dividend==0:
                    return res
                if dividend<0:
                    return res-1

    def divide3(self, dividend, divisor):
        """
        翻倍逼近 类似于 折半查找

        23/3  :
        a .  3翻倍：3•2=6    余数17
        b.   再次翻倍 6•2=12 ;   余数11
        c.   再次翻倍128•2=24  此时24 大于23 了 返回b 此时3×2^2 余数为11 加权值p=2
        d    用11/3继续上述操作直至余数小于3 此时为3×2^1 余数为5   加权值p=1，
        5/3   继续上述操作直至余数小于3 此时为3*2^0 余数为2 此时循环结束  加权值p=0 每一步得到一个每一位数的权值序列：【2,1,0】
        最后商的数字为2^2 + 2^1 + 2^0 = 4+2+1 =7

        作者：高大宽333
        链接：https://www.jianshu.com/p/486bcaa8a2df
        来源：简书
        简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
        :param dividend:
        :param divisor:
        :return:
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor # temp:除数
            i = 1          # 初始 i=1
            # print(temp, i)
            while dividend >= temp:
                print(dividend,temp,i,res)
                dividend -= temp  # 被除数 = 被除数-temp
                res += i          # 结果+i
                i <<= 1           # i = i*2
                temp <<= 1        # temp = temp*2 temp是 i*除数

        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

s = Solution()
# print(s.divide(-2147483648,-1))
print(s.divide3(-17,-2))