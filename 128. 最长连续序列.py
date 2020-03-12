# -*- coding:utf-8 -*-

"""
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路: 1. 使用集合存储 nums 中的所有元素, 集合的查找时间复杂度为 O(1)
     2. 遍历数组, 遇到 num - 1 不在集合中说明是一段序列的开始, 这时候就从集合中查找元素是否在集合中, 在集合中则连续序列长度 + 1继续+1找
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if not num - 1 in s:
                t = num
                while (t in s):
                    t += 1
                res = max(res, t - num)
        return res
