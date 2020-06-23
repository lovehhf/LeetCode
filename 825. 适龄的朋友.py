# -*- coding:utf-8 -*-

"""
人们会互相发送好友请求，现在给定一个包含有他们年龄的数组，ages[i] 表示第 i 个人的年龄。
当满足以下条件时，A 不能给 B（A、B不为同一人）发送好友请求：
age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
否则，A 可以给 B 发送好友请求。
注意如果 A 向 B 发出了请求，不等于 B 也一定会向 A 发出请求。而且，人们不会给自己发送好友请求。 
求总共会发出多少份好友请求?

示例 1:
输入: [16,16]
输出: 2
解释: 二人可以互发好友申请。

示例 2:
输入: [16,17,18]
输出: 2
解释: 好友请求可产生于 17 -> 16, 18 -> 17.

示例 3:
输入: [20,30,100,110,120]
输出: 3
解释: 好友请求可产生于 110 -> 100, 120 -> 110, 120 -> 100.

说明:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.

825. 适龄的朋友
链接：https://leetcode-cn.com/problems/friends-of-appropriate-ages
"""

from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        """
        排序 + 双指针
        """
        ages.sort()
        res = 0
        j = 0
        # age不相等的小盆友
        for i in range(1, len(ages)):
            while j < i and ages[j] <= ages[i] // 2 + 7:
                j += 1
            res += i - j

        j = 0
        # age相等的小朋友
        for i in range(len(ages)):
            while j < i and ages[j] < ages[i]:
                j += 1
            if (ages[j] > ages[i] // 2 + 7):
                res += i - j

        return res


ages = [8, 85, 24, 85, 69]
s = Solution()
print(s.numFriendRequests(ages))
