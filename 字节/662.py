#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = defaultdict(list)

        def dfs(root, pos, level):
            if not root:
                return
            res[level].append(pos)
            dfs(root.left, pos * 2, level + 1)
            dfs(root.right, pos * 2 + 1, level + 1)

        dfs(root, 0, 0)
        ans = 0
        for item in res.values():
            ans = max(item[-1] - item[0] + 1, ans)
        return ans


if __name__ == '__main__':
    sn = Solution()
    root = [1, 3, 2, 5, None, None, 9, 6, None, 7]
    from gen_tree import generate_tree

    print(sn.widthOfBinaryTree(generate_tree(root)))
