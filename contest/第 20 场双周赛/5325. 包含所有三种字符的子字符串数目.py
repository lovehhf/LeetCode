# -*- coding:utf-8 -*-

"""
给你一个字符串 s ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。

 

示例 1：
输入：s = "abcabc"
输出：10
解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。

示例 2：
输入：s = "aaacb"
输出：3
解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。

示例 3：
输入：s = "abc"
输出：1
 
提示：

3 <= s.length <= 5 x 10^4
s 只包含字符 a，b 和 c 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        双指针实现滑动窗口, 记录窗口内abc出现的次数
        j, i 窗口内满足条件的最短长度的字符串

        i往前走, 不满足要求时以 i 结尾的子字符串为 j + 1
        满足条件是 j 往前走, 直到再次不满足条件,
        :param s:
        :return:
        """
        n = len(s)
        abc = [0, 0, 0]
        i, j = 0, 0
        res = 0
        while (i < n):
            while (i < n and any(x == 0 for x in abc)):
                abc[ord(s[i]) - ord('a')] += 1
                if (any(x == 0 for x in abc)):
                    res += j
                i += 1
                # print(i, j, res, abc)
            if all(x > 0 for x in abc):
                while (j < i and all(x > 0 for x in abc)):
                    abc[ord(s[j]) - ord('a')] -= 1
                    j += 1
                res += j
                # print(i, j, res, abc)
        return res
