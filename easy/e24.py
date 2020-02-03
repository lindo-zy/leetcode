#!/usr/bin/python3
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        queue = []
        current = [root]
        while current:
            cur_layer_val = []
            next_layer_node = []
            for node in current:
                if node:
                    cur_layer_val.append(node.val)
                    next_layer_node.extend([node.left, node.right])
            if cur_layer_val:
                queue.insert(0, cur_layer_val)
            current = next_layer_node
        return queue
