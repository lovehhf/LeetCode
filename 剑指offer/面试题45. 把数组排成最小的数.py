# -*- coding:utf-8 -*-

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"

提示:
0 < nums.length <= 100

说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from functools import cmp_to_key

from typing import List


class Solution:

    # x + y < y + x,  x 放前面
    def compare(self, x, y):
        return int(int(str(x) + str(y))) - int(int(str(y) + str(x)))

    def minNumber(self, nums: List[int]) -> str:
        res = sorted(nums, key=cmp_to_key(self.compare))
        return "".join([str(x) for x in res])


class QuickSort_Solution:
    """
    快排
    """
    def compare(self, x, y):
        return int(str(x) + str(y)) - int(str(y) + str(x))

    def quick_sort(self, nums, l, r):
        if (l >= r):
            return
        i, j = l - 1, r + 1
        x = nums[(l + r) >> 1]
        while (i < j):
            i += 1
            while (self.compare(nums[i], x) < 0):
                i += 1

            j -= 1
            while (self.compare(nums[j], x) > 0):
                j -= 1

            if(i < j):
                nums[i], nums[j] = nums[j], nums[i]

        self.quick_sort(nums, l, j)
        self.quick_sort(nums, j + 1, r)

    def minNumber(self, nums: List[int]) -> str:
        self.quick_sort(nums, 0, len(nums) - 1)
        res = "".join([str(x) for x in nums])
        return res

class MergeSort_Solution:
    """
    归并排序
    """
    def compare(self, x, y):
        return int(str(x) + str(y)) - int(str(y) + str(x))

    def merge_sort(self, nums, l, r):
        if (l >= r):
            return

        mid = (l + r) >> 1
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)

        i, j = l,  mid + 1
        t = [0] * (r - l + 1)
        k = 0
        while(i <= mid and j <= r):
            if (self.compare(nums[i], nums[j]) < 0):
                t[k] = nums[i]
                k += 1
                i += 1
            else:
                t[k] = nums[j]
                j += 1
                k += 1

        while i <= mid:
            t[k] = nums[i]
            k += 1
            i += 1


        while j <= r:
            t[k] = nums[j]
            j += 1
            k += 1

        for i in range(l, r + 1):
            nums[i] = t[i - l]

    def minNumber(self, nums: List[int]) -> str:
        self.merge_sort(nums, 0, len(nums) - 1)
        res = "".join([str(x) for x in nums])
        return res


s = MergeSort_Solution()
nums = [3,30,34,5,9]
print(s.minNumber(nums))
