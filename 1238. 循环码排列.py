# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足：

p[0] = start
p[i] 和 p[i+1] 的二进制表示形式只有一位不同
p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同
 

示例 1：

输入：n = 2, start = 3
输出：[3,2,0,1]
解释：这个排列的二进制表示是 (11,10,00,01)
     所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
示例 2：

输出：n = 3, start = 2
输出：[2,6,7,5,4,0,1,3]
解释：这个排列的二进制表示是 (010,110,111,101,100,000,001,011)
 

提示：

1 <= n <= 16
0 <= start < 2^n
"""

from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        """
        题目和89. 格雷编码很像，
        升级版的格雷编码， 要求第一个数与最后一个数也只差一位
        从0生成格雷编码再找到开始的位置重新排序
        :param n:
        :param start:
        :return:
        """
        nums = ['0', '1']
        for i in range(1, n):
            nums = ['0' + x for x in nums] + ['1' + x for x in reversed(nums)]
        # print(nums)
        nums = [int(x, 2) for x in nums]
        i = nums.index(start)
        return nums[i:] + nums[:i]


s = Solution()
n = 2
start = 3
print(s.circularPermutation(n, start))
