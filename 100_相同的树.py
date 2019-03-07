# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def isSameTree(self, p, q):
    if not p and not q:
        return True
    elif p is not None and q is not None:
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
    else:
        return False