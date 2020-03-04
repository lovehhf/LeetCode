# -*- coding:utf-8 -*-

"""
假设你是一个专业的狗仔，参加了一个 n 人派对，其中每个人被从 0 到 n - 1 标号。在这个派对人群当中可能存在一位 “名人”。所谓 “名人” 的定义是：其他所有 n - 1 个人都认识他/她，而他/她并不认识其他任何人。
现在你想要确认这个 “名人” 是谁，或者确定这里没有 “名人”。而你唯一能做的就是问诸如 “A 你好呀，请问你认不认识 B呀？” 的问题，以确定 A 是否认识 B。你需要在（渐近意义上）尽可能少的问题内来确定这位 “名人” 是谁（或者确定这里没有 “名人”）。
在本题中，你可以使用辅助函数 bool knows(a, b) 获取到 A 是否认识 B。请你来实现一个函数 int findCelebrity(n)。
派对最多只会有一个 “名人” 参加。若 “名人” 存在，请返回他/她的编号；若 “名人” 不存在，请返回 -1。

 

示例 1:
输入: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
输出: 1
解析: 有编号分别为 0、1 和 2 的三个人。graph[i][j] = 1 代表编号为 i 的人认识编号为 j 的人，而 graph[i][j] = 0 则代表编号为 i 的人不认识编号为 j 的人。“名人” 是编号 1 的人，因为 0 和 2 均认识他/她，但 1 不认识任何人。

示例 2:
输入: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
输出: -1
解析: 没有 “名人”

注意:
该有向图是以邻接矩阵的形式给出的，是一个 n × n 的矩阵， a[i][j] = 1 代表 i 与 j 认识，a[i][j] = 0 则代表 i 与 j 不认识。
请记住，您是无法直接访问邻接矩阵的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-celebrity
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

普通做法:
建图, 找入度为 n-1,出度为 0 的点: 超时

烧脑做法:
1. 如果 i 认识 j, i 一定不是名人, 如果 i 不认识 j, j 一定不认识名人
2. 双指针分别指向首尾, knows(i, j)=true, i 往右移, 否则j往左移, 最后一定可以排除到只剩下一个可疑的答案
3. 然后验证这个答案是否满足性质: 所有人都认识他, 但是他不认识所有人
"""



def knows(a, b):
    return graph[a][b]


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n - 1
        while (l < r):
            if (knows(l, r)):
                # l 认识 r, 淘汰掉 l
                l += 1
            else:
                # r 不认识 l, 淘汰掉 r
                r -= 1

        for i in range(n):
            if i != l and (not knows(i, l) or knows(l, i)):
                return -1

        return l

graph = [[1, 1, 0, 1],
         [0, 1, 0, 0],
         [1, 1, 1, 1],
         [1, 1, 0, 1]]

s = Solution()
print(s.findCelebrity(4))
