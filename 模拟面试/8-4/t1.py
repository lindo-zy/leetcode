#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans_left = []
        self.ans_right = []

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    from gen_tree import generate_tree

    s = Solution()
    p = [10, 5, 15]
    q = [10, 5, None, None, 15]
    p_tree = generate_tree(p)
    q_tree = generate_tree(q)
    print(s.isSameTree(p_tree, q_tree))
