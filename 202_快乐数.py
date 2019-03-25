# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # n 转为整数列表 19 = [1,9]

        now = n
        next_num = self.get_next_num(n)
        res_set = set()
        while not next_num in res_set:
            res_set.add(next_num)
            now,next_num = next_num,self.get_next_num(next_num)
        if now!=1:
            return False
        return True

    def get_next_num(self,n):
        l = []
        while n:
            a = n%10
            n//=10
            l.insert(0,a)
        next_num = sum(map(lambda x:x*x,l))
        return next_num

    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()                #利用 set（）集合，保存平方求和后的数值
        while n != 1:              #利用 while 实现循环
            n = sum([int(i)**2 for i in str(n)])    #通过str（n）调取输入整数各个位数的值
            if n not in mem:       #若平方求和后的数值是首次出现，则添加进集合中
                mem.add(n)
            else:                  #若求和后数值，在集合中存在，则直接返回false,即出现死循环
                return False
        return True                #最终当n==1时，跳出while循环，返回true

s = Solution()
print(s.isHappy(2))