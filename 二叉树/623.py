#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def dfs(root, level, flag):  # flag用来表示当前遍历到的节点是其双亲节点的左孩子节点还是右孩子节点
            if root:  # 不是根节点的状态
                if level == d:  # 到达了指定替换的行了
                    new_root = TreeNode(v)
                    if not flag:
                        new_root.left = root
                    else:
                        new_root.right = root
                    return new_root
                root.left = dfs(root.left, level + 1, 0)
                root.right = dfs(root.right, level + 1, 1)
                return root
            return TreeNode(v) if level == d else None  # 比较特殊 因为最后一行的下一行也可能是指定行

        return dfs(root, 1, 0)


if __name__ == '__main__':
    s = Solution()
    root = [4, 2, 6, 3, 1, 5]
    val = 1
    depth = 2
    from gen_tree import generate_tree

    print(s.addOneRow(generate_tree(root), val, depth))
