import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                q.extend([node.left, node.right])
            else:
                return not any(q)


if __name__ == '__main__':
    sn = Solution()
    root = [1, 2, 3, 4, 5, None, 7]
    from gen_tree import generate_tree

    print(sn.isCompleteTree(generate_tree(root)))
