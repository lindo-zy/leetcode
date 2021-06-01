#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def dfs(node: TreeNode, max_value: int) -> int:
            if not node:
                return
            else:
                # 如果存在比当前值大的计数器+1
                if node.val >= max_value:
                    self.counter += 1
                    max_value = node.val
                # 递归到叶子为止
                dfs(node.left, max_value)
                dfs(node.right, max_value)

        # 最小值切入
        dfs(root, float('-inf'))
        return self.counter


if __name__ == '__main__':
    s = Solution()
    from gen_tree import generate_tree

    # root = [3, 1, 4, 3, None, 1, 5]
    # root = [3, 3, None, 4, 2]
    root = [2, None, 4, 10, 8, None, None, 4]  # 4
    # root = [9, None, 3, 6] #1
    tree = generate_tree(root)
    print(s.goodNodes(tree))
