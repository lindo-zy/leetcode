#!/usr/bin/python3
# -*- coding:utf-8 -*-.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import Counter


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(root, pre, cnt):
            if not root:
                return 0
            cnt += root.val
            ans = pre[cnt - sum]
            pre[cnt] += 1
            if root.left:
                ans += dfs(root.left, pre, cnt)
            if root.right:
                ans += dfs(root.right, pre, cnt)
            pre[cnt] -= 1
            return ans

        return dfs(root, Counter([0]), 0)


if __name__ == '__main__':
    s = Solution()

    from gen_tree import generate_tree

    root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    targetSum = 8
    print(s.pathSum(generate_tree(root), targetSum))
