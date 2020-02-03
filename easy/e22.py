#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root) -> bool:
        def isSymmetric(self, root) -> bool:
            if not root:
                return True
            return self.isMirror(root.left, root.right)

        def isMirror(self, p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            l = self.isMirror(p.left, q.right)
            r = self.isMirror(p.right, q.left)
            return p.val == q.val and l and r