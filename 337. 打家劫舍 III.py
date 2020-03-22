# -*- coding:utf-8 -*-

"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1
输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""

from utils.TreeNode import List2TN, TreeNode


class Solution:
    def dfs(self, root):
        """
        记忆化搜索:
        返回两个值:
        0: 偷根节点最多能偷到多少: 根节点 + 不偷左子树 + 不偷右子树
        1: 不偷根节点最多能偷到多少: 不偷根节点不一定要非偷左右子树, 有可能不偷儿子偷孙子的值更大, 如 [4,1,null,2,null,3]
           所有不偷根节点的最大值为 max(偷左子树, 不偷左子树) + max(偷右子树, 不偷右子树)

        也可以使用树形dp会更好理解一点: f[root][0]: 不偷根节点, f[root][1]: 偷根节点
        """
        if not root:
            return (0, 0)

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return (root.val + left[1] + right[1], max(left) + max(right))

    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))


root = List2TN([4, 1, None, 2, None, 3])
s = Solution()
print(s.rob(root))
