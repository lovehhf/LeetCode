# -*- coding:utf-8 -*-

__author__ = 'huanghf'


"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""
def removeElement(nums, val):

    # 双指针法
    i, j = 0, 0
    n = len(nums)
    for j in range(n):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return nums

    # # 逆序循环
    # j = len(nums)
    # for i in range(j - 1, -1, -1):
    #     if nums[i] == val:
    #         nums.pop(i)
    # return len(nums)

print(removeElement([3,2,2,3,3,5,3],3))