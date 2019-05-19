# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出一个单词列表，其中每个单词都由小写英文字母组成。
如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。
词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。
从给定单词列表 words 中选择单词组成词链，返回词链的**最长可能长度**。
 

示例：

输入：["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 "a","ba","bda","bdca"。
dp[0]=1
dp[1]=1
dp[2]=2 = max(dp[0],dp[1])+1
dp[3]=3 = dp[2]+1
...

提示：
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] 仅由小写英文字母组成。
"""


class Solution(object):
    def check(self, word1, word2):
        for i in range(len(word2)):
            for j in [chr(ord('a') + x) for x in range(26)]:
                if word1[:i] + j + word1[i:] == word2:
                    return True
        return False

    def longestStrChain3(self, words):
        """
        超时
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        words = sorted(words, key=lambda x: len(x))
        n = len(words)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if len(words[i]) - len(words[j]) == 1 and self.check(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def longestStrChain2(self, words):
        """
        多过了一些测试样例
        超时+1
        :param words:
        :return:
        """
        d1 = {x: 1 for x in words}   # d1存储 某个字母为队尾的词链
        d2 = {x: [] for x in range(20)} # d2键：长度 值:某个长度的所有字母
        for word in words:
            d2[len(word)].append(word)
        for i in range(1, 17):
            if not d2[i]:
                continue
            for word in d2[i]:
                for l in range(len(word) + 1):
                    for j in [chr(ord('a') + x) for x in range(26)]:
                        t = word[:l] + j + word[l:]
                        if t in d2[i + 1]:
                            d1[t] = max(d1[t], d1[word] + 1)
        # for word in sorted(words, key=lambda x: len(x)):
        #     print(word, d1[word])
        # print(d1)
        res = max(d1.values())
        return res

    def longestStrChain(self, words):
        """
        改进了一下上面的代码,判断d[i]某字母减掉一个字符是否在字典里面比上面的加字母遍历速度快
        :param words:
        :return:
        """
        d1 = {x: 1 for x in words}
        d2 = {x: [] for x in range(20)}
        for word in words:
            d2[len(word)].append(word)
        for i in range(1, 17):
            if not d2[i]:
                continue
            for word in d2[i]:
                for j in range(i):
                    t = word[:j] + word[j + 1:]
                    if t in d2[i - 1]:
                        d1[word] = max(d1[word], d1[t] + 1)
        res = max(d1.values())
        return res


words = ["yaifvhymztm", "ypwmqksl", "prpsmcjf", "gfek", "nmuyseumwa", "gxlureiyhbtey", "qocrjrymrqfep", "yisn",
         "cdyrfurhlizhvycg", "wjpvg", "iwotyxmjggqfhz", "acuxrapngm", "aep", "yfvhytm", "gwoewspcpqv", "wwela",
         "bippwujllph", "aanexmrwp", "iwoyxmgqfz", "prpsemcdjf", "gyysilxsn", "m", "gsxlureliyhbtey", "qorjrymrqfe",
         "odcmohm", "qaqzkbijdfuurck", "qaqzkbijduurck", "yywjaxqrgwul", "qqzkbjduurk", "bb", "xhjinzjii", "tnqazxzm",
         "cpoteplnoigdz", "nllybjzdsfc", "uoqfyi", "qprpsnemcdjf", "egtyysxoilxssen", "aexmrwp", "gjoferklo", "hl",
         "uo", "gferklo", "awjpxvg", "ozohil", "iwoyxmgqf", "sjag", "mhodcamzmohwm", "akxbxqrkmwq", "njzsfc", "gbkkc",
         "xmzwuzgsb", "iyeaexvckuqxm", "rwiv", "jgmfiqx", "ypw", "eawjpxhxjvwg", "hj", "ibbd", "orjrymrqe",
         "axkxbxzqrkmwbqg", "aexrp", "octgrbziicpe", "akxbxqmwq", "wwesla", "gferk", "iwoyxmjggqfz", "el",
         "eawjpxxjvwg", "uoqfi", "mxouywukd", "yaifvhymztmz", "xxgskevdgc", "acuxraqpngam", "crat", "mgjqtwnsxu",
         "acuxrtaqpngam", "gyilsn", "uuodqfyi", "hs", "gbkkcf", "octgrxbcziicpe", "xhjinzi", "frilbrbud", "ibb",
         "coteplnoigdz", "iwoyxmjgqfz", "octgrbcziicpe", "acxrapnm", "anexmrwp", "a", "pwujlph", "xmzwtukzgsb",
         "cdamlgjwwsv", "ymuqurtoodm", "axkxbxzqrkmrwbqg", "acuxraqpngm", "bkc", "nuyseumwa", "nlybjzdsfc", "wela",
         "yywjazxqrgwul", "crgat", "xxbgskevdgc", "frilbrobud", "iwoxmgqf", "gmfiqx", "gjolfeirkctlo", "fsw", "wjaxqgw",
         "eawjpxvg", "odcazmohm", "mxouyuk", "qzkbdurk", "woewppqv", "axrapm", "ocmohm", "qaqzkbfijdfuurck",
         "axkxbxqrkmwq", "ywjaxqrgwl", "fsyww", "cdamclhgjwwsv", "maxouyvxwufkd", "gjofeirkctlo", "gbkc", "yw",
         "qshwgrhqqutovx", "ywjaxqrgwul", "gtyysoilxsen", "ygaifvhymztmz", "yjpdwmqksl", "mhodcahmzmochwm",
         "gjrdooilxct", "wjaxqgwl", "nllybbjzdsflc", "ayorjsgudtgh", "girlzzbngiia", "xgevc", "akxbxmwq", "orjrymrqfe",
         "qozrokhil", "maxouyxwukd", "woeppqv", "prpsmcdjf", "jwzonpcz", "gferkl", "cdyrfurhlzhvycg", "oqi", "pwulph",
         "fribrbud", "npllybbjzdsflc", "gyysilsn", "tnqlwriayzxzm", "rwi", "i", "w", "ymuqurtooodm", "xmzwukzgsb",
         "iyeaxvckuqm", "uuozirdqfyi", "gyysilxsen", "bipwujllph", "xmzfwtoukzgvsb", "iwotygxmjggqfhz", "uuozrdqfyi",
         "nuysmw", "kbduk", "wjpv", "akxxmwq", "gamoepgip", "woepqv", "qqzkbduurk", "omhm", "gtyysilxsen", "qozrjokhil",
         "zoyhl", "nuyseumw", "qkbduk", "gwoewpcpqv", "qsqhwgrhqqutovx", "ypwmk", "yn", "zmgjqtwnsxu", "sjuag",
         "ypdwmqksl", "mhodcazmohm", "gyyilsn", "gjrdooixct", "eaqwjpxhxpujvwg", "yin", "fuuozirdqfyi", "acuxrapnm",
         "mhodcamzmochwm", "eawjpxhxujvwg", "ri", "bpwujllph", "ibbud", "hil", "ygaifvhcymztmz", "xev", "coteploidz",
         "wjaxqrgwl", "anhss", "qocrjrymrqfe", "xxbgskeovdgc", "ribrbud", "tnqlayzxzm", "qqzkbdurk", "eawjpxvwg",
         "yafvhytm", "fmyrgkvvlplcp", "iyeaxvckuqxm", "hqprpsnemcdjf", "aexrwp", "prpsmjf", "ozrohil", "omgf",
         "jwzbonpcz", "mhodcazmohwm", "hjini", "eawjpxjvwg", "nuysw", "ohil", "akxxmq", "goferklo", "cpoteplnoitgdz",
         "ela", "xgkevdgc", "uorrq", "yilsn", "njzdsfc", "fw", "axkxbxqrkmwbq", "ae", "coteploigdz", "anhsso", "ypwk",
         "ypwmqks", "gjofeirktlo", "xhjinzji", "gtyysxoilxsen", "yl", "nllybbjzdsfc", "qaqzkbijduurk", "aerp", "omgqf",
         "ayogrjsdgudtgh", "oqfi", "fuuozirdqfpyi", "gamoegip", "vmaxouyvxwufkd", "fsyw", "yfvhtm", "bu",
         "eaqwjpxhxujvwg", "fek", "nuysemw", "yaifvhymtm", "bpwujlph", "wwezsla", "coteplodz", "xjzpkpeaf",
         "hodcazmohm", "uuoqfyi", "woewpcpqv", "oohil", "kbu", "gsxlureiyhbtey", "ioxmgqf", "uor", "nljzdsfc", "ypwmks",
         "xhgjinzjii", "cdamlhgjwwsv", "kbuk", "iyefaexvckuqxm", "xgev", "umorrq", "gtyysxoilxssen", "njzsf",
         "xmzwtoukzgsb", "mxouyxwukd", "gwoewmspcpqv", "gmiqx", "l", "xmzfwtoukzagvsb", "xgevgc", "axkxbxzqrkmwbq",
         "iwotyxmjggqfz", "iomgqf", "oyl", "wjpxvg", "hss", "hjni", "qqzkbijduurk", "tnqlrayzxzm", "uorq", "prpsmj",
         "qkbdurk", "gwoewbmspcpqv", "mxouyukd", "gjofeirklo", "omohm", "mgf", "odczmohm", "crgagt", "nlyjzdsfc",
         "ayorjsdgudtgh", "xgevdgc", "xhjini", "uuordqfyi", "xxgkevdgc", "zoyl", "nhss", "tnqlazxzm", "ribbud",
         "akxbxqkmwq", "hji", "ozrokhil", "qprpsemcdjf", "maxouyvxwukd", "tnqlriayzxzm", "xmzfwtoukzgsb", "yafvhymtm",
         "njsf", "octgtrxbcziicpe", "acxrapm", "girzlzzbngiia"]
s = Solution()
print(s.longestStrChain(words))
print(s.longestStrChain2(words))
