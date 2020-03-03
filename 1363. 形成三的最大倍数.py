# -*- coding:utf-8 -*-


"""
给你一个整数数组 digits，你可以通过按任意顺序连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。
由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。
如果无法得到答案，请返回一个空字符串。

示例 1：
输入：digits = [8,1,9]
输出："981"

示例 2：
输入：digits = [8,6,7,1,0]
输出："8760"

示例 3：
输入：digits = [1]
输出：""

示例 4：
输入：digits = [0,0,0,0,0,0]
输出："0"

提示：
1 <= digits.length <= 10^4
0 <= digits[i] <= 9
返回的结果不应包含不必要的前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-multiple-of-three
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        digits.sort(reverse=True)
        s = sum(digits)
        n = len(digits)
        k = s % 3
        mod_1 = [x for x in digits if x % 3 == 1]
        mod_2 = [x for x in digits if x % 3 == 2]

        if k == 0:
            if (all(x == 0 for x in digits)):
                return "0"
            return "".join([str(x) for x in digits]).lstrip('0')
        elif k == 1:
            if len(mod_1) > 0:
                for i in range(n - 1, -1, -1):
                    if (digits[i] % 3) == k:
                        digits.pop(i)
                        break
            elif len(mod_2) > 1:
                j = 0
                for i in range(n - 1, -1, -1):
                    if (digits[i] % 3) == 2:
                        digits.pop(i)
                        j += 1
                    if j == 2:
                        break
            else:
                return ""
        else:
            if len(mod_2) > 0:
                for i in range(n - 1, -1, -1):
                    if (digits[i] % 3) == k:
                        digits.pop(i)
                        break
            elif len(mod_1) > 1:
                j = 0
                for i in range(n - 1, -1, -1):
                    if (digits[i] % 3) == 1:
                        digits.pop(i)
                        j += 1
                    if j == 2:
                        break
            else:
                return ""

        if not digits:
            return ""

        if (all(x == 0 for x in digits)):
            return "0"

        return "".join([str(x) for x in digits]).lstrip('0')
