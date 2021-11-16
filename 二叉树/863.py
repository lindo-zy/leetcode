#!/usr/bin/python3
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 需要记录下来每个节点的父节点
        # 节点值是唯一的
        self.parents = {}

        def get_parent(root):
            if root.left:
                self.parents[root.left.val] = root
                get_parent(root.left)
            if root.right:
                self.parents[root.right.val] = root
                get_parent(root.right)

        self.res = []
        get_parent(root)

        def dfs(root, node, k):
            if k == 0:
                self.res.append(root.val)
                return
            if root.left and root.left != node:
                dfs(root.left, root, k - 1)
            if root.right and root.right != node:
                dfs(root.right, root, k - 1)
            if root.val in self.parents and self.parents[root.val] != node:
                dfs(self.parents[root.val], root, k - 1)

        dfs(target, None, k)
        return self.res


if __name__ == '__main__':
    s = Solution()
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    target = 5
    K = 2

    from gen_tree import generate_tree

    print(s.distanceK(generate_tree(root), generate_tree([target]), K))
