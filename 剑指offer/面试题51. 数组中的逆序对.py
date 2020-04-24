# -*- coding:utf-8 -*-

"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5

限制：
0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def merge_sort(self, nums, l, r):
        if (l >= r):
            return 0

        tmp = []
        mid = (l + r) >> 1

        res = 0
        res += self.merge_sort(nums, l, mid)
        res += self.merge_sort(nums, mid + 1, r)

        i = l
        j = mid + 1
        while (i <= mid and j <= r):
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                res += mid - i + 1
                tmp.append(nums[j])
                j += 1

        if (i <= mid):
            tmp += nums[i:mid + 1]
        if (j <= r):
            tmp += nums[j:r + 1]

        nums[l: r + 1] = tmp
        return res

    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)


s = Solution()
nums = [1,3,2,3,1]
print(s.reversePairs(nums))