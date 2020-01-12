# -*- coding:utf-8 -*-

"""
二指输入法定制键盘在 XY 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处，例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1)，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。

给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。坐标 (x1,y1) 和 (x2,y2) 之间的距离是 |x1 - x2| + |y1 - y2|。 

注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。

 

示例 1：

输入：word = "CAKE"
输出：3
解释：
使用两根手指输入 "CAKE" 的最佳方案之一是：
手指 1 在字母 'C' 上 -> 移动距离 = 0
手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2
手指 2 在字母 'K' 上 -> 移动距离 = 0
手指 2 在字母 'E' 上 -> 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1
总距离 = 3
示例 2：

输入：word = "HAPPY"
输出：6
解释：
使用两根手指输入 "HAPPY" 的最佳方案之一是：
手指 1 在字母 'H' 上 -> 移动距离 = 0
手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2
手指 2 在字母 'P' 上 -> 移动距离 = 0
手指 2 在字母 'P' 上 -> 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0
手指 1 在字母 'Y' 上 -> 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4
总距离 = 6

示例 3：
输入：word = "NEW"
输出：3

示例 4：
输入：word = "YEAR"
输出：7

提示：
2 <= word.length <= 300
每个 word[i] 都是一个大写英文字母。
"""


class Solution:
    def get_dis(self, a, b):
        """
        获取从下标为a的字母移动到下标为b的字母的曼哈顿距离(花费)
        :param a:
        :param b:
        :return:
        """
        ax, ay = a // 6, a % 6
        bx, by = b // 6, b % 6
        return abs(ax - bx) + abs(ay - by)

    def minimumDistance(self, word: str) -> int:
        """
        dp[i][a][b] 表示输入完第i个字符时手指1放在A上, 手指2放在字母B的最小移动距离
        状态表示:
          i: 输入到第i个字符
          a或b = -1: 表示没有放置手指,
               0~25: 表示手指放在字母'A'-'Z'上
                 26: 表示手指还没有开始输入
        状态转移:
          i-1的状态手指放在a,b, 第i个字母是v
          1. 移动手指1输入 -> dp[i][v][b] = dp[i-1][a][b] + dis[a->v]
          2. 移动手指2输入 -> dp[i][a][v] = dp[i-1][a][b] + dis[b->v]
        :param word:
        :return:
        """
        dp = [[[-1] * 30 for _ in range(30)] for _ in range(310)]
        dp[0][26][26] = 0
        n = len(word)

        for i in range(1, n + 1):
            c = word[i - 1]
            v = ord(c) - ord('A')
            for a in range(0, 27):
                for b in range(0, 27):
                    # =-1 表示之前状态不存在
                    if dp[i - 1][a][b] == -1:
                        continue

                    # 使用之前的状态更新现在的状态
                    # 转移手指1, = 26 表示手指1之前没有输入过, 现在使用手指1花费就是0, 否则就是曼哈顿距离的代价
                    cost = 0 if a == 26 else self.get_dis(a, v)

                    # 现在的状态不存在或者输入的代价变小了, 更新现在的状态
                    if (dp[i][v][b] == -1 or dp[i][v][b] > dp[i - 1][a][b] + cost):
                        dp[i][v][b] = dp[i - 1][a][b] + cost

                    # 转移手指2
                    cost = 0 if b == 26 else self.get_dis(b, v)
                    if (dp[i][a][v] == -1 or dp[i][a][v] > dp[i - 1][a][b] + cost):
                        dp[i][a][v] = dp[i - 1][a][b] + cost
                    # print(i, a, b, v, dp[i][a][v], dp[i][v][b])

        # return min(dp[n][i][j] for i in range(27) for j in range(27) if dp[n][i][j] != -1)

        res = -1
        for i in range(27):
            for j in range(27):
                if(dp[n][i][j] == -1):
                    continue
                if (res == -1 or res > dp[n][i][j]):
                    res = dp[n][i][j]
        return res



s = Solution()
print(s.minimumDistance(word = "YEAR"))
