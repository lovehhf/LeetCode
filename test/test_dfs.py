# -*- coding:utf-8 -*-

__author__ = 'huanghf'

from utils import TreeNode

root = TreeNode.List2TN([3, 1, 2, 5, 8, 4, 6, 7, 9, 11, 10])

def dfs(root):
    stack = []
    # 将首个根节点添加到栈中
    stack.append(root)
    res = []
    while stack:
        # 从栈末尾弹出一个节点并判断其是否有左右节点
        # 若有子节点则把对应子节点压入栈中，且优先判断右节点 由于栈是先进后出,会先弹出左节点
        temp = stack.pop()
        l = temp.left
        r = temp.right
        if r:
            stack.append(r)
        if l:
            stack.append(l)
        res.append(temp.val)
    return res

def bfs(root):
    queue = []
    # 根节点加入队列中
    queue.append(root)
    res = []
    while queue:
        temp = queue.pop(0)
        l = temp.left
        r = temp.right
        if l:
            queue.append(l)
        if r:
            queue.append(r)
        res.append(temp.val)
    return res

print(dfs(root))
print(bfs(root))