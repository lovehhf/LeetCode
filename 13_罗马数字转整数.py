# -*- coding:utf-8 -*-

__author__ = 'huanghf'

import re

def romanToInt(s):
    result = 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in range(0,len(s)):
        if i<len(s)-1 and roman_dict[s[i]]<roman_dict[s[i+1]]:
            result -= roman_dict[s[i]]
        else:
            result += roman_dict[s[i]]
    return result


    # result = 0
    #
    # temp_dict = {
    #     'IV':4,
    #     'IX':9,
    #     'XL':40,
    #     'XC':90,
    #     'CD':400,
    #     'CM':900
    # }
    # for key,value in temp_dict.items():
    #
    #     if re.findall(key,s):
    #         # print(key, value)
    #         result += value*len(re.findall(key,s))
    #         s = re.sub(key,'',s)
    #
    # # print(result)
    # roman_dict = {
    #     'I': 1,
    #     'V': 5,
    #     'X': 10,
    #     'L': 50,
    #     'C': 100,
    #     'D': 500,
    #     'M': 1000
    # }
    # result += sum([roman_dict[x] for x in list(s)])
    # return result


print(romanToInt("MCMXCIV"))