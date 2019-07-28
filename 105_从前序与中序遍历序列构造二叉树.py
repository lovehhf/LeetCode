# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        def helper(Lin, Rin):
            if Lin < Rin:
                root = TreeNode(preorder.pop(0))
                rootind = inddict[root.val]
                root.left = helper(Lin, rootind)
                root.right = helper(rootind + 1, Rin)
                return root

        inddict = {val: i for i, val in enumerate(inorder)}
        return helper(0, len(inorder))

    def buildTree2(self, preorder, inorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}
        return self.dfs_helper(inorder_map, preorder, 0, len(inorder) - 1)

    def dfs_helper(self, inorder_map, preorder, left, right):
        if not preorder:
            return
        node = preorder.pop(0)
        root = TreeNode(node)
        root_index = inorder_map[node]
        if root_index != left:
            root.left = self.dfs_helper(inorder_map, preorder, left, root_index - 1)
        if root_index != right:
            root.right = self.dfs_helper(inorder_map, preorder, root_index + 1, right)
        return root

    def buildTree3(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        node = TreeNode(preorder.pop(0))
        node.left = self.buildTree3(preorder, inorder[:inorder.index(node.val)])
        node.right = self.buildTree3(preorder, inorder[inorder.index(node.val) + 1:])
        return node

    def buildTree4(self, preorder, inorder):
        """
        20190728
        前序: 根->左->右
        中序: 左->根->右
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return
        root_val = preorder[0]
        inorder_root_index = inorder.index(root_val)
        left_inorder = inorder[:inorder_root_index]
        right_inorder = inorder[inorder_root_index + 1:]
        left_preorder = preorder[1:inorder_root_index + 1]
        right_preorder = preorder[inorder_root_index + 1:]
        root = TreeNode(root_val)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root


s = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
t = s.buildTree4(preorder, inorder)
print(t)
