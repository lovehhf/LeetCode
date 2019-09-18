# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
输入为三个整数：day、month 和 year，分别表示日、月、年。
您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。


示例 1：

输入：day = 31, month = 8, year = 2019
输出："Saturday"
示例 2：

输入：day = 18, month = 7, year = 1999
输出："Sunday"
示例 3：

输入：day = 15, month = 8, year = 1993
输出："Sunday"
 

提示：

给出的日期一定是在 1971 到 2100 年之间的有效日期。

1971年1月1日 -> 星期五
1993年8月人15日 -> 星期天
"""


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        weekday = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        days = 0
        for i in range(1971, year):
            if ((i % 4 == 0 and i % 100 != 0) or i % 400 == 0):
                days += 366
                # print(i, 366)
            else:
                days += 365
                # print(i, 365)
        for i in range(1, month):
            month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            days += month_day[i]
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and year > 2:
            days += 1
        days += day - 1
        return weekday[days % 7]


day, month, year = 18, 9, 2019
s = Solution()
print(s.dayOfTheWeek(day, month, year))
