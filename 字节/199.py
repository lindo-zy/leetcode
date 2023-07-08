#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []

        def dfs(root, level):
            if root is None:
                return
            if level == len(ans):
                ans.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    sn = Solution()
    root = [1, 2, 3, None, 5, None, 4]
    from gen_tree import generate_tree

    print(sn.rightSideView(generate_tree(root)))
