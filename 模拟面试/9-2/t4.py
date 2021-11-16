#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root):
        self.res = []
        self.inOrder(root)
        if not self.res:
            return
        dummy = TreeNode(-1)
        cur = dummy
        for node in self.res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)


if __name__ == '__main__':
    s = Solution()
    root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
    from gen_tree import generate_tree

    print(s.increasingBST(generate_tree(root)))
