# -*- coding:utf-8 -*-

"""
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例：
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

进阶:
如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
"""
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_1 = []  # 堆1, 小的元素形成的大根堆
        self.heap_2 = []  # 堆2, 大的元素形成的小根堆
        self.count = 0  # 数据流的数量

    # def heap_add(self, heap, x, type):
    #     """
    #     将元素 x 加入到堆 heap 中
    #     :param heap:
    #     :param x:
    #     :param type: 0 为大根堆, 1 为小根堆
    #     :return:
    #     """
    #     heap.append(x)
    #     u = len(heap) - 1
    #     if type == 0:
    #         while (u // 2 and heap[u // 2] < x):
    #             heap[u // 2], heap[u] = heap[u], heap[u // 2]
    #             u //= 2
    #     else:
    #         while (u // 2 and heap[u // 2] > x):
    #             heap[u // 2], heap[u] = heap[u], heap[u // 2]
    #             u //= 2

    def addNum(self, num: int) -> None:
        """
        先将元素加入到大根堆中, 如果大根堆与小根堆的元素数量之差 > 1,
        则将大根堆的堆顶元素移动到小根堆中
        :param num:
        :return:
        """
        self.count += 1

        # 元素取负数加入到大根堆中, heapq默认的是小根堆, 取负数能模拟出大根堆的效果
        heapq.heappush(self.heap_1, -num)

        # 大根堆堆顶元素移动到小根堆
        t = heapq.heappop(self.heap_1)
        heapq.heappush(self.heap_2, -t)

        # 小根堆元素比大根堆多时, 小堆顶元素移动到大根堆
        if self.count & 1:
            t = heapq.heappop(self.heap_2)
            heapq.heappush(self.heap_1, -t)

    def findMedian(self) -> float:
        """
        元素数量
          奇数: 返回 大根堆堆顶
          偶数: 返回 (大根堆堆顶 + 小根堆堆顶) / 2

        由于大根堆中存的是元素的负数, 用的时候需要
        :return:
        """
        if self.count & 1:
            return -self.heap_1[0]
        return (self.heap_2[0] - self.heap_1[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
