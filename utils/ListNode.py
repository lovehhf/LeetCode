# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        r = ""
        t = self
        for i in range(10):
            if t is None:
                break
            r += str(t.val) + "->"
            t = t.next
        if t:
            r += "..."
        else:
            r += "None"
        return r


def List2LN(ip):
    head = ListNode(0)
    p = head
    for i in ip:
        nN = ListNode(i)
        p.next = nN
        p = p.next
    return head.next

def String2LN(ip):
    lip = ip[1:-1].split(",")
    for i in range(len(lip)):
        lip[i] = int(lip[i])
    return List2LN(lip)

def LN2List(node):
    r = []
    while node:
        r.append(node.val)
        node = node.next
    return r

def LN2String(node):
    r = []
    while node:
        r.append(str(node.val))
        node = node.next
    return '->'.join(r) + '->None'

if __name__ == "__main__":
    def test():
        st = "[1,2,3,4,5,6,7,8,9,10,11,12]"
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        st_root = String2LN(st)
        print(st_root)
        lst_root = List2LN(lst)
        p = lst_root
        while p:
            p = p.next


    test()