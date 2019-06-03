# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。
例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

示例 1:

输入: dict(词典) = ["cat", "bat", "rat"]
sentence(句子) = "the cattle was rattled by the battery"
输出: "the cat was rat by the bat"
注:

输入只包含小写字母。
1 <= 字典单词数 <=1000
1 <=  句中词语数 <= 1000
1 <= 词根长度 <= 100
1 <= 句中词语长度 <= 1000
"""


class Solution(object):
    def replaceWords(self, d, s):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        s = s.split()
        d = sorted(d,key=lambda x:len(x))
        m,n = len(s),len(d)
        for i in range(m):
            for j in range(n):
               if s[i].startswith(d[j]):
                    s[i] = d[j]
                    break
        return ' '.join(s)

d = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
s = Solution()
print(s.replaceWords(d,sentence))