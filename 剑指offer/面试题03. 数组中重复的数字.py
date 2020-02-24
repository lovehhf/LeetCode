# -*- coding:utf-8 -*-

"""
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


做法一: 排序, 时间复杂度 O(nlogn), 空间复杂度 O(1)
做法二: 哈希表, 时间复杂度 O(n), 空间复杂度 O(n)
做法三: 抽屉原理: 时间复杂度 O(n), 空间复杂度 O(1)
  由于数组元素的值都在范围 0 ~ n-1 内，这个范围恰恰好与数组的下标可以一一对应, 可以将每个元素放到下标等于元素值对应的位置。

"""

from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while(i != nums[i]):
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # 这里不能写成 nums[i], nums[nums[i]] = nums[nums[i]], nums[i], 会死循环
                t = nums[i]
                nums[i] = nums[t]
                nums[t] = t


def test(nums: List[int]):
    i = 0
    print(nums[i], nums[nums[i]])  # 2, 1
    # 1.在赋值之前先计算等号右边的值
    # 2.计算时的结果不参与二次计算，而是使用原来的值进行计算
    #
    # 1. nums[0] = 2， 先算出 nums[0] = nums[2] 得到 nums[0] = 1
    # 2. nums[i] 是个引用, 从 nums[2] 变为了nums[1] -> nums[1] = 2
    nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
    print(nums)

s = Solution()
nums = [2, 3, 1, 0, 2, 5, 3]
test(nums)
print(s.findRepeatNumber(nums))

import dis
print(dis.dis(test))