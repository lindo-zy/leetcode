#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return

        root = TreeNode(postorder[-1])
        idx = inorder.index(root.val)
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return root
