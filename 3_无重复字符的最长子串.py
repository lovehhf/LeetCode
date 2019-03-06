# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def lengthOfLongestSubstring(s):
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            """
            所以if s[j] in st:是判断s[j]相同元素上次出现的位置，和i孰大孰小。
            如果i大，说明[i,j-1]中没有与s[j]相同的元素，起始位置仍取i；
            如果i小，则在[i,j-1]中有了与s[j]相同的元素，所以起始位置变为st[s[j]]+1，即[st[sj]+1,j]。
            """
            i = max(st[s[j]], i)    # i记录下最新的重复字符所在位置
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1
    return ans


    # a = ''
    # max_count = 0
    # count = 0
    # for char in s:
    #     if not (char in a):
    #         a += char
    #         count += 1
    #     else:
    #         if count > max_count:
    #             max_count = count
    #         index = a.index(char)    # 相同字符串在上一段字符串中的索引
    #         a = a[(index+1):] + char # 切出上一段字符串中索引后一位到当前字符作为初始字符串
    #         count = len(a)           # 初始串长度
    #         # print(index)
    # if count > max_count:
    #     max_count = count
    # return max_count


print(lengthOfLongestSubstring("aab"))
