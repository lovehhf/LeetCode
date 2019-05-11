# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"
"""

import re


class Solution(object):
    def countAndSay(self, n):
        """
        从左往右推
        使用队列存储上一个数,然后不断删掉第一个数,直到队列删光了,使用c计数
        :type n: int
        :rtype: str
        """
        dp = [''] * (n)
        dp[0] = '1'
        for i in range(1, n):
            queue = list(dp[i - 1])
            tmp = ''
            c = 1
            while queue:
                cur = queue.pop(0)
                if queue and queue[0] == cur:
                    c += 1
                else:
                    tmp += str(c) + cur
                    c = 1
            dp[i] = tmp
        return dp[n - 1]

    def countAndSay3(self, n):
        """
        优化空间
        :type n: int
        :rtype: str
        """
        import collections
        res = '1'
        for i in range(1,n):
            queue = collections.deque(res)
            res = ''
            c = 1
            while queue:
                cur = queue.popleft()
                if queue and queue[0]==cur:
                    c += 1
                else:
                    res += str(c)+cur
                    c = 1
        return res

    def countAndSay2(self,nums):
        """
        骚方法:使用re 暂时还学不来
        :param nums:
        :return:
        """
        s = '1'
        for _ in range(nums - 1):
            s = ''.join(str(len(p[0])) + p[1] for p in re.findall(r'((.)\2*)', s))
        return s


s = Solution()
nums = 30
print(s.countAndSay(nums))
print(s.countAndSay2(nums))
print(s.countAndSay3(nums))
