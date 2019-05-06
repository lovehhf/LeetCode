# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

"""


class Solution(object):
    def jusitify(self, words, maxWidth):
        """
        单词左右对齐
        要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
        最后一行应为左对齐，且单词之间不插入额外的空格。
        :param words:
        :param maxWidth:
        :return:
        """
        if len(words) == 1:
            return words[0].ljust(maxWidth, ' ')
        n = len(words) - 1  # 字符间隔,可以插入空格的地方
        s = maxWidth - len(''.join(words))  # 需要插入的空格数量
        a, b = s % n, s // n  # 左侧空格要比右侧多,余下的空格从左往右填写
        space = [b] * n
        for i in range(a):
            space[i] += 1
        # 开始填空格啦
        res = words[0]
        for i in range(n):
            res = res + ' ' * space[i] + words[i + 1]
        return res

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        c = 0  # 计算单词长度
        ls1, ls2 = [], []  # ls1存放所有单词,并按maxWidth分隔,ls2用来暂时存放长度还不到maxWidth的单词
        res = []

        # 贪心分配单词
        for word in words:
            c += len(word)
            print(word, c)
            if c == maxWidth:
                ls2.append(word)
                ls1.append(ls2)
                ls2, c = [], 0
                continue
            elif c < maxWidth:
                ls2.append(word)
                c += 1
            else:
                ls1.append(ls2)
                ls2 = [word]
                c = len(word) + 1
                # print(word,c)
        if ls2:
            ls1.append(ls2)

        for i in range(len(ls1) - 1):
            s = self.jusitify(ls1[i], maxWidth)
            res.append(s)

        res.append(' '.join(ls1[-1]).ljust(maxWidth, ' '))  # 最后一行左对齐
        print(ls1)
        return res


words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
         "is", "everything", "else", "we", "do"]
maxWidth = 20
s = Solution()
print(s.fullJustify(words, maxWidth))
