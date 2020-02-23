# -*- coding:utf-8 -*-

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：

1 <= 数组长度 <= 50000

注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        正常操作： 1. 排序 2, 字典统计数字出现次数
        骚操作：
        某数字x出现的次数超过数组长度的一半 则出现的次数减去其他数字出现的次数一定 > 0, 使用变量 c 统计x出现的次数减掉其他数字出现的次数
        遍历数组, 最后c > 0 的数字一定会是该数字
        :param nums:
        :return:
        """
        res = nums[0]
        c = 0
        for num in nums:
            if num == res:
                c += 1
            else:
                c -= 1

            if c < 0:
                res = num
                c = 1

        return res
