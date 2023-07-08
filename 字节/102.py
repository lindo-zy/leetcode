#!/usr/bin/python3
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []

        def dfs(root, level):
            if root is None:
                return
            if len(ans) == level:
                ans.append([])
            ans[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    sn = Solution()
    root = [3, 9, 20, None, None, 15, 7]
    from gen_tree import generate_tree

    print(sn.levelOrder(generate_tree(root)))
