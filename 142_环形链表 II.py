# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
进阶：
你是否可以不用额外空间解决此题？

1.快慢指针确定是否有环
2.
首先假定链表起点到入环的第一个节点A的长度为a【未知】，到快慢指针相遇的节点B的长度为（a + b）【这个长度是已知的】。
现在我们想知道a的值，注意到快指针p2始终是慢指针p走过长度的2倍，所以慢指针p从B继续走（a + b）又能回到B点，如果只走a个长度就能回到节点A。
但是a的值是不知道的，解决思路是曲线救国，注意到起点到A的长度是a，那么可以用一个从起点开始的新指针q和从节点B开始的慢指针p同步走，相遇的地方必然是入环的第一个节点A。

证明:
假设环内剩余长度为c,
则快指针走过的长度为: 2(a+b) = a + b + c + b 所以c=a
"""

from utils.ListNode import ListNode


class Solution(object):
    def detectCycle(self, head):
        """
        1. 快慢指针确定是否有环
        2. 快慢指针确定环的长度
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        p, q = head, head
        while q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                break
        if p != q: # 无环
            return None
        r = head
        while p!=r:
            p = p.next
            r = r.next
        return p


ls = [ListNode(x) for x in [3, 2, 0, -4]]
for i in range(len(ls) - 1):
    ls[i].next = ls[i + 1]
ls[-1].next = ls[1]
head = ls[0]
s = Solution()
print(s.detectCycle(head))
