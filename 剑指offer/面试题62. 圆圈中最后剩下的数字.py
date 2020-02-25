# -*- coding:utf-8 -*-

"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出: 3

示例 2：
输入: n = 10, m = 17

输出: 2

限制：
1 <= n <= 10^5
1 <= m <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


约瑟夫环, 模拟
"""


class Solution:
    def remove_num(self, nums, i, m):
        """
        以下表为 i 的点为起点, 删除步长为 m 的数, 返回删除之后所在的下标
        :param nums:
        :param i:
        :param m:
        :return:
        """
        n = len(nums)
        k = (i + m - 1) % n
        nums.pop(k)
        return k

    def lastRemaining(self, n: int, m: int) -> int:
        """
        模拟, 直到删除到数组长度为 1
        :param n:
        :param m:
        :return:
        """
        nums = [x for x in range(n)]
        i = 0
        while (len(nums) > 1):
            i = self.remove_num(nums, i, m)
        return nums[0]
