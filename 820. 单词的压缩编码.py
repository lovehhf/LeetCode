# -*- coding:utf-8 -*-

"""
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

示例：
输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。

提示：
1 <= words.length <= 2000
1 <= words[i].length <= 7
每个单词都是小写字母 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

题意:
如果一个单词是另一个单词的结尾, 那么这个单词就可以被压缩掉, 需要返回最后所有 没被压缩的单词长度+1 的和
"""

from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        goods = set(words)   # 转成集合, 去重
        res = 0

        for word in words:
            for i in range(1, len(word)):
                # 切片, 然后在集合里面暴力去掉以这个单词尾部的所有单词
                # set 删除元素 remove 在 set 当中没有的话会报错，而 discard 不会
                goods.discard(word[i:])

        # 统计剩下的单词的长度
        for word in goods:
            res += len(word) + 1

        return res
