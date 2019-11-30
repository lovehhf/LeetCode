# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定字符串 S，找出最长重复子串的长度。如果不存在重复子串就返回 0。

 

示例 1：

输入："abcd"
输出：0
解释：没有重复子串。
示例 2：

输入："abbaba"
输出：2
解释：最长的重复子串为 "ab" 和 "ba"，每个出现 2 次。
示例 3：

输入："aabcaabdaab"
输出：3
解释：最长的重复子串为 "aab"，出现 3 次。
示例 4：

输入："aaaaa"
输出：4
解释：最长的重复子串为 "aaaa"，出现 2 次。
 

提示：

字符串 S 仅包含从 'a' 到 'z' 的小写英文字母。
1 <= S.length <= 1500
"""


class Solution(object):
    def longestRepeatingSubstring(self, S):
        """

        :param S:
        :return:
        """
        res = 0
        n = len(S)
        for i in range(1, n):
            # i:跨度  2个需要比较的字符串之间的跨度
            # j:指针
            # cur: 计重复子串长度
            cur = 0
            for j in range(0, n - i):
                if S[j] == S[j + i]:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 0
        return res

    def longestRepeatingSubstring2(self, S):
        n = len(S)
        lcp = [[0] * (n + 1)] * (n + 1)
        res = 0
        i = n - 1
        while i > 0:
            for j in range(i + 1, n):
                if S[i] == S[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
                else:
                    lcp[i][j] = 0
                res = max(res, lcp[i][j])
            i -= 1
        return res

    def longestRepeatingSubstring3(self, S):
        """
        超时
        :type S: str
        :rtype: int
        """
        n = len(S)
        for i in range(1, n - 1):
            tmp = []
            for j in range(0, i + 1):
                if S[j:n - i + j] not in tmp:
                    tmp.append(S[j:n - i + j])
                else:
                    return len(S[j:n - i + j])
        return 0


S = "aabcaabdaab"
# S = "aaabaabaaaababaaaaaaaabaabaaabbbaaaabbbabbbaaaababbbababbbabaaabbaabaaabbaabbaaaabbbaaaabababbbbbaabbbabbaaabababbbbbbaabaaaabbbaaaaaabbbababbaabbbbaabaaabbababbbbabbbabbaabaaaaaabbabaabbbbbabaabababaabbabaaaabbbabbbbbabbaaaaabaababbbbabbaaaaaababbbbaabbbaabaaabaabbbbabbabaabaaaabaaabaaaaaabbbbabbbabbabaaabbbaaaaababaabaabbbbbababaaabbaaaabbbabababaabaabbababbbaaaaabbbabaabbbbbaaabbbaaaaaaabbbbbbbbabbaabbbabaaaabbbbabababababbabbbbbababaaaaababaabbabbbbaababaabbbbbabbbabbaaabbababaabbabbbbaaabaabbaaabbbababaabaaaaaabababaaababaaabaabaabaababaabbaaaaaabababbbabbaababbbababbabababbbabbababbbabbaaaabbbaaabbaababababaaaabbababbbbaaababababbabababbaaaaaabababbbabbabbbaabaaaaabbbbaabaababbbbbbbbbbbbaaaaaaababbbbbaaabaaaaaabaababaababaabaaabbbbaabbbaabbaaaaabaaabaaaababbaabaaaababbbaabbbabaabbaabbbbbabaaaaabaabbabaabbaaaabbababaaabaabbabbbaaaaaaababbbabaaaaaabbbaaabbbabaaabbaaaabbbaabaabbaaaaaaaaabababaaabbaabaaaaaaabbbbabbabbbbbbabbbbbbbaabbbaaaabbabbbbbaabaabbbbbbaabbabbabbaababbbaababbbaab"
s = Solution()
print(s.longestRepeatingSubstring(S))
