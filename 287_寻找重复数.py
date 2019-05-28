# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n^2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

快慢指针，一个时间复杂度为O(N)的算法。

其一，对于链表问题，使用快慢指针可以判断是否有环。
其二，本题可以使用数组配合下标，抽象成链表问题。但是难点是要定位环的入口位置。
举个例子：nums = [2,5, 9 ,6,9,3,8, 9 ,7,1]，构造成链表就是：2->[9]->1->5->3->6->8->7->[9]，也就是在[9]处循环。
其三，快慢指针问题，会在环内的[9]->1->5->3->6->8->7->[9]任何一个节点追上，不一定是在[9]处相碰，事实上会在7处碰上。
其四，必须另起一个for循环定位环入口位置[9]。这里需要数学证明。
"""


class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        while slow != fast or (slow == 0 and fast == 0):
            slow, fast = nums[slow], nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate2(self, nums):
        """
        超时
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[i]


s = Solution()
nums = [3, 1, 3, 4, 2]
print(s.findDuplicate(nums))
