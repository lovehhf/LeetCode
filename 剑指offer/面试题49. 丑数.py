# -*- coding:utf-8 -*-

"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:  
1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        uglys = [0] * 1700
        uglys[0] = 1
        for i in range(1, n):
            # 下一个丑数的值
            nu = min(uglys[i2] * 2, uglys[i3] * 3, uglys[i5] * 5)
            uglys[i] = nu
            if (nu == uglys[i2] * 2):
                i2 += 1
            if (nu == uglys[i3] * 3):
                i3 += 1
            if (nu == uglys[i5] * 5):
                i5 += 1
        return uglys[n - 1]
