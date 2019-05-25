# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
864
给定一个二维网格 grid。 "." 代表一个空房间， "#" 代表一堵墙， "@" 是起点，（"a", "b", ...）代表钥匙，（"A", "B", ...）代表锁。

我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。
我们不能在网格外面行走，也无法穿过一堵墙。如果途经一个钥匙，我们就把它捡起来。除非我们手里有对应的钥匙，否则无法通过锁。

假设 K 为钥匙/锁的个数，且满足 1 <= K <= 6，字母表中的前 K 个字母在网格中都有自己对应的一个小写和一个大写字母。
换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。

返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。
示例 1：

输入：["@.a.#","###.#","b.A.B"]
输出：8
示例 2：

输入：["@..aA","..B#.","....b"]
输出：6
 
提示：

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F'
钥匙的数目范围是 [1, 6]，每个钥匙都对应一个不同的字母，正好打开一个对应的锁。


这和普通的bfs有什么不同呢，现在给出一个具体实例["@...a",".###A","b.BCc"]，
你会发现这里要走回头路的，那么如果凭空就可以来回走的话，会是一个死循环，但我们稍微仔细思考一下，
走回头路的条件是获得一个新key这个点应该不难想到，只需要将标准bfs写法中的visited中key值变为(i,j,key)即可
"""

import collections

class Solution(object):
    def shortestPathAllKeys(self, grid):
        n, m = len(grid), len(grid[0])
        numOfKeys = 0
        direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        starti,startj = 0,0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    starti,startj = i,j
                elif grid[i][j] in "abcdef":
                    numOfKeys += 1

        deque = collections.deque()
        deque.append([starti, startj, 0, ".@abcdef", 0])

        while deque:
            i, j, steps, keys, collectedKeys = deque.popleft()

            if grid[i][j] in "abcdef" and grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                collectedKeys += 1

            if collectedKeys == numOfKeys:
                return steps

            for x, y in direc:
                ni = i + x
                nj = j + y
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] in keys:
                    if (ni, nj, keys) not in visited:
                        visited.add((ni, nj, keys))
                        deque.append([ni, nj, steps + 1, keys, collectedKeys])
            print(deque)
        return -1


    # def shortestPathAllKeys(self, grid):
    #     """
    #     :type grid: List[str]
    #     :rtype: int
    #     """
    #     m, n = len(grid), len(grid[0])
    #     queue = []
    #     key_cnt = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == '@':
    #                 queue.append([i, j, 0, 0, set()])
    #             if 'a' <= grid[i][j] <= 'f':
    #                 key_cnt += 1
    #     visited = []
    #     ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #     while queue:
    #         i, j, key_count, step, keys = queue.pop(0)
    #         # print(i,j,step,keys)
    #         # print(step,'aaaaaaaaaaaaaa')
    #         if len(keys) == key_cnt:
    #             return step
    #         # print(i,j,key_cnt,key_count,keys)
    #         for dx, dy in ds:
    #             x = i + dx
    #             y = j + dy
    #             if 0 <= x < m and 0 <= y < n and not (x, y, keys) in visited:
    #                 if grid[x][y] == '.' or grid[x][y] == '@':
    #                     visited.append((i, j, keys))
    #                     queue.append([x, y, key_count, step + 1, keys])
    #                     print('=============',queue)
    #                 if 'a' <= grid[x][y] <= 'f':
    #                     # if grid[x][y]=='b':
    #                     #     print(keys)
    #                     visited.append((i, j, keys))
    #                     # print(visited, keys)
    #                     if grid[x][y] not in keys:
    #                         keys.add(grid[x][y])
    #                         queue.append([x, y, key_count + 1, step + 1, keys])
    #                     else:
    #                         queue.append([x, y, key_count, step + 1, keys])
    #                     print('----------',x,y,step,key_cnt,key_count,keys)
    #
    #                 if 'A' <= grid[x][y] <= 'F' and grid[x][y].lower() in keys:
    #                     visited.append((i, j, keys))
    #                     queue.append([x, y, key_count, step + 1, keys])
    #                 # print(x,y)
    #         print(queue)
    #     return -1

grid = ["@...a",
        ".###A",
        "b.BCc"]
s = Solution()
print(s.shortestPathAllKeys(grid))
