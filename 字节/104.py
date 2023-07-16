#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0

        def dfs(root, level):
            if not root:
                return

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            self.ans = max(self.ans, level)

        dfs(root, 1)
        return self.ans
