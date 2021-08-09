#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = set()

        def dfs(node):
            if node is not None:
                dfs(node.left)
                self.ans.add(node.val)
                dfs(node.right)

        dfs(root)
        res = sorted(list(self.ans))
        if len(res) > 1:
            return res[1]
        return -1


if __name__ == '__main__':
    s = Solution()
    from gen_tree import generate_tree

    root = [2, 2, 5, None, None, 5, 7]

    print(s.findSecondMinimumValue(generate_tree(root)))
