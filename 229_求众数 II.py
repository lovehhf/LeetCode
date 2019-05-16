# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

169_求众数 进阶版

摩尔投票算法
摩尔投票法。该算法用于1/2情况，它说：“在任何数组中，出现次数大于该数组长度一半的值只能有一个。”
那么，改进一下用于1/3。可以着么说：“在任何数组中，出现次数大于该数组长度1/3的值最多只有两个。”
于是，需要定义两个变量。空间复杂度为O(1)。

摩尔投票算法(Boyer–Moore majority vote algorithm)又名多数投票算法，
通过线性时间和常数空间来查找数组中的多数元素，关于该算法的详细理解和解释参考理解摩尔投票算法(https://www.zhihu.com/question/49973163)。
我们只需要对原数组进行两趟扫描，第一趟扫描我们得到候选元素candidate，第二趟扫描我们判断candidate出现的次数是否大于⌊ n/3 ⌋。
"""


class Solution:
    def majorityElement(self, nums):
        """
        :param nums:
        :return:
        """
        res = []
        n = len(nums)
        if n<=1:
            return nums
        a, b = 0, 0  # 2个可能的数
        ca, cb = 0, 0  # 如果某个数字出现大于1/3 那个在遍历过程中ca,cb不会<0
        for i in range(n):
            if a == nums[i]:
                ca += 1
            elif b == nums[i]:
                cb += 1
            elif ca == 0:
                a = nums[i]
                ca = 1
            elif cb == 0:
                b = nums[i]
                cb = 1
            else:
                ca -= 1
                cb -= 1
        ca, cb = 0, 0
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
        if ca > n // 3:
            res.append(a)
        if cb > n // 3:
            res.append(b)

        return res


s = Solution()
nums = [1, 1, 1, 3, 3, 2, 2,2]
print(s.majorityElement(nums))
