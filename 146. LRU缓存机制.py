# -*- coding:utf-8 -*-

"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""


class ListNode:
    """
    双端链表
    """
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    字典 + 双端链表
    """

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.ht = {}

    def remove_head_node(self):
        """
        删除双链表头结点(最久没有访问过的节点)
        head 的 next 指向表头节点的下一个节点
        表头节点下一节点的 prev 指向 head, 中间的节点就相当于被删了
        :return: 被删除的节点的键, 需要拿到这个去删除字典中键
        """
        node = self.head.next
        self.head.next = node.next
        node.next.prev = node.prev
        return node.key

    def append_to_tail(self, node: ListNode):
        """
        将 node 节点(最近访问的节点)加到表尾
        表尾节点(tail.prev)的 next 指针指向node
        node 的 prev 指针指向表尾节点, next 指针指向 tail
        tail 的 prev 指针指向 node
        :param node: 要加到表尾的节点
        :return:
        """
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def move_to_tail(self, node: ListNode) -> None:
        """
        将链表节点移至表尾
        1. 节点 node 的前一个节点的 next 指针指向node后一个节点
           节点 node 的后一个节点的 prev 指针指向node前一个节点
        2. node 插到表尾
        :param node: 要移动的节点
        :return:
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        self.append_to_tail(node)

    def get(self, key: int) -> int:
        """
        查找元素:
        1. 元素不存在, 返回 -1
        2. 元素存在, 将节点提到链表尾, 返回节点的 val 值
        :param key: 要查找的键
        :return:
        """
        node = self.ht.get(key)
        if not node:
            return -1
        self.move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        1. key不存在的情况, 插入元素
          缓存未满, 插到表尾
          缓存已满, 且key在字典中不存在, 插到表尾, 删除表头, 删除字典中的键值对
        2. key已经存在的情况, 修改值, 节点移到表尾
        :param key: 要插入的键
        :param value: 插入键对应的值
        :return:
        """
        if (not key in self.ht):
            if (len(self.ht) >= self.capacity):
                removed_key = self.remove_head_node()
                self.ht.pop(removed_key)
            node = ListNode(key, value)
            self.ht[key] = node
            self.append_to_tail(node)
        else:
            node = self.ht[key]
            node.val = value
            self.move_to_tail(node)


ops = [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]]
cache = LRUCache(ops[0][0])
for op in ops[1:]:
    if len(op) == 1:
        cache.get(op[0])
    else:
        cache.put(op[0], op[1])

    # p = cache.head
    # while p!=cache.tail:
    #     print((p.key, p.val), end = '->')
    #     p = p.next
    # print('None')
