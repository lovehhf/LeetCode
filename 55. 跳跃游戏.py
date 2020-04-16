# -*- coding:utf-8 -*-

"""
55. 跳跃游戏
https://leetcode-cn.com/problems/jump-game/

给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        max_jmp = 0  # 前 i 个点中所有点最远能跳到的距离

        for i in range(n):
            if i > max_jmp:
                # 跳不到 i 号点, 直接返回
                return False
            max_jmp = max(max_jmp, i + nums[i])

        return True

nums = [0]
s = Solution()
print(s.canJump(nums))
