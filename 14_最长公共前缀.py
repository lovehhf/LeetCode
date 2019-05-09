# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        常规方法一:
        找到最短长度 遍历所有strs看对应位置的字符是否相同
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        n = min(len(x) for x in strs)  # 最短字符的长度
        res = ''
        for i in range(n):
            char = strs[0][i]
            if all(char == s[i] for s in strs):
                res += char
            else:
                break
        return res

    def longestCommonPrefix2(self, strs):
        """
        常规方法二
        定义一个找到两个字符串的公共前缀的函数
        使用reduce找到所有字符的公共前缀
        :return:
        """
        from functools import reduce
        if not strs:
            return ''

        def find_common_pre(s1, s2):
            s = ''
            for i in range(min(len(s1), len(s2))):
                if s1[i] == s2[i]:
                    s += s1[i]
                else:
                    break
            return s

        return ''.join(list(reduce(find_common_pre, strs)))

    def longestCommonPrefix3(self, strs):
        """
        骚方法1
        使用zip*
        zip: 将多个一维列表左对齐压缩成一个二维列表
        zip*: 将二维列表左对齐压缩成一个新的二维列表
        zip* 会将所有字符串纵坐标对齐压缩到一个新的二维列表里面
        示例: ["flower", "flow", "flight"] -> [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        再用分别set对tuple内的元素去重,从左往右遍历如果set长度不为0则返回
        """
        res = ''
        z = [list(set(x)) for x in zip(*strs)]
        for i in z:
            if len(i) == 1:
                res += i[0]
            else:
                break
        return res

    def longestCommonPrefix4(self, strs):
        """
        骚方法2:
        使用min,max函数,取按ascii字符排序的最大的字符和最小字符比较
        只需要比较最大的和最小的公共前缀就是整个数组的公共前缀
        :param strs:
        :return:
        """
        if not strs:
            return ''
        s1 = min(strs)
        s2 = max(strs)
        res = ''
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                res += s1[i]
            else:
                break
        return res

s = Solution()
strs = ["flower", "flow", "flight"]
print(s.longestCommonPrefix(strs))
