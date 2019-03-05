# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def isValid(s):
    stack = []
    a =  {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in a.values():
            stack.append(char)  # 左括号添加到栈上
        else:
            if stack:
                top_element = stack.pop()   # 弹出栈顶元素并返回相应值
                if a[char] != top_element:  # 栈顶元素与值下一个字符要对应
                    return False
            else:
                return False
        # print(stack)
    return not stack
    # for i in s:
    #     # print(i)
    #     if i in a.keys():
    #         if
    #
    #         top_element = stack.pop() if stack else '#'
    #         # print(top_element)
    #         if a[i]!=top_element:
    #             return False
    #     else:
    #         # print(i)
    #         stack.append(i)
    # return not stack

print(isValid("()[]{}"))