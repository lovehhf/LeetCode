# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。



例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

案例:

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 

注意事项:

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
"""


class Solution(object):
    def __init__(self):
        self.h = [1, 2, 4, 8]
        self.m = [1, 2, 4, 8, 16, 32]
        self.res = []

    def dfs_h(self, index, k, path, hres):
        """
        dfs时针
        :param index: 当前搜索到的索引
        :param k: 时针亮着的数量
        :param path:
        :param hres: 亮着k根时针是时针结果所有可能
        :return:
        """
        if k == 0 and 0 <= path < 12:
            hres.append(str(path))
            return
        for i in range(4):
            if i >= index:
                self.dfs_h(i + 1, k - 1, path + self.h[i], hres)

    def dfs_m(self, index, k, path, mres):
        """
        :param index: 当前搜索到的索引
        :param k: 分针亮着的数量
        :param path: 路径
        :param mres: 分针组合的所有可能
        :return:
        """
        if k == 0 and 0 <= path < 60:
            mres.append(str(path).rjust(2, '0'))
        for i in range(6):
            if i >= index:
                self.dfs_m(i + 1, k - 1, path + self.m[i], mres)

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # hres, mres = [], []
        # self.dfs_h(0, 3, 0, hres)
        # self.dfs_m(0, 3, 0, mres)
        # print(hres)
        # print(mres)
        # i: 时针亮着的数量 j: 分针亮着的数量
        for i in range(4):
            hres, mres = [], []
            j = num - i
            if i > num:
                break
            print(i, j)
            self.dfs_h(0, i, 0, hres)
            self.dfs_m(0, j, 0, mres)
            for x in hres:
                for y in mres:
                    self.res.append('%s:%s' % (x, y))
        return self.res

    def readBinaryWatch2(self, num):
        """
        直接暴力 从0:00-11:59 直接判断小时位出现的1个数+分秒位出现的1个数
        就是在二进制手表中，每一个时间数都会被唯一表示
        :type num: int
        :rtype: List[str]
        """

        def count1(n):
            # 下面是使用位运算统计1的格式
            # res = 0
            # while n:
            #     n &= n-1
            #     res += 1
            # return res
            return bin(n).count('1')

        res = []
        for i in range(0, 12):
            for j in range(60):
                if count1(i) + count1(j) == num:
                    res.append('%s:%s' % (str(i), str(j).rjust(2, '0')))
        return res


n = 3
s = Solution()
print(s.readBinaryWatch2(n))
