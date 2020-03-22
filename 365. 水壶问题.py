# -*- coding:utf-8 -*-

"""
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False

方法一:

任意一个时刻，我们可以且仅可以采取以下 6 种操作：

1. 把 X 壶的水灌进 Y 壶，直至灌满或倒空；
2. 把 Y 壶的水灌进 X 壶，直至灌满或倒空；
3. 把 X 壶灌满；
4. 把 Y 壶灌满；
5. 把 X 壶倒空；
6. 把 Y 壶倒空。

方法二:

找到x ,y的最大公约数能否z被整除
"""


class Solution:
    def gcd(self, x, y):
        return x if (y == 0) else self.gcd(y, x % y);

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True

        if x + y < z:
            return False

        if x == 0 or y == 0:
            return x + y == z

        return z % self.gcd(x, y) == 0

class BFS_Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        queue = [(0, 0)]
        s = set()
        while queue:
            rx, ry = queue.pop(0)  # rx: x 壶中剩余的水, ry: y 壶剩余的水
            if (rx == z or ry == z or rx + ry == z):
                return True
            if ((rx, ry) in s):
                continue

            s.add((rx, ry))  # 已经有过该状态
            queue.append((x, ry))  # 灌满 x 壶
            queue.append((rx, y))  # 灌满 y 壶
            queue.append((0, ry))  # 倒空 x 壶
            queue.append((rx, 0))  # 倒空 y 壶

            # x 壶中的水倒入 y 壶
            # 有两种情况, 1. 如果灌满了 y 壶的话, x 壶中用了 y - ry 的水, 2. x 壶中水倒空了
            queue.append((rx - min(rx, y - ry), ry + min(rx, y - ry)))

            # y 壶中的水倒入 x 壶
            queue.append((rx + min(ry, x - rx), ry - min(ry, x - rx)))


s = Solution()
x = 3
y = 5
z = 4
print(s.canMeasureWater(x, y, z))
