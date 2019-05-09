# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

class Solution(object):
    def isValid(self, s):
        """
        常规做法:
        遍历一遍s
        碰到左括号入栈，碰到右括号弹出栈顶元素并与之对比
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i == ')':
                if not stack or stack.pop()!='(':
                    return False
            elif i == ']':
                if not stack or stack.pop()!='[':
                    return False
            elif i == '}':
                if not stack or stack.pop()!='{':
                    return False
        return not stack

    def isValid2(self, s):
        """
        取巧做法
        :type s: str
        :rtype: bool
        """
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()','')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return not s

sol = Solution()
print(sol.isValid2("()[]{}"))


# def isValid(s):
#     stack = []
#     a =  {")": "(", "}": "{", "]": "["}
#
#     for char in s:
#         if char in a.values():
#             stack.append(char)  # 左括号添加到栈上
#         else:
#             if stack:
#                 top_element = stack.pop()   # 弹出栈顶元素并返回相应值
#                 if a[char] != top_element:  # 栈顶元素与值下一个字符要对应
#                     return False
#             else:
#                 return False
#     return not stack
