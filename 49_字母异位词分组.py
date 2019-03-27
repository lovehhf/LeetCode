# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        借助字典
        键:排序后的字符串 值:字母异位词列表
        :param strs:
        :return:
        """
        strs_dict = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key in strs_dict:
                strs_dict[key].append(item)
            else:
                strs_dict[key] = [item]
        return list(strs_dict.values())

    def groupAnagrams2(self, strs):
        """
        方法二
        :param strs:
        :return:
        """
        import collections

        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams2(strs))