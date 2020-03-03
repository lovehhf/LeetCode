# -*- coding:utf-8 -*-

"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例 2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

限制：

1 <= n <= 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def twoSum(self, n: int) -> List[float]:
        f = [[0] * (n * 6 + 1) for _ in range(n + 1)]

        for i in range(1, 7):
            f[1][i] = 1

        # f[i][j]: i 个骰子, 点数为 j 的出现次数
        # f[i][j] += f[i - 1][j - k] for k in range(1, 7)
        for i in range(2, n + 1):
            for j in range(i, i * 6 + 1):
                for k in range(1, 7):
                    # 当前点数 - 本次迭代的值小于了上一轮迭代的最小可能的值, 这种情况不可能会出现
                    if j - k < i - 1:
                        break
                    f[i][j] += f[i - 1][j - k]

        x = 6 ** n
        res = [i / x for i in f[-1] if i > 0]
        return res


n = 2
s = Solution()
print(s.twoSum(n))