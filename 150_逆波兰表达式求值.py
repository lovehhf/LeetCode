# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
根据逆波兰表示法，求表达式的值。
https://baike.baidu.com/item/%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F/128437

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        后缀表达式
        a+b = ab+
        a+b+c = ab+c+
        (a+b)*c = ab+c*
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                r = stack.pop()
                l = stack.pop()
                # 除法时不能用// -6//132=-1 应用int转换
                stack.append(str(int(eval(l+i+r))))
        return int(stack[0])



tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s = Solution()
print(s.evalRPN(tokens))