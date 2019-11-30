# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出一个有序数组 A，数组中的每个数字都是 独一无二的，找出从数组最左边开始的第 K 个缺失数字。

 

示例 1：

输入：A = [4,7,9,10], K = 1
输出：5
解释：
第一个缺失数字为 5 。
示例 2：

输入：A = [4,7,9,10], K = 3
输出：8
解释： 
缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8 。
示例 3：

输入：A = [1,2,4], K = 3
输出：6
解释：
缺失数字有 [3,5,6,7,...]，因此第三个缺失数字为 6 。
 

提示：

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""


class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] - 1 >= k:
                return nums[i] + k
            else:
                k -= nums[i + 1] - nums[i] - 1
        return nums[-1] + k

    def missingElement2(self, nums, k):
        """
        超时
        [247645,695157,1735965,4220736,4322043,9465544,9543270,9900210]
        10
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        set1 = set(nums)
        set2 = set(list(range(nums[0], nums[-1] + k + 1)))
        set3 = set2 - set1
        l = sorted(list(set3))
        # print(l)
        return l[k - 1]


nums = [1,2,4]
k = 3
s = Solution()
print(s.missingElement(nums, k))
