#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = []

        def dfs(root, path):
            if root:
                path.append(root.val)
                if not root.left and not root.right:
                    # 叶子节点
                    res.append(path)
                else:
                    dfs(root.left, path[:])
                    dfs(root.right, path[:])

        dfs(root, [])
        res.sort(key=len, reverse=True)
        deep = len(res[0])
        s = 0
        for item in res:
            if len(item) == deep:
                s += item[-1]

        return s


if __name__ == '__main__':
    s = Solution()
    from gen_tree import generate_tree

    root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
    tree = generate_tree(root)
    print(s.deepestLeavesSum(tree))
