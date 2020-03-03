# -*- coding:utf-8 -*-

"""
给你一个整数数组 arr。你可以从中选出一个整数集合，并删除这些整数在数组中的每次出现。
返回 至少 能删除数组中的一半整数的整数集合的最小大小。

示例 1：
输入：arr = [3,3,3,3,5,5,5,2,2,7]
输出：2
解释：选择 {3,7} 使得结果数组为 [5,5,5,2,2]、长度为 5（原数组长度的一半）。
大小为 2 的可行集合有 {3,5},{3,2},{5,2}。
选择 {2,7} 是不可行的，它的结果数组为 [3,3,3,3,5,5,5]，新数组长度大于原数组的二分之一。

示例 2：
输入：arr = [7,7,7,7,7,7]
输出：1
解释：我们只能选择集合 {7}，结果数组为空。

示例 3：
输入：arr = [1,9]
输出：1

示例 4：
输入：arr = [1000,1000,3,7]
输出：1

示例 5：
输入：arr = [1,2,3,4,5,6,7,8,9,10]
输出：5

提示：
1 <= arr.length <= 10^5
arr.length 为偶数
1 <= arr[i] <= 10^5


题意:
找出要求的最小数量的集合 (在列表中干掉集合中包含的元素使得列表剩余的元素数量小于 n / 2)

解题思路:
1. 统计所有元素出现的频率
2. 依次将元素加入到集合中, 统计次数, 统计到>=n/2时集合的大小就是答案
"""

from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        c = sorted(c.values(), reverse=True)
        res = 0
        count = 0
        for i in c:
            count += i
            res += 1
            if count >= len(arr) // 2:
                return res
        return 0
