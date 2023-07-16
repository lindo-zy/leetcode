#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            cur = TreeNode(root.val)
            cur.left = dfs(root.right)
            cur.right = dfs(root.left)
            return cur

        return dfs(root)
