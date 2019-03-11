# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def addBinary(a, b):
    int_a = int(a, 2)
    int_b = int(b, 2)
    result = str(bin(int_a + int_b))[2:]
    return result


a = "1010"
b = "1011"
print(addBinary(a,b))