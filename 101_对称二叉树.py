# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def isSymmetric(root):
    def ismirror(l_root, r_root):
        if not l_root and not r_root:
            return True
        elif not l_root or not r_root:
            return False
        elif l_root.val == r_root.val:
            return ismirror(l_root.left, r_root.right) and ismirror(l_root.right, r_root.left)
        return False

    return ismirror(root, root)