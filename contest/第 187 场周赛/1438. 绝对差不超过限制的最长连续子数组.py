# -*- coding:utf-8 -*-

"""
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
如果不存在满足条件的子数组，则返回 0 。

示例 1：
输入：nums = [8,2,4,7], limit = 4
输出：2
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4.
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4.
因此，满足题意的最长子数组的长度为 2 。

示例 2：
输入：nums = [10,1,2,4,7,2], limit = 5
输出：4
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。


示例 3：
输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3

提示：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

堆 + 滑动窗口
维护一个大根堆和一个小根堆，存储最大值和最小值
遍历一遍如果最大值 - 当前值 > limit 或 当前值 - 最小值 > limit, 更新滑窗左边界
"""

import heapq
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i, j = 0, 0
        n = len(nums)
        q1 = []
        q2 = []
        res = 0
        for i in range(n):
            while q1 and nums[i] - q1[0][0] > limit:   # 小根堆
                _, k = heapq.heappop(q1)
                j = max(j, k + 1)

            while q2 and -q2[0][0] - nums[i] > limit:  # 小根堆
                _, k = heapq.heappop(q2)
                j = max(j, k + 1)

            heapq.heappush(q1, (nums[i], i))
            heapq.heappush(q2, (-nums[i], i))

            res = max(res, i - j + 1)

        return res


nums = [10,1,2,4,7,2]
limit = 5
s = Solution()
print(s.longestSubarray(nums, limit))
