#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(root, target, tmp):
            if not root:
                return
            if not root.left or not root.right:
                if target == root.val:
                    res.append(tmp + [root.val])
            dfs(root.left, target - root.val, tmp + [root.val])
            dfs(root.right, target - root.val, tmp + [root.val])

        dfs(root, sum, [])
        return res


if __name__ == '__main__':
    sn = Solution()
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    targetSum = 22
    from gen_tree import generate_tree

    print(sn.pathSum(generate_tree(root), targetSum))
