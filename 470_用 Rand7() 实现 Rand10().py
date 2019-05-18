# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。

 

示例 1:

输入: 1
输出: [7]
示例 2:

输入: 2
输出: [8,4]
示例 3:

输入: 3
输出: [8,1,10]
 

提示:

rand7 已定义。
传入参数: n 表示 rand10 的调用次数。
    
进阶:

rand7()调用次数的 期望值 是多少 ?
你能否尽量少调用 rand7() ?

 
把等概率产生数的空间扩大
使得该空间大于要产生新的数的范围，然后
找到最接近这个空间的一个值k，使得k%新数==0
也就是说使得k是这个要新生成数的倍数。

(rand7()-1)*7+rand7()-1 等概率生成0~48的数字
如果生成的数字小于40,模10后生成的就是0~9的随机数

"""
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random


def rand7():
    return random.randint(1, 7)


class Solution(object):
    def rand10(self):
        """
        方法一: (rand7()-1)*7+rand7()-1 等概率生成0~48的数字
        0-7-14-21-28-35-42 + (0~6) 每个数字出现的概率都是随机的
        如果生成的数字小于40,模10后生成的就是0~9的随机数
        rand7()调用次数期望值: 2*(48/40)=2.4次
        :rtype: int
        """
        res = (rand7() - 1) * 7 + rand7() - 1
        if res < 40:
            return 1 + res % 10
        else:
            return self.rand10()

    def rand10_2(self):
        """
        方法二: 调用10次rand7
        :rtype: int
        """
        nums = [rand7()-1 for _ in range(10)]
        return sum(nums)%10 + 1

s = Solution()
print([s.rand10() for _ in range(100)])
