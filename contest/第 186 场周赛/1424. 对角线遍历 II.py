# -*- coding:utf-8 -*-

"""
链接: https://leetcode-cn.com/problems/diagonal-traverse-ii/

给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。

示例 1：
输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,4,2,7,5,3,8,6,9]

示例 2：
输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

示例 3：
输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
输出：[1,4,2,5,3,8,6,9,7,10,11]

示例 4：
输入：nums = [[1,2,3,4,5,6]]
输出：[1,2,3,4,5,6]


提示：
1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
nums 中最多有 10^5 个数字。
"""

import collections
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        ht = collections.defaultdict(list)  # y = -x + b, 使用 哈希表存所有 b 相同的对角线上的元素

        res = []
        ma = 0
        for i in range(m):
            for j in range(len(nums[i])):
                ht[i + j].insert(0, nums[i][j])  # 因为是从上到下遍历的， 所以新遍历到的肯定是在前面， 没必要再进行排序
                ma = max(ma, i + j)

        for i in range(ma + 1):
            res += ht[i]

        return res


s = Solution()
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
print(s.findDiagonalOrder(nums))
