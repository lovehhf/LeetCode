# -*- coding:utf-8 -*-

"""
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。
每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。
注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

示例:
输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        f = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(1, n + 1):
            f[i][i] = nums[i - 1] * nums[i] * nums[i + 1]

        for l in range(1, n + 1):  # 枚举区间长度
            for i in range(1, n):  # 区间左边界
                j = i + l  # 区间右边界
                if j > n:
                    break
                f[i][j] = max(nums[i - 1] * nums[j + 1] * nums[k] + f[i][k - 1] + f[k + 1][j] for k in range(i, j + 1))

        return f[1][n]
