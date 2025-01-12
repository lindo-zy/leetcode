#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        for i in range(1, len(res)):
            if res[i] > res[i - 1]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    sn = Solution()
    root = [2, 1, 3]
    from gen_tree import generate_tree

    print(sn.isValidBST(generate_tree(root)))
