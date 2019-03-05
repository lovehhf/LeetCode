# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def longestCommonPrefix(strs):
    s = ''
    # min_len = min(list(map(len,strs)))
    from functools import reduce

    def find(x,y):
        s = ''
        # print(x,y)
        for i in range(min(len(x),len(y))):
            if x[i]==y[i]:
                s+=x[i]
                # print(s)
            else:
                break
        return s


    if strs:
        result = ''.join(list(reduce(find, strs)))
    else:
        result = ''
    return result

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))