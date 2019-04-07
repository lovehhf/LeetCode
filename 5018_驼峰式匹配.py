# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

 

示例 1：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
示例 2：

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
示例 3：

输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输入：[false,true,false,false,false]
解释： 
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
 

提示：

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
所有字符串都仅由大写和小写英文字母组成。
"""


class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        import re

        if pattern[0] in [chr(ord('a') + x) for x in range(26)]:
            pattern1 = re.split(r'[A-Z]', pattern)
            pattern2 = re.findall("[A-Z][a-z]*", pattern)
            pattern = [pattern1[0]]+pattern2
        else:
            pattern = re.findall("[A-Z][a-z]*", pattern)
        # print(pattern)
        # for i in pattern:
        #     if i in
        tmp = ''
        for i in pattern:
            if len(i)<2:
                tmp += i+'[a-z]*'
            if len(i)>=2:
                tmp2 = ''
                for j in range(len(i)):
                    if i==0:
                        tmp2 += i[j]
                    else:
                        tmp2 += i[j] + '[a-z]*'
                tmp += tmp2
        pattern = tmp
        # if pattern[0] in [chr(ord('a') + x) for x in range(26)]:
        pattern = '[a-z]*' + pattern

        # print(pattern)
        # pattern = '[a-z]*'.join(pattern)+'[a-z]*'
        # print(pattern)
        # res = [bool(re.match(pattern,x)) for x in queries]
        res = []
        for query in queries:
            if re.match(pattern,query) and re.match(pattern,query).group(0)==query:
                res.append(True)
            else:
                res.append(False)
        return res

    def camelMatch2(self, queries, pattern: str):
        import string
        upper = string.ascii_uppercase
        def check(que, pat):
            a = ''.join(filter(lambda x:x in upper, que))
            b = ''.join(filter(lambda x:x in upper, pat))
            if a != b:
                return False
            for c in pat:
                if c not in que:return False
                i = que.index(c)
                que = que[i+1:]
            return True
        return [check(que,pattern) for que in queries]
    
# queries = ["uAxaqlzahfialcezsLfj","cAqlzyahaslccezssLfj","AqlezahjarflcezshLfj","AqlzofahaplcejuzsLfj","tAqlzahavslcezsLwzfj","AqlzahalcerrzsLpfonj","AqlzahalceaczdsosLfj","eAqlzbxahalcezelsLfj"]
# pattern = "AqlzahalcezsLfj"

queries = ["aksvbjLiknuTzqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"]
pattern = "ksvjLiknTzqn"

# queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# pattern = "FoBaT"
s = Solution()
print(s.camelMatch(queries, pattern))