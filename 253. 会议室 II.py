

"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:
输入: [[0, 30],[5, 10],[15, 20]]
输出: 2

示例 2:
输入: [[7,10],[2,4]]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        统计同时进行的会议数量
        1. 把所有的开始时间和结束时间放在一起排序
        2. 用 cur 表示当前进行的会议数量，遍历排序后的时间数组
        3. 如果是开始时间, cur+1，如果是结束时间，cur-1 (如果出现(1, 10)(10, 20)这种两场连会议在一起的, 只需要 1 个会议室, 时间相同时所以结束时间排在前面)
        4. 在遍历的过程中, cur 出现的最大值就是需要的房间数
        """
        events = sorted([[x[0], 1] for x in intervals] + [[x[1], -1] for x in intervals])
        res = 0
        cur = 0
        for event in events:
            cur += event[1]
            res = max(res, cur)
        return res