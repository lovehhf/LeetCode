# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
爱丽丝有一手（hand）由整数数组给定的牌。 
现在她想把牌重新排列成组，使得每个组的大小都是 W，且**由 W 张连续的牌**组成。
如果她可以完成分组就返回 true，否则返回 false。

示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
输出：true
解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
示例 2：

输入：hand = [1,2,3,4,5], W = 4
输出：false
解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。
 
提示：

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if n % W:
            return False
        hand.sort()
        while hand:
            j = hand[0]
            t = [j]
            for i in range(W - 1):
                if j + 1 in hand:
                    j = j + 1
                    t.append(j)
                else:
                    return False
            for i in t:
                hand.remove(i)
        return True


s = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
W = 3
print(s.isNStraightHand(hand, W))
