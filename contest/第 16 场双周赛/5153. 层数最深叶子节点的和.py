# -*- coding:utf-8 -*-

"""
给你一棵二叉树，请你返回层数最深的叶子节点的和。



示例：



输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15


提示：

树中节点数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。

mid


dl的dfs解法:

class Solution {
public:
    int md, res;
    void dfs(TreeNode* x , int dep) {
        if (x == NULL) return;
        if (x->left == NULL && x->right == NULL) {
            if (dep > md) {
                res = 0;
                md = dep;
            }
            if (dep == md) {
                res += x->val;
            }
        } else {
            dfs(x->left, dep + 1);
            dfs(x->right, dep + 1);
        }
    }

    int deepestLeavesSum(TreeNode* root) {
        md = -1;
        res = 0;
        dfs(root , 0);
        return res;
    }
};
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        bfs层次遍历
        :param root:
        :return:
        """
        s = [0] * 10010
        q = [(root, 0)]
        level = 0
        while q:
            cur, level = q.pop(0)
            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))
            if not cur.left and not cur.right:
                s[level] += cur.val
        return s[level]


class DFS_Solution:
    """
    dfs 解法
    """

    def __init__(self):
        self.max_depth = 0
        self.res = 0

    def dfs(self, node, depth):
        if not node:
            return

        if not node.left and not node.right:
            if depth == self.max_depth:
                self.res += node.val
        else:
            if depth + 1 > self.max_depth:
                self.max_depth = depth + 1
                self.res = 0
            self.dfs(node.left, depth + 1)
            self.dfs(node.right, depth + 1)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.res
