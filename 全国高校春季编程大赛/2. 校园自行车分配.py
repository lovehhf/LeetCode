# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在由 2D 网格表示的校园里有 n 位工人（worker）和 m 辆自行车（bike），n <= m。所有工人和自行车的位置都用网格上的 2D 坐标表示。

我们需要为每位工人分配一辆自行车。在所有可用的自行车和工人中，我们选取彼此之间曼哈顿距离最短的工人自行车对  (worker, bike) ，并将其中的自行车分配給工人。如果有多个 (worker, bike) 对之间的曼哈顿距离相同，那么我们选择工人索引最小的那对。类似地，如果有多种不同的分配方法，则选择自行车索引最小的一对。不断重复这一过程，直到所有工人都分配到自行车为止。

给定两点 p1 和 p2 之间的曼哈顿距离为 Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|。

返回长度为 n 的向量 ans，其中 a[i] 是第 i 位工人分配到的自行车的索引（从 0 开始）。

 

示例 1：



输入：workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
输出：[1,0]
解释：
工人 1 分配到自行车 0，因为他们最接近且不存在冲突，工人 0 分配到自行车 1 。所以输出是 [1,0]。
示例 2：



输入：workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
输出：[0,2,1]
解释：
工人 0 首先分配到自行车 0 。工人 1 和工人 2 与自行车 2 距离相同，因此工人 1 分配到自行车 2，工人 2 将分配到自行车 1 。因此输出为 [0,2,1]。
 

提示：

0 <= workers[i][j], bikes[i][j] < 1000
所有工人和自行车的位置都不相同。
1 <= workers.length <= bikes.length <= 1000
"""


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """

        ans = [-1] * len(workers)
        record = dict()
        for b, bike in enumerate(bikes):
            xb, yb = bike[0], bike[1]

            for w, worker in enumerate(workers):
                xw, yw = worker[0], worker[1]
                distance = abs(xb - xw) + abs(yb - yw)

                if distance in record:
                    record[distance].append([b, w])
                else:
                    record[distance] = [[b, w]]

        usedbike, usedworker = [0] * len(bikes), [0] * len(workers)
        while (record):
            key = min(record.keys())
            pairs = record[key]

            for pair in pairs:
                bikeid, workerid = pair[0], pair[1]
                if usedbike[bikeid] or usedworker[workerid]:
                    continue

                if ans[workerid] == -1:
                    ans[workerid] = bikeid

                    usedbike[bikeid] = 1
                    usedworker[workerid] = 1

            record.pop(key)

        return ans

    def assignBikes2(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        def get_manhattan(p1,p2):
            manhattan = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
            return manhattan
        W = []
        for i in workers:
            manhattans = []
            for j in bikes:
                manhattans.append(get_manhattan(i,j))
            W.append(manhattans)
        res = [0]*len(workers)
        count = 0


workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
s = Solution()
print(s.assignBikes(workers,bikes))