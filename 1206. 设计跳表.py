# -*- coding:utf-8 -*-

"""
了解更多 : https://en.wikipedia.org/wiki/Skip_list

注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

样例:

Skiplist skiplist = new Skiplist();

skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除
约束条件:

0 <= num, target <= 20000
最多调用 50000 次 search, add, 以及 erase操作。
"""

import random

MAXLEVEL = 16    # 最高层数 log(2)50000 = 16

# 跳表节点
class SkiplistNode:
    def __init__(self, level, val):
        """
        :param level: 跳表节点每层的前进指针
        :param val: 跳表值
        """
        self.val = val
        self.next = [None for _ in range(level)]

# 跳表
class Skiplist:

    def __init__(self):
        self.header = SkiplistNode(MAXLEVEL, -1)  # 跳表头结点
        self.level = 0  # 跳表节点的最高层数

    def random_level(self):
        level = 1

        while ((random.choice([0, 1]))):
            level += 1

        return min(level, MAXLEVEL)


    def search(self, target: int) -> bool:
        """
        :param target:
        :return: 返回target是否存在于跳表中
        """
        x = self.header

        for i in range(self.level - 1, -1, -1):
            while (x.next[i] and x.next[i].val < target):
                x = x.next[i]

        if x.next[0] and x.next[0].val == target:
            return True

        return False

    def add(self, num: int) -> None:
        """
        插入一个元素 num 到跳表
        :param num:
        :return:
        """
        if self.search(num):
            return

        x = self.header
        update = [SkiplistNode(0, 0) for _ in range(MAXLEVEL)]
        for i in range(self.level - 1, -1, -1):
            while (x.next[i] and x.next[i].val < num):
                x = x.next[i]
            update[i] = x

        level = self.random_level()

        # 随机出的层数比当前最高层数大
        if level > self.level:
            for i in range(self.level, level):
                update[i] = self.header
            # 更新最高层数
            self.level = level

        x = SkiplistNode(level, num)

        for i in range(level):
            # 设置新节点的 next 指针
            x.next[i] = update[i].next[i]

            update[i].next[i] = x


    def erase(self, num: int) -> bool:
        """
        在跳表中删除一个值 num
        :param num:
        :return:
        """
        x = self.header
        update = [SkiplistNode(0, 0) for _ in range(MAXLEVEL)]

        for i in range(self.level - 1, -1, -1):
            while (x.next[i] and x.next[i].val < num):
                x = x.next[i]
            update[i] = x

        x = x.next[0]
        if not x or x.val != num:
            return False

        # while x.next[0] and x.val == x.next[0].val:
        #     x = x.next[0]

        level = len(x.next)

        for i in range(level):
            update[i].next[i] = x.next[i]

        if self.level == level:
            while self.level > 0 and self.header.next[self.level - 1].val == num:
                self.level -= 1

        return True







skiplist = Skiplist()

skiplist.add(1)
skiplist.add(2)
skiplist.add(3)
print(skiplist.search(3))   # 返回 true

print(skiplist.search(0))   # 返回 false
skiplist.add(4)
print(skiplist.search(1))   # 返回 true

print(skiplist.erase(0))    # 返回 false，0 不在跳表中
skiplist.erase(1)    # 返回 true

print(skiplist.search(1))   # 返回 false，1 已被擦除)