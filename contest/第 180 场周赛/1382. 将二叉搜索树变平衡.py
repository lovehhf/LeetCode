# -*- coding:utf-8 -*-

"""
给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
如果有多种构造方法，请你返回任意一种。

示例：
输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
 

提示：
树节点的数目在 1 到 10^4 之间。
树节点的值互不相同，且在 1 到 10^5 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balance-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from utils.TreeNode import TreeNode, List2TN, TN2List


class Solution:
    def inorder(self, root):
        """
        中序遍历
        :param root:
        :return:
        """
        if not root:
            return []
        return self.inorder(root.left) + [root] + self.inorder(root.right)

    def rebuild(self, inorder):
        """
        以中序遍历的结果重建二叉树
        :param inorder:
        :return:
        """
        if not inorder:
            return
        n = len(inorder)
        mid = n >> 1
        root = inorder[mid]
        root.left = self.rebuild(inorder[: mid])
        root.right = self.rebuild(inorder[mid + 1:])
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        先中序遍历, 再重建二叉平衡搜索树
        :param root:
        :return:
        """
        inorder = self.inorder(root)
        res = self.rebuild(inorder)
        return res


if __name__ == '__main__':
    root = List2TN([1, None, 2, None, 3, None, 4, None, None])
    s = Solution()
    root_new = s.balanceBST(root)
    print(TN2List(root_new))
