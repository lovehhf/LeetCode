# -*- coding:utf-8 -*-

"""
二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。
只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。
如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。
注意：节点没有值，本问题中仅仅使用节点编号。

示例 1：
输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
输出：true

示例 2：
输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
输出：false

示例 3：
输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
输出：false

示例 4：
输入：n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
输出：false

提示：
1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-tree-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        indegrees = [0] * n
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l != -1 and r != -1 and l == r:
                return False
            if l != -1:
                indegrees[l] += 1
            if r != -1:
                indegrees[r] += 1
            if indegrees[l] > 2 or indegrees[r] > 2:
                return False

        root = [i for i in range(n) if indegrees[i] == 0]
        if len(root) != 1:
            return False
        root = root[0]
        queue = [root]
        vis = [0] * n
        vis[root] = 1
        while (queue):
            cur = queue.pop(0)
            if leftChild[cur] != -1:
                if vis[leftChild[cur]]:
                    return False
                queue.append(leftChild[cur])
                vis[leftChild[cur]] = 1
            if rightChild[cur] != -1:
                if vis[rightChild[cur]]:
                    return False
                queue.append(rightChild[cur])
                vis[rightChild[cur]] = 1
        # print(root)
        return True


n = 4
leftChild = [1, -1, 3, -1]
rightChild = [2, -1, -1, -1]
s = Solution()
print(s.validateBinaryTreeNodes(n, leftChild, rightChild))
