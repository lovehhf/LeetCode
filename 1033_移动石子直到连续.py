# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""

用户通过次数 353
用户尝试次数 418
通过次数 359
提交次数 1357
题目难度 Easy
三枚石子放置在数轴上，位置分别为 a，b，c。

每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]

 

示例 1：

输入：a = 1, b = 2, c = 5
输出：[1, 2]
解释：将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。
示例 2：

输入：a = 4, b = 3, c = 2
输出：[0, 0]
解释：我们无法进行任何移动。
 

提示：

1 <= a <= 100
1 <= b <= 100
1 <= c <= 100
a != b, b != c, c != a
"""

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        x,y,z = sorted([a, b, c])
        maximum_moves = z-x-2
        if z-y == 1 and y-x == 1:
            minimum_moves = 0
        elif z-y == 2 or y-x == 2 or z-y == 1 or y-x==1:
            minimum_moves = 1
        else:
            minimum_moves = 2
        return [minimum_moves,maximum_moves]

a = 4
b = 3
c = 2
s = Solution()
print(s.numMovesStones(a,b,c))