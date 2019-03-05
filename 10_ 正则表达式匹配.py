# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def isMatch(self, s, p):
    import re
    value = re.match(p, s)
    if value == None or value.group(0) != s:
        return False
    else:
        return True