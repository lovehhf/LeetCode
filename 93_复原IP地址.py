# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

"""


class Solution(object):
    def dfs(self, s, k, path, res):
        if k == 4 and not s:
            res.append('.'.join(path))
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.dfs(s[i:], k + 1, path + [s[:i]], res)
                if i == 2 and s[0] != '0':
                    self.dfs(s[i:], k + 1, path + [s[:i]], res)
                if i == 3 and s[0] != '0' and int(s[:i]) <= 255:
                    self.dfs(s[i:], k + 1, path + [s[:i]], res)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        res = []
        self.dfs(s, 0, [], res)
        return res

    # def isvalid(self, s):
    #     if len(s) == 0 or len(s) > 3 or (s[0] == '0' and len(s) > 1) or int(s) > 255:
    #         return False
    #     return True
    #
    # def restoreIpAddresses2(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #     ans = []
    #     self.back_(ans, "", s, 0)
    #     return ans
    #
    # def back_(self, ans, path, s, index):
    #     if index == 4:
    #         if not len(s):
    #             ans.append(path[:-1])
    #         return
    #     for i in range(1, 4):
    #         if self.isvalid(s[:i]) and len(s) >= i:
    #             # print(i,s[:i],path,s,index)
    #             self.back_(ans, path + s[:i] + '.', s[i:], index + 1)

    def restoreIpAddresses2(self, s):
        """
        回溯
        :type s: str
        :rtype: List[str]
        """

        # u表示枚举到的字符串下标，k表示当前截断的IP个数，s表示原字符串
        def dfs(u, k, s, res, path):
            if k == 4 and u == len(s):
                res.append('.'.join(path))
            if k > 4:
                return
            t = 0
            for i in range(u, len(s)):
                t = t * 10 + int(s[i])
                if t >= 0 and t < 256:
                    path.append(str(t))
                    dfs(i + 1, k + 1, s, res, path)
                    path.pop()
                if not t:
                    break

        res = []
        dfs(0, 0, s, res, [])
        return res


sol = Solution()
s = "25525511135"
print(sol.restoreIpAddresses2(s))
