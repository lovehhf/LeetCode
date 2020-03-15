# -*- coding:utf-8 -*-

"""
公司有编号为 1 到 n 的 n 个工程师，给你两个数组 speed 和 efficiency ，其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。请你返回由最多 k 个工程师组成的 ​​​​​​最大团队表现值 ，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。
团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。

示例 1：
输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
输出：60
解释：
我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 performance = (10 + 5) * min(4, 7) = 60 。

示例 2：
输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
输出：68
解释：
此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = (2 + 10 + 5) * min(5, 4, 7) = 68 。

示例 3：
输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
输出：72

提示：
1 <= n <= 10^5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10^5
1 <= efficiency[i] <= 10^8
1 <= k <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-performance-of-a-team
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


使用堆 维护k个工人组成组成的表现最好的团队
对工人效率进行排序之后遍历,
  当堆中的元素数量<k时, 直接加入到堆里面
  堆中元素满了则看是否可以干掉堆顶的元素加入新的
"""

import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # 按照员工的工作效率的逆序排序
        engineers = sorted(zip(efficiency, speed), reverse = True)

        h = []  # 堆
        s = 0   # 堆元素的和
        res = 0 # 团队表现值

        for i in range(n):
            speed_i = engineers[i][1]
            efficiency_i = engineers[i][0]
            if i < k:
                # 堆中元素不足 k 个, 直接加入到堆里面 (不能直接建大小为 k 的堆, 因为可能会出现人数越多, 团队表现值反而的情况)
                heapq.heappush(h, speed_i)
                s += speed_i
            elif ((s + speed_i - h[0]) * efficiency_i > res):
                # 加入第 i 名员工的最大团队表现值比当前高, 更新堆中元素和与
                s += speed_i - h[0]
                heapq.heappop(h)  # 弹出堆顶元素
                heapq.heappush(h, speed_i) # 将i的速度插到堆里面去
            res = max(res, s * efficiency_i)

        return res

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 6
s = Solution()
print(s.maxPerformance(n, speed, efficiency, k))