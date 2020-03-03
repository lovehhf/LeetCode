# -*- coding:utf-8 -*-

"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。

提示：
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
 

注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class DFS_Solution:
    def dfs(self, head):
        if not head:
            return
        node = Node(head.val)
        if node in self.visited:
            return self.visited[node]
        node.random = self.dfs(head.random)
        node.next = self.dfs(head.next)
        return node

    def copyRandomList(self, head: 'Node') -> 'Node':
        self.visited = {}
        return self.dfs(head)


class Solution:

    def copyRandomList(self, head: 'Node'):
        """
        原地复制
        :param head:
        :return:
        """
        if not head:
            return

        # 1. 复制的节点添加到原先链表的节点的后面
        p = head
        while (p):
            node = Node(p.val)
            node.next = p.next
            p.next = node
            p = node.next

        # 2. 复制 random 指针
        p = head
        while (p):
            if (p.random):
                p.next.random = p.random.next
            p = p.next.next

        # 3. 分离链表, 深拷贝不能修改, 原链表题目没有说明
        dummy = Node(0)
        dummy.next = head.next
        p = head
        q = head.next
        while (p):
            p.next = p.next.next
            p = p.next
            if (q.next):
                q.next = q.next.next
                q = q.next

        return dummy.next