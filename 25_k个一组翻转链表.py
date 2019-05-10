# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

1->2->3->4->5->6->7 3

第一轮翻转:
0->3->2->1->4->5->6->7

第二轮翻转:
0->3->2->1->6->5->4->7

1. 设置虚拟头结点dummy,同时另cur指向dummy
2. first指向cur.next,循环使end指向第k个元素,同时检查是否满足翻转的个数,不满足的话退出
3. 对first->end的元素进行区间翻转
4. 翻转完之后,cur.next指向end,cur指向first(下一轮翻转的第一个节点的前一个元素),fisrt.next指向翻转前end的后一个元素(q)
5. 开始下一轮翻转
"""

from utils.ListNode import List2LN, ListNode


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        dummy: 虚拟头结点
        first: 每一轮翻转的第一个节点
        end: 每一轮翻转的最后一个节点
        cur: first的前一个节点,用于每一轮翻转结束的时候把next指针end,连接链表
        p,q,r: 链表的区间翻转用到的变量
        """
        dummy = ListNode(0)
        cur = dummy
        cur.next = head
        while cur:
            first = cur.next
            end = first
            for _ in range(k - 1):
                if end:
                    end = end.next
                else:
                    break
            if not end:
                break
            # 链表的区间翻转 p = end时结束翻转 此时first.next->end的每个节点都指向了链表的前一个节点
            # eg: 0(cur,dummy)->1(first)<-2<-3(end,p)->4(q)->5(r)->6->7
            p = first
            q = p.next
            while p != end:
                r = q.next
                q.next = p
                p = q
                q = r
            cur.next = end
            cur = first
            first.next = q
        return dummy.next


s = Solution()
k = 3
head = List2LN([1, 2, 3, 4, 5, 6, 7, 8])
print(s.reverseKGroup(head, k))
