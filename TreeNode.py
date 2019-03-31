# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
A leetcode TreeNode helper.
1. How to use it:
    Just like the leetcode way.

2. How it helps:
    a. You can easily create a tree of nodes and return the root by 
        inputing a list, like the problems in Leetcode:
            lst = [0,1,2,3,4,5,6,7,8,9,10,11,12]
            root = List2TN(lst)

        Specific nodes in the list can be returned if needed:
            lst = [0,1,2,3,4,5,6,7,8,9,10,11,12]

        Not only the root node, we also want the instances of the 5th one and 
        the 7th one:
            root, nodesInTree = List2TN(lst, [4, 6])
            (nodesInTree: [[Self: 4]/L: 9/R: 10, [Self: 6]/L: None/R: None])

    b. Change the way of representation from the default one. When you 
        print out a Treenode, the values of itself and the left node and 
        right node would be shown. This also works when you are debugging. 
        The IDE would present a TreeNode like:
            [Self: 7]/L: 82/R: 82

    c. You can change a tree by handling the root to a list by calling the 
        function:
            lst = TN2List(root)
3. Just run this file and try it out!
Versions:
- 1.1 1/20/2018 Jing Qi zzzgin@hotmail.com
    :: Specific nodes in the list can be returned if needed.
- 1.0 1/19/2019 Jing Qi zzzgin@hotmail.com
    :: Created this file.
"""

class TreeNode:
    def __init__(self, x, L=None, R=None):
        self.val = x
        self.left = L
        self.right = R

    def __repr__(self):
        return "[Self: {0}]/L: {1}/R: {2}" \
            .format(self.val, self.left.val if self.left else None, self.right.val if self.right else None)


def List2TN(lst, needs=None):
    '''
    lst: a leetcode way tree list
    needs: A list of Int. The nodes whose indexes provided in this list would be returned.
    EXAMPLE:
        >>> root1 = List2TN([7,82,82,-79,98])
        >>> root1
        [Self: 7]/L: 82/R: 82
        >>> root2, nodesInTree = List2TN([7,82,82,-79,98], [2, 3])
        >>> root2
        [Self: 7]/L: 82/R: 82
        >>> nodesInTree
        [[Self: 82]/L: None/R: None, [Self: -79]/L: None/R: None]
    '''
    nit = []
    root = TreeNode(lst[0])
    tnQ = [root]
    i = 1
    if needs and i in needs:
        nit.append(root)
    while i < len(lst):
        cur = tnQ.pop(0)
        if lst[i] != None:
            cur.left = TreeNode(lst[i])
            tnQ.append(cur.left)
            if needs and i in needs:
                nit.append(cur.left)
        i += 1
        if i >= len(lst):
            break
        if lst[i] != None:
            cur.right = TreeNode(lst[i])
            tnQ.append(cur.right)
            if needs and i in needs:
                nit.append(cur.right)
        i += 1
    if needs:
        return root, nit
    else:
        return root


def TN2List(root):
    q = [root]
    r = []
    while q:
        t = q.copy()
        q.clear()
        for n in t:
            if n == None:
                r.append(None)
            else:
                r.append(n.val)
                q.append(n.left)
                q.append(n.right)
    p = len(r) - 1
    while r[p] == None:
        p -= 1
    return r[:p + 1]


if __name__ == "__main__":
    def test():
        l = [7, 82, 82, -79, 98, 98, -79, -79, None, -28, -24, -28, -24, None, -79, None, 97, 65, -4, None, 3, -4, 65,
             3, None, 97]
        root = List2TN(l)
        print(root)
        lst = TN2List(root)
        print("Input and Output are the same: ", l == lst)
        root1, nodesInTree = List2TN([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [4, 6])
        print(root1)
        print(nodesInTree)
        pass


    test()