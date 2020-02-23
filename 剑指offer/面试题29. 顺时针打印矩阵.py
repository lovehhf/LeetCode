# -*- coding:utf-8 -*-

"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = 0, 0
        vis = [[0] * n for _ in range(m)]
        cur = 0
        res = []
        for _ in range(m * n):
            res.append(matrix[i][j])
            vis[i][j] = 1
            x = i + ds[cur & 3][0]
            y = j + ds[cur & 3][1]
            if x < 0 or x >= m or y < 0 or y >= n or vis[x][y]:
                cur += 1
                x = i + ds[cur & 3][0]
                y = j + ds[cur & 3][1]
            i, j = x, y

        return res


s = Solution()
matrix = [[3],[2]]
print(s.spiralOrder(matrix))
