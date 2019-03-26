# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        理论上数字4幂的二进制类似于100，10000，1000000，etc...形式。可以有如下结论：
        4的幂一定是2的。
        2的幂减1与原数做与运算结果一定是0
        4的幂和2的幂一样，只会出现一位1。但是，4的1总是出现在奇数位。
        :param num:
        :return:
        """
        if num <= 0 or num&(num-1)!=0:
            return False
        # 4的幂次-1一定是3的倍数
        # return (num - 1) % 3 == 0
        # 0x5 = 0101b可以用来校验奇数位上的1
        return bool(0x55555555 & num)


    def isPowerOfFour5(self, num: int) -> bool:
        """
        :param num:
        :return:
        """
        if num <= 0 or num&(num-1)!=0:
            return False
        # 100 & 011+1 = 100
        # num 与 -num 做与运算结果还是num
        t = num & -num
        return num & 0x55555555 and num==t

    def isPowerOfFour4(self, num: int) -> bool:
        """
        不用循环或递归
        4的二进制格式: 100，10000，1000000...
        :param num:
        :return:
        """
        if num <= 0:
            return False
        num_bin = bin(num)[2:]
        if len(num_bin)%2!=0 and num_bin[0] == '1':
            if num_bin[1:]:
                if int(num_bin[1:])==0:
                    return True
            else:
                return True
        return False

    def isPowerOfFour3(self, num: int) -> bool:
        """
        递归
        :param num:
        :return:
        """
        if num == 0:
            return False
        if num == 1:
            return True
        if num%4==0:
            return self.isPowerOfFour(num//4)
        return False


    def isPowerOfFour2(self, num: int) -> bool:
        """
        循环
        :param num:
        :return:
        """
        while num>1:
            num /= 4
        return num==1



num  = 1
s = Solution()
print(s.isPowerOfFour5(num))