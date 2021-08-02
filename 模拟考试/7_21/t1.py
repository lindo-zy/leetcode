#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
from typing import List

from gen_tree import generate_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        cnt, level_sum = [], []

        def dfs(root, depth):
            if root:
                if len(cnt) < depth:
                    cnt.append(0)
                    level_sum.append(0)
                cnt[depth - 1] += 1
                level_sum[depth - 1] += root.val
                dfs(root.left, depth + 1)
                dfs(root.right, depth + 1)

        dfs(root, 1)
        return [s / c for s, c in zip(level_sum, cnt)]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 9, 20, None, None, 15, 7]
    root = generate_tree(nums)
    print(s.averageOfLevels(root))
