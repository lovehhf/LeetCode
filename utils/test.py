# -*- coding:utf-8 -*-

__author__ = 'huanghf'

from utils import TreeNode

l = [2,1,3,4,None,5,6]

root = TreeNode.List2TN(l)

l1 = TreeNode.TN2List(root.left)

print(root)
print(l1)