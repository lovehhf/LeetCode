# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。
1
11
121
1331

示例:

输入: 3
输出: [1,3,3,1]
"""

class Solution():
    def getRow(self,rowIndex):
        """
        递归
        :param rowIndex:
        :return:
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1]*(rowIndex+1)
        for i in range(1,rowIndex):
            res[i] = self.getRow(rowIndex-1)[i-1] + self.getRow(rowIndex-1)[i]
        return res

    def getRow2(self,rowIndex):
        """
        非递归
        打印出所有结果
        :param rowIndex:
        :return:
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [[1]*(x) for x in range(1,rowIndex+2)]
        for i in range(2,rowIndex+1):
            for j in range(1,len(res[i])-1):
                res[i][j] = res[i-1][j-1]+res[i-1][j]
        return res[-1]

    def getRow3(self,rowIndex):
        """
        杨辉三角的数学性质:第n行的m个数可表示为 C(n-1，m-1)，即为从n-1个不同元素中取m-1个元素的组合数
        :param rowIndex:
        :return:
        """
        if rowIndex==0:
            return [1]
        res = []
        i = j = 1
        h = rowIndex
        while i < rowIndex:
            res.append(h//j)
            h *= rowIndex-i
            j *= i + 1
            i += 1
        res.append(1)
        res.insert(0,1)
        return res


s = Solution()
print(s.getRow3(10))