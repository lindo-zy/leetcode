#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def dfs(root):
            if not root:
                return 0
            left_value = max(dfs(root.left), 0)
            right_value = max(dfs(root.right), 0)
            self.ans = max(self.ans, left_value + right_value + root.val)
            return root.val + max(left_value, right_value)

        dfs(root)
        return self.ans


if __name__ == '__main__':
    sn = Solution()
    root = [-10, 9, 20, None, None, 15, 7]
    from gen_tree import generate_tree

    print(sn.maxPathSum(generate_tree(root)))
