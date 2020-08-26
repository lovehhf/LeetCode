# -*- coding:utf-8 -*-

"""
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。
注意:

输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。

示例 1:
输入: "owoztneoer"
输出: "012" (zeroonetwo)

示例 2:
输入: "fviefuro"
输出: "45" (fourfive)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-original-digits-from-english
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import Counter

class Solution:

    def originalDigits(self, s: str) -> str:
        c0 = s.count('z')
        c2 = s.count('w')
        c4 = s.count('u')
        c6 = s.count('x')
        c8 = s.count('g')
        c7 = s.count('s') - c6
        c3 = s.count('h') - c8
        c5 = s.count('f') - c4
        c9 = s.count('i') - c5 - c6 - c8
        c1 = s.count('n') - c7 - 2 * c9
        cc = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
        res = ''.join((str(i) * cc[i] for i in range(10)))
        return res

    def test(self):
        nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        c = Counter(''.join(nums))
        print(c)
        for k in c:
            t = []
            for num in nums:
                if k in num:
                    t.append((num, nums.index(num)))
            print(k, t)


sol = Solution()
sol.test()
s = "nnei"
print(sol.originalDigits(s))