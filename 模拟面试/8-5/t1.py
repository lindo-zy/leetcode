#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []

        def dfs(root):
            if not root:
                return
            else:
                dfs(root.left)
                dfs(root.right)
                self.ans.append(root.val)

        dfs(root)
        return self.ans


if __name__ == '__main__':
    from gen_tree import generate_tree

    s = Solution()
    root = [1, None, 2, 3]
    print(s.postorderTraversal(generate_tree(root)))
