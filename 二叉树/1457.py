#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
from collections import Counter

from gen_tree import generate_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(root, record):
            if root:
                record ^= (1 << root.val)
                if not (root.left or root.right):
                    if bin(record).count("1") < 2:
                        self.ans += 1
                    return
                dfs(root.left, record)
                dfs(root.right, record)

        dfs(root, 0)
        return self.ans


if __name__ == '__main__':
    root = [2, 3, 1, 3, 1, None, 1]
    tree = (generate_tree(root))
    s = Solution()
    print(s.pseudoPalindromicPaths(tree))
