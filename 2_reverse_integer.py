# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def reverse(self, x):
    if ((x < (-2 ** 31)) or (x > (2 ** 31 - 1))):
        return 0
    else:
        str_x = str(x)
        list_x = list(str_x)
        result = 0
        if list_x[0] == '-':
            result = int('-' + ''.join((list(reversed(list_x[1:])))))
        else:
            result = int(''.join((list(reversed(str_x)))))
        if ((result < (-2 ** 31)) or (result > (2 ** 31 - 1))):
            return 0
        return result