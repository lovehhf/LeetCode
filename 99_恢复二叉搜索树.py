# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？

1 2 3 4 5
3 2 1 4 5(1,3)
2 1 3 4 5(1,2)
5 2 3 4 1(1,5)

Morris Inorder Traversal 算法流程(非递归，不用栈，O(1)空间)：
从根节点开始遍历，直至当前节点为空为止：

如果当前节点没有左儿子，则打印当前节点的值，然后进入右子树；
如果当前节点有左儿子，则找当前节点的前驱。
(1) 如果前驱节点的右儿子为空，说明左子树没遍历过，则进入左子树遍历，并将前驱节点的右儿子置成当前节点，方便回溯；
(2) 如果前驱节点的右儿子为当前节点，说明左子树已被遍历过，则将前驱节点的右儿子恢复为空，然后打印当前节点的值，然后进入右子树继续遍历；
中序遍历的结果就是二叉树搜索树所表示的有序数列。有序数列从小到大排序，但有两个数被交换了位置。共有两种情况：

交换的是相邻两个数，例如 1 3 2 4 5 6，则第一个逆序对，就是被交换的两个数，这里是3和2；
交换的是不相邻的数，例如 1 5 3 4 2 6，则第一个逆序对的第一个数，和第二个逆序对的第二个数，就是被交换的两个数，这里是5和2；
找到被交换的数后，我们将它们换回来即可。

https://www.acwing.com/solution/LeetCode/content/181/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils.TreeNode import List2TN, TreeNode, TN2List


class Solution(object):
    def recoverTree(self, root):
        """
        非递归中序遍历 时间复杂度O(N),空间复杂度O(N)
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack1 = []
        cur = root
        stack2 = []  # 存放中序遍历结果
        while stack1 or cur:
            if cur:
                stack1.append(cur)
                cur = cur.left
            else:
                node = stack1.pop()
                stack2.append(node)
                cur = node.right

        node1, node2 = stack2[0], stack2[-1]
        n = len(stack2)
        for i in range(n):
            if 0 < i < n - 1 and stack2[i].val > stack2[i + 1].val and stack2[i].val > stack2[i - 1].val:
                node1 = stack2[i]  # 找到左边的被错误交换的节点的位置(比两边都大)
                break
            elif i == 0 and stack2[0].val > stack2[1].val:
                node1 = stack2[0]
                break

        for i in range(n - 1, -1, -1):
            if 0 < i < n - 1 and stack2[i].val < stack2[i + 1].val and stack2[i].val < stack2[i - 1].val:
                node2 = stack2[i]  # 找到右边被交换的节点(比两边都小)
                break
            elif i == n - 1 and stack2[n - 2].val > stack2[n - 1].val:
                node2 = stack2[n - 1]
                break
        node1.val, node2.val = node2.val, node1.val

    def recoverTree2(self, root):
        """
        Morris-traversal算法
        暂时看不懂 以后再看
        :param root:
        :return:
        """
        first, second, prep = None, None, None
        while root:
            if not root.left:
                if prep and prep.val > root.val:
                    if not first:
                        first = prep
                        second = root
                    else:
                        second = root
                prep = root
                root = root.right
            else:
                p = root.left
                while p.right and p.right != root:
                    p = p.right
                if not p.right:
                    p.right = root
                    root = root.left
                else:
                    p.right = None
                    if prep and prep.val > root.val:
                        if not first:
                            first = prep
                            second = root
                        else:
                            second = root
                    prep = root
                    root = root.right
        first.val, second.val = second.val, first.val


s = Solution()
root = List2TN([146, 71, -13, 55, None, 231, 399, 321, None, None, None, None, None, -33])
s.recoverTree(root)
print(TN2List(root))
