# -*- coding:utf-8 -*-

"""
给你一个仅由数字 6 和 9 组成的正整数 num。
你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
请返回你可以得到的最大数字。

示例 1：
输入：num = 9669
输出：9969

示例 2：
输入：num = 9996
输出：9999

示例 3：
输入：num = 9999
输出：9999 

提示：
1 <= num <= 10^4
num 每一位上的数字都是 6 或者 9 。

思路:
将最高位的6换成9
做法一:
    转成字符串, 将最高位的6换成9, 再转回整数: return int(str(num).replace('6', '9', 1))
做法二:
    从右往左取模计算, 出现 6 num 就 +3*10^k 将这一位变成 9
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        res = num
        n = num
        t = 1
        while num // t > 0:
            if n % 10 == 6:
                # 这里没有必要用 res = max(res, num + t * 3)
                # 因为如果走到这一步的话, num + t * 3 一定是大于 res 的
                res = num + t * 3
            t *= 10
            n //= 10

        return res