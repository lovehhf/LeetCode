# -*- coding:utf-8 -*-

"""
给你一个字符串 s 和一个整数 k 。请你用 s 字符串中 所有字符 构造 k 个非空 回文串 。
如果你可以用 s 中所有字符构造 k 个回文字符串，那么请你返回 True ，否则返回 False 。

示例 1：
输入：s = "annabelle", k = 2
输出：true
解释：可以用 s 中所有字符构造 2 个回文字符串。
一些可行的构造方案包括："anna" + "elble"，"anbna" + "elle"，"anellena" + "b"

示例 2：
输入：s = "leetcode", k = 3
输出：false
解释：无法用 s 中所有字符构造 3 个回文串。

示例 3：
输入：s = "true", k = 4
输出：true
解释：唯一可行的方案是让 s 中每个字符单独构成一个字符串。

示例 4：
输入：s = "yzyzyzyzyzyzyzy", k = 2
输出：true
解释：你只需要将所有的 z 放在一个字符串中，所有的 y 放在另一个字符串中。那么两个字符串都是回文串。

示例 5：
输入：s = "cr", k = 7
输出：false
解释：我们没有足够的字符去构造 7 个回文串。

提示：
1 <= s.length <= 10^5
s 中所有字符都是小写英文字母。
1 <= k <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-k-palindrome-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

贪心,
统计有多少个落单的字母（出现次数为奇数）
因为这些字符在每个回文串中最多只能用一次。 如果 落单的单词数量 > k，那么肯定是无解的

可以构造的充要条件： 字母出现的次数为奇数的个数 <= k
"""
import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        c = collections.Counter(s)
        return sum(x & 1 for x in c.values()) <= k


s = "leetcode"
k = 3
sol = Solution()
print(sol.canConstruct(s, k))
