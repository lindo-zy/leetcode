#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode) -> int:
        res = []

        def dfs(root, path, counter):
            if root:
                if counter <= 0:
                    res.append(path)
                    return

                if not root.left and not root.right:
                    res.append(path)
                    return
                else:
                    dfs(root.left, path + [root.val], counter - root.val)
                    dfs(root.right, path + [root.val], counter - root.val)

        dfs(root, [], 4)
        return res


if __name__ == '__main__':
    s = Solution()
    # root = [1, None, 2, None, 3, None, 4, None, 5,]
    root = [1, 2, 3, 4, None, None, 5]
    from gen_tree import generate_tree

    tree = generate_tree(root)
    print(s.countPairs(tree))
