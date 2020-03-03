# -*- coding:utf-8 -*-

"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        单调队列
        :param nums:
        :param k:
        :return:
        """

        n = len(nums)
        queue = []
        res = []
        for i in range(n):
            # 队头元素已经滑出窗口, 弹出
            if queue and i - k + 1 > queue[0]:
                queue.pop(0)

            # 队列中只保留单调递减的元素的下标, 从队尾开始删除比 nums[i] 大的元素
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()

            # 将新的下标加入到队尾
            queue.append(i)

            if i >= k - 1:
                res.append(nums[queue[0]])

        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))