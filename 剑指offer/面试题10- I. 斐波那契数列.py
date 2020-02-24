# -*- coding:utf-8 -*-

"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：1

示例 2：
输入：n = 5
输出：5

提示：
0 <= n <= 100
注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        for i in range(2, n + 1):
            f.append(f[i - 1] + f[i - 2])
        return f[n] % (10 ** 9 + 7)


class Solution_2:
    def fib(self, n: int) -> int:
        """
        f[n] 只与 f[n - 1], f[n - 2] 有关, 可以使用变量代替数组
        :param n:
        :return:
        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a % (10 ** 9 + 7)
