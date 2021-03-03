#!/usr/bin/python3
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if nums:
            m = len(nums) // 2
            r = TreeNode(nums[m])
        r.left, r.right = map(self.sortedArrayToBST, [nums[:m]], nums[m + 1:])
        return r
