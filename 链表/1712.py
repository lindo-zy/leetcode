#!/usr/bin/python3
# -*- coding:utf-8 -*-
# https://leetcode.cn/problems/binode-lcci/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        head = TreeNode(None)
        self.pre = head
        self.inorder(root)
        return head.right

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            root.left = None
            self.pre.right = root
            self.pre = root
            self.inorder(root.right)


if __name__ == '__main__':
    pass
