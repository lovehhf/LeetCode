# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：

"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。

 

示例 1：

输入："GGLLGG"
输出：true
解释：
机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
重复这些指令，机器人将保持在以原点为中心，2 为半径的环中进行移动。
示例 2：

输入："GG"
输出：false
解释：
机器人无限向北移动。
示例 3：

输入："GL"
输出：true
解释：
机器人按 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ... 进行移动
"""


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        如果机器人运动轨迹为环
        那么重复4次指令后肯定会回到原点 否则会越走越远
        :type instructions: str
        :rtype: bool
        """
        d = (0, 1)
        now = (0, 0)
        instructions = instructions * 4
        for i in range(len(instructions)):
            if instructions[i] == 'G':
                now = (now[0] + d[0], now[1] + d[1])
            elif instructions[i] == 'R':
                # 0,1->-1,0->0,-1->1,0
                d = (-d[1], d[0])
            else:
                # 0,1->1,0->0,-1->-1,0
                d = (d[1], -d[0])
        return now == (0, 0)


s = Solution()
instructions = "RRGRRGLLLRLGGLGLLGRLRLGLRLRRGLGGLLRRRLRLRLLGRGLGRRRGRLG"
print(s.isRobotBounded(instructions))
