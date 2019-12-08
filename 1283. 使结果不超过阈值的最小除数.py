# -*- coding:utf-8 -*-

"""
给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。

请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。

每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。

题目保证一定有解。

 

示例 1：

输入：nums = [1,2,5,9], threshold = 6
输出：5
解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
示例 2：

输入：nums = [2,3,5,7,11], threshold = 11
输出：3
示例 3：

输入：nums = [19], threshold = 5
输出：4
 

提示：

1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6

cpp:
class Solution {
public:
    int sum(vector<int>& nums, int div, int threshold)
    {
        int res = 0;
        for(int num : nums) res += ceil(num*1.0/div);
        return res;
    }

    int smallestDivisor(vector<int>& nums, int threshold) {
        int l = 1, r = 1e6, mid;
        while(l < r)
        {
            mid = (l + r) >> 1;
            if(sum(nums, mid, threshold) > threshold) l = mid + 1;
            else r = mid;
        }
        return r;
    }
};
"""

from typing import List

import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        简单二分
        时间复杂度: nums.length*log(max(nums)) = 17*5*10^4 足够了
        :param nums:
        :param threshold:
        :return:
        """
        L, R = 1, max(nums)
        while (L < R):
            mid = (L + R) >> 1
            print(mid, sum(math.ceil(x / mid) for x in nums))
            # 小于等于阈值, 说明 答案不是在mid的左边就是mid
            if(sum(math.ceil(x/mid) for x in nums) <= threshold):
                R = mid
            # 大于阈值, 答案在mid右边
            else:
                L = mid + 1

        return R

nums = [1,2,5,9]
threshold = 6
s = Solution()
print(s.smallestDivisor(nums, 6))