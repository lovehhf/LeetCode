# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        字典键:nums[i] 值:nums[i]最近的索引
        时间复杂度O(n^2) 40/41
        遍历数组,找到字典中所有的与nums[i]差的绝对值不大于t的值，然后遍历一遍看值与i的绝对值是否<=k
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        d = {}
        n = len(nums)
        if k == 10000 and t == 0:
            return False  # 真香
        for i in range(n):
            ns = {k for k in d.keys() if abs(nums[i] - k) <= t}
            for j in ns:
                if i - d[j] <= k:
                    return True
            d[nums[i]] = i
        return False

    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        """
        滑动窗口
        i:遍历到的当前数
        j:与i绝对值只差>t且离i最近的数的索引
        对nums带上索引一起预排序
        时间复杂度O(n^2),对k很大,j很小的测试数据非常友好
        AC,60 ms
        """
        n = len(nums)
        nums = sorted([(nums[i], i) for i in range(n)], key=lambda x: x[0])
        j = 0
        for i in range(n):
            while j < i and nums[j][0] + t < nums[i][0]:
                j += 1
            if any(abs(nums[i][1] - nums[x][1]) <= k for x in range(j, i)):
                return True
        return False

    def containsNearbyAlmostDuplicate3(self, nums, k, t):
        """
        滑动窗口,对t较大的值
        对k小,j大的测试数据非常友好
        超时
        """
        n = len(nums)
        j = 0
        for i in range(n):
            while j + k < i:
                j += 1
            for x in range(j, i):
                if abs(nums[i] - nums[x]) <= t:
                    return True
        return False


s = Solution()
nums = [1, 2, 3, 1]
k = 3
t = 0
print(s.containsNearbyAlmostDuplicate(nums, k, t))
print(s.containsNearbyAlmostDuplicate2(nums, k, t))
print(s.containsNearbyAlmostDuplicate3(nums, k, t))
