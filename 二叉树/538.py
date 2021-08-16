#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            root.val += self.pre
            self.pre = root.val
            dfs(root.left)

        dfs(root)
        return root


if __name__ == '__main__':
    s = Solution()
    root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    from gen_tree import generate_tree

    print(s.convertBST(generate_tree(root)))
