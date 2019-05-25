# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
返回与给定的前序和后序遍历匹配的任何二叉树。
pre 和 post 遍历中的值是不同的正整数。

示例：
输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
 
提示：

1 <= pre.length == post.length <= 30
pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。

pre:根左右
post:左右根
"""

from utils.TreeNode import TreeNode, TN2List


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post:
            return
        n = len(pre)
        root = TreeNode(pre[0])
        for i in range(1, n):
            if sorted(pre[1:i + 1]) == sorted(post[:i]):
                pre_left = pre[1:i + 1]
                pre_right = pre[i + 1:]
                post_left = post[:i]
                post_right = post[i:-1]
                left = self.constructFromPrePost(pre_left, post_left)
                right = self.constructFromPrePost(pre_right, post_right)
                root.left = left
                root.right = right
                break
        return root


s = Solution()
pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
res = s.constructFromPrePost(pre, post)
print(TN2List(res))