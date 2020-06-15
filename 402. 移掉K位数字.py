# -*- coding:utf-8 -*-

"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:
num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。

示例 1 :
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。

示例 2 :
输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

示例 3 :
输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。

链接：https://leetcode-cn.com/problems/remove-k-digits

贪心, 分两种情况讨论,
1. 字符串严格单调非减: 删除最后一个数
2. 存在 i 使得 s[i] > s[i + 1], 删除最前面的 > s[i + 1] 的 i
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = ['0']
        n = len(num)

        for i in range(n):
            while k > 0 and res[-1] > num[i]:
                res.pop()
                k -= 1
            res.append(num[i])

        res = res[:len(res) - k]
        res = ''.join(res).lstrip('0')
        return res if res else '0'
