# -*- coding:utf-8 -*-

"""
给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，
且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

示例 1：
输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。

示例 2：
输入：[23,2,6,4,7], k = 6
输出：True
解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
 

说明：
数组的长度不会超过 10,000 。
你可以认为所有数字总和在 32 位有符号整数范围内。

1. 分情况讨论(k = 0, k < 0, k > 0)
2. 哈希 + 前缀和
3. 同余定理
"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if k == 0:
            s = 0
            ht = {0:-1}
            for i in range(n):
                s += nums[i]
                if s in ht:
                    if i - ht[s] > 1:
                        return True
                else:
                    ht[s] = i
            return False

        if k < 0:
            k = -k

        nums = [(x % k + k) % k for x in nums]
        ht = {0:-1}
        s = 0
        for i in range(n):
            s = (nums[i] + s) % k
            if s in ht:
                if i - ht[s] > 1:  # 长度最小为2
                    return True
            else:
                ht[s] = i   # 记录最左边的， 例: [0,0]，0 的情况

        return False