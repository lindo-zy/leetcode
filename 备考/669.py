#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        res = []

        def dfs(node):
            if low < node.val < high:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return res
