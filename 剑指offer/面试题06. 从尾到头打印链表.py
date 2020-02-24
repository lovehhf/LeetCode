# -*- coding:utf-8 -*-


"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
 
限制：
0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


解法一：将链表元素加入到数组中, 翻转数组
解法二: 先翻转链表, 再遍历链表
解法三: 利用 dfs 的回溯性质, 递归遍历链表
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_1:

    def reversePrint(self, head: ListNode) -> List[int]:
        """
        遍历链表, 翻转数组
        :param head:
        :return:
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]


class Solution_2:

    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []

        # 翻转链表, 翻转之后的表头为 p
        p = head
        q = p.next
        p.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r

        res = []
        while p:
            res.append(p.val)
            p = p.next

        return res


class Solution_3:
    def dfs(self, head, path):
        """
        利用 dfs 的回溯特性, 先递归, 再取值
        """
        if not head:
            return
        self.dfs(head.next, path)
        path.append(head.val)

    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        self.dfs(head, res)
        return res
