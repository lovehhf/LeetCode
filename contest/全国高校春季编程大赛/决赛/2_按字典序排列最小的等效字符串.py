# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出长度相同的两个字符串：A 和 B，其中 A[i] 和 B[i] 是一组等价字符。举个例子，如果 A = "abc" 且 B = "cde"，
那么就有 'a' == 'c', 'b' == 'd', 'c' == 'e'。

等价字符遵循任何等价关系的一般规则：

- 自反性：'a' == 'a'
- 对称性：'a' == 'b' 则必定有 'b' == 'a'
- 传递性：'a' == 'b' 且 'b' == 'c' 就表明 'a' == 'c'

例如，A 和 B 的等价信息和之前的例子一样，那么 S = "eed", "acd" 或 "aab"，这三个字符串都是等价的，而 "aab" 是 S 的按字典序最小的等价字符串

利用 A 和 B 的等价信息，找出并返回 S 的按字典序排列最小的等价字符串。

 

示例 1：

输入：A = "parker", B = "morris", S = "parser"
输出："makkek"
解释：根据 A 和 B 中的等价信息，我们可以将这些字符分为 [m,p], [a,o], [k,r,s], [e,i] 共 4 组。每组中的字符都是等价的，并按字典序排列。所以答案是 "makkek"。
示例 2：

输入：A = "hello", B = "world", S = "hold"
输出："hdld"
解释：根据 A 和 B 中的等价信息，我们可以将这些字符分为 [h,w], [d,e,o], [l,r] 共 3 组。所以只有 S 中的第二个字符 'o' 变成 'd'，最后答案为 "hdld"。
示例 3：

输入：A = "leetcode", B = "programs", S = "sourcecode"
输出："aauaaaaada"
解释：我们可以把 A 和 B 中的等价字符分为 [a,o,e,r,s,c], [l,p], [g,t] 和 [d,m] 共 4 组，因此 S 中除了 'u' 和 'd' 之外的所有字母都转化成了 'a'，最后答案为 "aauaaaaada"。
 

提示：

字符串 A，B 和 S 仅有从 'a' 到 'z' 的小写英文字母组成。
字符串 A，B 和 S 的长度在 1 到 1000 之间。
字符串 A 和 B 长度相同。
"""


class Solution(object):
    def smallestEquivalentString(self, A, B, S):
        """
        :type A: str
        :type B: str
        :type S: str
        :rtype: str
        """
        l = []
        l2 = []
        n = len(A)
        for i in range(n):
            a, b = A[i], B[i]
            if a in l2 and b in l2:
                j = 0
                while j < len(l):
                    if a in l[j] and b in l[j]:
                        break
                    if a in l[j] and not b in l[j]:
                        k = j + 1
                        while k < len(l):
                            if b in l[k]:
                                t = l[j] + l[k]
                                # 由于 k在j后面 所以要先pop(k),不然k的index会减1
                                l.pop(k)
                                l.pop(j)
                                l.append(t)
                                break
                            k += 1
                    if not a in l[j] and b in l[j]:
                        k = j + 1
                        while k < len(l):
                            if a in l[k]:
                                t = l[j] + l[k]
                                l.pop(k)
                                l.pop(j)
                                l.append(t)
                                break
                            k += 1
                    j += 1

            elif a in l2 and not b in l2:
                l2.append(b)
                for j in range(len(l)):
                    if a in l[j]:
                        l[j].append(b)
                        break
            elif not a in l2 and b in l2:
                l2.append(a)
                for j in range(len(l)):
                    if b in l[j]:
                        l[j].append(a)
                        break
            else:
                if not a == b:
                    l.append([a, b])
                    l2.append(a)
                    l2.append(b)
                else:
                    l.append([a])
                    l2.append(a)

        res = ''
        l = [sorted(set(x)) for x in l]
        for i in S:
            find_j = False
            for j in l:
                if i in j:
                    find_j = True
                    res += j[0]
                    break
            if not find_j:
                res += i
        return res


A = "gmerjboftfnqseogigpdnlocmmhskigdtednfnjtlcrdpcjkbj"
B = "fnnafafhqkitbcdlkpiloiienikjiikdfcafisejgeldprcmhd"

S = "ezrqfyguivmybqcsvibuvtajdvamcdjpmgcbvieegpyzdcypcx"

s = Solution()
print(s.smallestEquivalentString(A, B, S))
