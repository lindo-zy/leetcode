#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        ans = set()

        def dfs(root):
            if root:
                ans.add(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        if len(ans) > 1:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    root = [1, 1, 1, 1, 1, None, 1]
    from gen_tree import generate_tree

    print(s.isUnivalTree(generate_tree(root)))
