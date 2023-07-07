#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return res


if __name__ == '__main__':
    sn = Solution()
    root = [3, 9, 20, None, None, 15, 7]
    from gen_tree import generate_tree

    print(sn.zigzagLevelOrder(generate_tree(root)))
