#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []

        def dfs(root, path):
            if not root:
                return
            path.append(root.val)
            # 叶子节点
            if not root.left and not root.right:
                ans.append(path)
            else:
                dfs(root.left, path[:])
                dfs(root.right, path[:])

        dfs(root, [])
        cnt = 0
        for item in ans:
            cnt += int(''.join(map(str, item)))

        return cnt


if __name__ == '__main__':
    sn = Solution()
    root = [4, 9, 0, 5, 1]
    from gen_tree import generate_tree

    print(sn.sumNumbers(generate_tree(root)))
