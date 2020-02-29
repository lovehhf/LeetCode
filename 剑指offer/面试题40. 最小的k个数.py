# -*- coding:utf-8 -*-

"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

限制：
0 <= k <= arr.length <= 1000
0 <= arr[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


1. 快速选择算法
2. 使用数组个数为 k 的大根堆记录最小的 k 位数
"""

from typing import List


class Solution:
    def down(self, heap, u, k):
        """
        节点 u 向下移动, 和比 u 小的儿子做交换
        :param heap: 堆
        :param k: 堆元素个数
        :return:
        """
        t = u
        l = t * 2
        r = t * 2 + 1
        if (l <= k and heap[t] < heap[l]):
            t = l
        if (r <= k and heap[t] < heap[r]):
            t = r
        if (u != t):
            heap[t], heap[u] = heap[u], heap[t]
            self.down(heap, t, k)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        建堆
        :param arr:
        :param k:
        :return:
        """
        if k == 0:
            return []
        heap = [0] + arr[:k]
        for i in range(k // 2, 0, -1):
            self.down(heap, i, k)

        for i in range(k, len(arr)):
            if heap[1] > arr[i]:
                heap[1] = arr[i]
                self.down(heap, 1, k)

            # print(heap)
        return heap[1:]

s = Solution()
arr = [2, 3, 4, 1, 9, 6, 5, 8]
k = 3
print(s.getLeastNumbers(arr, k))
