#!/usr/bin/python3
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False

            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    s = Solution()
    root = [5, 1, 4, None, None, 3, 6]
    from gen_tree import generate_tree

    print(s.isValidBST(generate_tree(root)))
