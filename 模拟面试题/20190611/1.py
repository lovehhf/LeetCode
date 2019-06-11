# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明: 
你可以假设 nums 的长度≥ k-1 且k ≥ 1。
"""

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort(reverse = True)
        while len(self.nums)>self.k:
            self.nums.pop()
        return self.nums[-1]

arr = []
s = KthLargest(1,arr)
print(s.add(3))
print(s.add(5))
print(s.add(10))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
