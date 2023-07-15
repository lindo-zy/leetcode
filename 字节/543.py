#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(left + right, self.ans)

            return max(left, right) + 1

        dfs(root)
        return self.ans


if __name__ == '__main__':
    sn = Solution()
