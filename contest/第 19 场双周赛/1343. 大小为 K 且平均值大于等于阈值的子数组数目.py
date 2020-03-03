# -*- coding:utf-8 -*-

"""
给你一个整数数组 arr 和两个整数 k 和 threshold 。

请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

示例 1：
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。

示例 2：
输入：arr = [1,1,1,1,1], k = 1, threshold = 0
输出：5

示例 3：
输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。

示例 4：
输入：arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
输出：1

示例 5：
输入：arr = [4,4,4,4], k = 4, threshold = 1
输出：1
 
提示：
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^4
1 <= k <= arr.length
0 <= threshold <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        遍历, 双指针求和
        :param arr:
        :param k:
        :param threshold:
        :return:
        """
        if k == 1:
            return sum(x >= threshold for x in arr)
        n = len(arr)
        s = sum(arr[0:k])
        res = int(s / k >= threshold)
        for i in range(k, n):
            s += arr[i] - arr[i - k]
            res += (s / k >= threshold)
        return res


s = Solution()
arr = [2852, 5203, 9375, 3209, 932, 9529, 4416, 3525, 2435, 3131, 3232, 2047, 2871, 3550, 5923, 4553, 2086, 5990, 4580,
       2948, 8522, 4850, 3597, 744, 6963, 8126, 2153, 258, 1955, 3169, 3165, 4334, 791, 5342, 4348, 5404, 8531, 1045,
       7767, 9842]
k = 17
threshold = 65
print(s.numOfSubarrays(arr, k, threshold))
