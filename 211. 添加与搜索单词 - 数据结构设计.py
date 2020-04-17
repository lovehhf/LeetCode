# -*- coding:utf-8 -*-

"""
211. 添加与搜索单词 - 数据结构设计
链接：https://leetcode-cn.com/problems/add-and-search-word-data-structure-design

设计一个支持以下两种操作的数据结构：
void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

说明:
你可以假设所有单词都是由小写字母 a-z 组成的。

Trie树应用
"""


class Node(object):
    def __init__(self):
        self.son = [None] * 26
        self.is_end = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        p = self.root
        for char in word:
            idx = ord(char) - ord('a')

            if not p.son[idx]:
                node = Node()
                p.son[idx] = node

            p = p.son[idx]

        p.is_end = True

    def find(self, root, word):
        """
        查找 trie 树是否有该节点
        出现 . 就 dfs 搜索所有的非空子节点
        """
        p = root
        n = len(word)

        for i in range(n):
            if word[i] == '.':
                nodes = [x for x in p.son if x]
                return any(self.find(node, word[i + 1:]) for node in nodes)

            idx = ord(word[i]) - ord('a')
            if not p.son[idx]:
                return False
            p = p.son[idx]

        return p.is_end

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
