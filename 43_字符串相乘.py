# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
123
 45
-----
   15
  10
  5
-----
  12
  8
 4
-----
05535

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"
        m, n = len(num1), len(num2)
        # d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        res = [0 for _ in range(m + n)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # x, y = d[num1[i]], d[num2[j]]
                x, y = ord(num1[i]) - ord('0'), ord(num2[j]) - ord('0')
                res[i + j + 1] += x * y % 10
                res[i + j] += x * y // 10  # 进位
        # print(res)
        # [8, 17, 26, 19, 10, 1] -> [9, 9, 8, 0, 0, 1]
        # 从后往前遍历, 处理进位
        for i in range(m + n - 1, 0, -1):
            carry = res[i] // 10
            # if carry:
            res[i] = res[i] % 10
            res[i - 1] += carry
        ans = ''.join([str(x) for x in res]).lstrip('0')
        return ans


num1 = '408'
num2 = '5'
s = Solution()
print(s.multiply(num1, num2))
