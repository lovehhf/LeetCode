# -*- coding:utf-8 -*-

"""
给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。
注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。
也就是说，你需要重复此过程直到不能继续删除。

示例 1：
输入：root = [1,2,3,2,null,2,4], target = 2
输出：[1,null,3,null,4]
解释：
上面左边的图中，绿色节点为叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。
有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。

示例 2：
输入：root = [1,3,3,3,2], target = 3
输出：[1,3,null,null,2]

示例 3：
输入：root = [1,2,null,2,null,2], target = 2
输出：[1]
解释：每一步都删除一个绿色的叶子节点（值为 2）。

示例 4：
输入：root = [1,1,1], target = 1
输出：[]

示例 5：
输入：root = [1,2,3], target = 1
输出：[1,2,3]

提示：
1 <= target <= 1000
每一棵树最多有 3000 个节点。
每一个节点值的范围是 [1, 1000] 。

显然 bfs 搞不定这个删完叶子节点后还要去删变为叶子节点的父节点的问题
可以使用 dfs, 如果某个节点是叶子节点就干掉这个节点, 删除这个点后它的父节点还在栈里，继续处理父节点...

如何删掉一个节点:
    将它的父节点对应的左/右儿子赋值为None就可以了
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import TreeNode, List2TN, TN2List


class Solution:
    def dfs(self, root: TreeNode, target: int):
        if not root:
            return
        l = root.left
        r = root.right
        self.dfs(l, target)
        self.dfs(r, target)
        # 放在递归的后面判断 root 的左右子树是否是 null, 是就将 root 的 left/right 赋值为空
        # 此时root还在函数栈里面, 处理完 root 的子节点之后就会处理root
        if (l and not l.left and not l.right and l.val == target):
            root.left = None
        if (r and not r.left and not r.right and r.val == target):
            root.right = None

    def removeLeafNodes(self, root: TreeNode, target: int):
        self.dfs(root, target)
        # 根节点的话不会被删掉, 在这里处理了
        if not root.left and not root.right and root.val == target:
            return None
        return root


s = Solution()
root = List2TN([1, 1, 1])
target = 1
res = s.removeLeafNodes(root, target)
print(TN2List(res))
