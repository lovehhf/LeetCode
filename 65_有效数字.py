# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        先去除行首和行尾空格；
        行首如果有一个正负号，直接忽略；
        如果字符串为空或只有一个'.'，则不是一个合法数；
        循环整个字符串，去掉以下几种情况：
        (1) '.'或'e'多于1个;
        (2) '.'在'e'后面出现；
        (3) 'e'后面或前面为空，或者'e'前面紧跟着'.'；
        (4) 'e'后面紧跟着正负号，但正负号后面为空；
        剩下的情况都合法；
        :param s:
        :return:
        """
        s = s.strip()  # 去空格
        if not s:  # 字符串为空
            return False
        if s[0] in '+-':
            s = s[1:]
        if len(s) == 1:
            if s[0] not in '0123456789':
                return False
            return True
        n = len(s)
        count_dot, count_e = 0, 0
        for i in range(n):
            if s[i] in '0123456789.+-e':
                if s[i] == 'e':
                    count_e += 1
                    if count_e > 1:  # e出现次数大于一次
                        return False
                    if i == 0 or i == n - 1:  # e出现在第一位或者最后一位
                        return False
                    if s[i - 1] not in '0123456789.':  # e前面的字符不是数字或.
                        return False
                    if s[i - 1] == '.' and i == 1:   # .e
                        return False
                    if s[i + 1] not in '0123456789+-':   # e后面的字符是数字或者+-
                        return False
                    if s[i + 1] in '+-' and i == n - 2:  # e后面的字符是+- 但是+-在最后一位
                        return False
                if s[i] == '.':
                    count_dot += 1
                    if count_e or count_dot > 1:  # .出现的次数大于一次 或前面出现了e
                        return False
                if s[i] in '+-':
                    if i == 0:
                        return False
                    if s[i - 1] != 'e':
                        return False
            else:
                return False
        return True

    def isNumber2(self, s: str) -> bool:
        import re
        return True if re.match(r'^\s*[+-]?(\d+\.?|\d*\.\d+)(e[+-]?\d+)?\s*$', s) else False

    def isNumber3(self, s: str) -> bool:
        try:
            float(s)
        except Exception:
            return False
        else:
            return True


s = '-1.e+6'
sol = Solution()
print(sol.isNumber(s))
