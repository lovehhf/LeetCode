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

前序遍历:根左右 中序遍历:左右根

遍历前序和中序,
找出可以作为左右子树的数组,用来做递归
eg: [1, 2, 4, 5, 3, 6, 7]和[4, 5, 2, 6, 7, 3, 1]
1为根节点, 前序的 245 和 中序的 452 相同, 245 这三个元素就可以作为左子树递归,除掉根节点和右子树的元素就可能作为右子树拿来递归
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
        root = TreeNode(pre[0])
        n = len(pre)
        for i in range(1, n):
            if sorted(pre[1:i + 1]) == sorted(post[:i]):
                left_pre = pre[1:i + 1] # 左子树的前序遍历
                right_pre = pre[i + 1:] # 右子树的前序遍历
                left_post = post[:i] # 左子树的后序遍历
                right_post = post[i:n - 1] # 右子树的后序遍历
                root.left = self.constructFromPrePost(left_pre, left_post)
                root.right = self.constructFromPrePost(right_pre, right_post)
                break
        return root


s = Solution()
pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
res = s.constructFromPrePost(pre, post)
print(TN2List(res))
