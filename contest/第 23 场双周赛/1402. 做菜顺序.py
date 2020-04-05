# -*- coding:utf-8 -*-

"""
一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1 单位时间。
一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 time[i]*satisfaction[i] 。
请你返回做完所有菜 「喜爱时间」总和的最大值为多少。
你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。

示例 1：
输入：satisfaction = [-1,-8,0,5,-9]
输出：14
解释：去掉第二道和最后一道菜，最大的喜爱时间系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。

示例 2：
输入：satisfaction = [4,3,2]
输出：20
解释：按照原来顺序相反的时间做菜 (2*1 + 3*2 + 4*3 = 20)

示例 3：
输入：satisfaction = [-1,-4,-5]
输出：0
解释：大家都不喜欢这些菜，所以不做任何菜可以获得最大的喜爱时间系数。

示例 4：
输入：satisfaction = [-2,5,-1,0,3,-3]
输出：35

提示：
n == satisfaction.length
1 <= n <= 500
-10^3 <= satisfaction[i] <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reducing-dishes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

方法一:
dp + 贪心
1. 先对 satisfaction 排序, 贪心思路: 先做分值小的菜, 越往后的菜满意程度乘的值越大
2. 遍历 satisfaction 数组, 枚举 0 ~ i 为起点(j), 使用 f[i][j] 表示做菜顺序 j ~ i 的喜爱时间系数和。
3. 状态转移方程: f[i][j] = f[i - 1][j] + satisfaction[i] * (i - j + 1)
答案: max(f[n - 1])
时间复杂度: O(n^2)

方法二:
贪心
1. 逆序排序
2. 从后面一个一个加入
3. 每新加一个数，之前加过的所有数都会多加一遍
时间复杂度: O(n)
"""

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        f = [[0] * 510 for _ in range(510)]

        for i in range(n):
            for j in range(i + 1):
                f[i][j] = f[i - 1][j] + satisfaction[i] * (i - j + 1)

        return max(f[n - 1])


class Solution_2:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = 0
        s = 0

        # 分值最高的菜肯定是最后做的, 前面的分值为负的菜做不做就不知道了
        satisfaction.sort(reverse=True)

        n = len(satisfaction)

        for i in range(n):
            s += satisfaction[i]
            if s < 0:
                break
            # 每新加一个新菜，之前加过的所有菜都会多加一遍, 直到和 < 0, 对总的分值就会减少了
            res += s

        return res


satisfaction = [-1, -8, 0, 5, -9]
sol = Solution_2()
print(sol.maxSatisfaction(satisfaction))
