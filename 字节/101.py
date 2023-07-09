#!/usr/bin/python3
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        res = defaultdict(list)

        def dfs(root, level):
            if not root:
                return
            res[level].append(root.val if root else None)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        for k, v in res.items():
            if v != v[::-1]:
                return False
        return True


if __name__ == '__main__':
    sn = Solution()
    root = [1, 2, 2, 3, 4, 4, 3]
    from gen_tree import generate_tree

    print(sn.isSymmetric(generate_tree(root)))
