# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, 0, "", res)
        return res
    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return

        for i in range(1, 4):
            # print(s)
            # 选择的数字不应超过s的长度
            if i <= len(s):
                # 选择一位数字
                if i==1:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # 选择2位数字 首字母不能是0
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + s[:i] + '.', res)
                # 选择3位数字 首字母不能是0 且不能大于255
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)

sol = Solution()
s = "25525511135"
print(sol.restoreIpAddresses(s))

