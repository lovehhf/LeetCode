# -*- coding:utf-8 -*-

"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1

限制：
1 <= nums.length <= 10000
1 <= nums[i] < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        枚举每一位， 出现 3 次的数的每位出现的次数加起来肯定都是 3 的倍数
        如果某一位出现的次数不能被3整数, 说明只出现一位的数中这一位是1
        :param nums:
        :return:
        """
        res = 0
        for i in range(32):
            t = 1
            t <<= i
            count = 0
            for num in nums:
                if (t & num):
                    count += 1
            if (count % 3):
                res += t
        return res
