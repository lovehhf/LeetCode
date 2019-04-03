# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一组字符，使用原地算法将其压缩。
压缩后的长度必须始终小于或等于原数组长度。
数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
在完成原地修改输入数组后，返回数组的新长度。

进阶：
你能否仅使用O(1) 空间解决问题？

示例 1：

输入：
["a","a","b","b","c","c","c"]

输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]

说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。
"""


class Solution(object):
    def compress(self, chars):
        """
        1个字符保持不动
        2个以上连续字符以字符,出现次数代替
        :type chars: List[str]
        :rtype: int
        """
        cur = 0
        count = 1
        while cur<len(chars)-1:
            if chars[cur] == chars[cur+1]:
                chars.pop(cur+1)
                count += 1
            else:
                if count > 1:
                    tmp = list(str(count))
                    for i in range(len(tmp)):
                        chars.insert(cur + 1 + i, tmp[i])
                    cur += len(tmp) + 1
                    count = 1
                else:
                    cur += 1
        if count > 1:
            chars.extend(list(str(count)))
        return len(chars)

    def compress2(self, chars):
        """
        1个字符保持不动
        2个以上连续字符以字符,出现次数代替
        :type chars: List[str]
        :rtype: int
        """
        left,right = 0,1
        count = 1
        while right<len(chars):
            if chars[left] == chars[left+1]:
                chars.pop(right)
                count += 1
            else:
                if count > 1:
                    tmp = list(str(count))
                    for i in range(len(tmp)):
                        chars.insert(left + 1 + i, tmp[i])
                    # ['a', 'b', '1','2']
                    # chars.insert(left+1, str(count))
                    left += len(tmp) + 1
                    right += len(tmp) + 1
                    count = 1
                else:
                    left += 1
                    right += 1
        if count > 1:
            chars.extend(list(str(count)))
        return len(chars)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
s = Solution()
print(s.compress(chars))