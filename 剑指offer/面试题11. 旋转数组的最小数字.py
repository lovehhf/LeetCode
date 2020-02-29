# -*- coding:utf-8 -*-

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0

注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
        二分, 减治思想
        [3, 4, 5, 1, 2]
        [1, 2, 3, 4, 5]
        // 不能使用左边数与中间数比较，这种做法不能有效地减治

        [1, 2, 3, 4, 5]
        [3, 4, 5, 1, 2]
        [2, 3, 4, 5 ,1]
        :param numbers:
        :return:
        """
        l, r = 0, len(numbers) - 1
        while (l < r):
            mid = (l + r) >> 1
            if numbers[mid] > numbers[r]:
                # 右边无序, 最小数字在右边
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                # 右边有序, 最小数字在左边
                r = mid
            else:
                # 遇到 nums[mid] == nums[r] 的时候，不能草率地下定结论最小数字在哪一边，但是可以确定的是，把 right 舍弃掉，并不影响结果
                r -= 1
        return numbers[l]


class Solution_2:
    def find(self, nums, l, r):
        """
        在区间 l, r 找最小值
        :param nums:
        :param l:
        :param r:
        :return:
        """
        if (l >= r):
            return nums[l]

        mid = (l + r) >> 1

        if (nums[mid] < nums[r]):
            return self.find(nums, l, mid)
        elif (nums[mid] > nums[r]):
            return self.find(nums, mid + 1, r)
        else:
            return self.find(nums, l, r - 1)

    def minArray(self, numbers: List[int]) -> int:
        """
        分治
        :param numbers:
        :return:
        """
        return self.find(numbers, 0, len(numbers) - 1)


nums = [4, 5, 1, 2, 3]
s = Solution_2()
print(s.minArray(nums))
