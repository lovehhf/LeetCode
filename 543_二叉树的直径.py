# -*- coding:utf-8 -*-

"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from utils.TreeNode import List2TN


class Solution(object):
    def dfs(self, root):
        """
        记忆化搜索，自底向上 dfs
        :param root:
        :return:
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = self.dfs(root.left)  # 左子树的直径
        right = self.dfs(root.right)  # 右子树的直径

        # 记录遍历过程中的最大直径
        self.res = max(self.res, left + right)

        # 返回该节点对它的父亲节点的贡献的节点数量
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        左子树深度 + 右子树深度
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res


s = Solution()
root = List2TN(
    [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4,
     None, None, None, -2])
print(s.diameterOfBinaryTree(root))
