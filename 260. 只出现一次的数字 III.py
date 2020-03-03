# -*- coding:utf-8 -*-

"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

解题思路:

假设两个数只出现一次的数为 a, b
1. 第一次异或遍历求出 x = a ^ b
2. 找出 x 的最低位的1 (x & -x), 记这个数为y,
   可以按这位上为1和0 (y & 1), 将数组可以分为 2 堆, a 和 b就分别是这两堆数中唯一一个出现只出现一次的数字
3. 再次遍历数组, 便可以分离出 a 和 b
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        y = x & -x
        a, b = 0, 0
        for num in nums:
            if num & y:
                a ^= num
            else:
                b ^= num
        return [a, b]


s = Solution()
nums = [1, 2, 1, 3, 2, 5]
print(s.singleNumber(nums))
