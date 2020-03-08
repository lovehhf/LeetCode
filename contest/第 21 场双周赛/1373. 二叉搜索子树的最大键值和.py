# -*- coding:utf-8 -*-

"""
给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

二叉搜索树的定义如下：

任意节点的左子树中的键值都 小于 此节点的键值。
任意节点的右子树中的键值都 大于 此节点的键值。
任意节点的左子树和右子树都是二叉搜索树。

示例 1：
输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
输出：20
解释：键值为 3 的子树是和最大的二叉搜索树。

示例 2：
输入：root = [4,3,null,1,2]
输出：2
解释：键值为 2 的单节点子树是和最大的二叉搜索树。

示例 3：
输入：root = [-4,-2,-5]
输出：0
解释：所有节点键值都为负数，和最大的二叉搜索树为空。

示例 4：
输入：root = [2,1,3]
输出：6

示例 5：
输入：root = [5,4,8,3,null,6,3]
输出：7
 
提示：
每棵树最多有 40000 个节点。
每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from utils.TreeNode import TreeNode


class Solution:

    def dfs(self, root):
        """
        自底向上 bfs,
        记忆化, 返回2个参数, 第一个参数表示二叉搜索子树的节点和, 第二个参数表示子树是否是二叉搜索树, 如果子树不是不是则树肯定不是二叉搜索树
        :param root:
        :return:
        """
        if not root:
            return 0, True

        left, left_is_bst = self.dfs(root.left)
        right, right_is_bst = self.dfs(root.right)

        if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
            return 0, False

        if not left_is_bst or not right_is_bst:
            return 0, False

        self.res = max(self.res, left + right + root.val)

        return left + right + root.val, True

    def maxSumBST(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
