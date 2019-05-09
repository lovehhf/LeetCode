# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。

示例 1:

输入: 12
输出: 21
示例 2:

输入: 21
输出: -1


和31.下一个排列类似
123654 -> 124356
230241 -> 230412
2302431 -> 2303124
# 从右往左遍历找到最后一个元素应该插入的位置,然后对后面剩下的元素排序(思路错了,以前做出来的时候没写思路好烦啊)

应该是从右往左遍历 找到第一个不是顺序排列的数字,而不是第一个比最右的数小的数
找到了这个数i之后再最后的数开始往右遍历,找到第一个比i大的数j与i交换,然后i 后面的重新排序
"""


class Solution(object):
    def nextGreaterElement(self, n):
        """
        转为list来做,和31类似
        :type n: int
        :rtype: int
        """
        nums = [int(x) for x in str(n)]
        if sorted(nums)[::-1] == nums:
            return -1
        m = len(nums)
        for i in range(m - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(m - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i + 1:] = sorted(nums[i + 1:])
                        break
                break
        res = 0
        for i in nums:
            res = 10 * res + i
        return res if res<2**31 else -1

        # 思路错了
        # for i in range(m - 2, -1, -1):
        #     if nums[i] < nums[m - 1]:
        #         nums[i], nums[m - 1] = nums[m - 1], nums[i]
        #         nums[i + 1:] = sorted(nums[i + 1:])
        #         break



n = 2302431
s = Solution()
print(s.nextGreaterElement(n))
