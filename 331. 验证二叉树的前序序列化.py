# -*- coding:utf-8 -*-

"""
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:

输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true
示例 2:

输入: "1,#"
输出: false
示例 3:

输入: "9,#,#,1"
输出: false
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        使用栈模拟二叉树前序遍历
        遍历到叶子节点时， 弹出此节点, 并将该节点替换为 '#'
        :param preorder:
        :return:
        """
        pre = preorder.split(',')
        stack = []
        for node in pre:
            while stack and stack[-1] == '#' and node == '#':
                # 弹出 '#'
                stack.pop()

                # 子树的根节点不存在, 说明有问题, 直接返回False
                if not stack:
                    return False

                # 弹出子树
                stack.pop()
            # 节点入栈
            stack.append(node)
        return stack == ['#']


s = Solution()
preorder = '1,#,1,#,#'
print(s.isValidSerialization(preorder))
