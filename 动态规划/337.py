# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为
#  root 。
#
#  除了
#  root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的
# 房子在同一天晚上被打劫 ，房屋将自动报警。
#
#  给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
#
#
#
#  示例 1:
#
#
#
#
# 输入: root = [3,2,3,null,3,null,1]
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
#
#  示例 2:
#
#
#
#
# 输入: root = [3,4,5,1,3,null,1]
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
#
#
#
#
#  提示：
#
#
#
#
#
#  树的节点数在 [1, 10⁴] 范围内
#  0 <= Node.val <= 10⁴
#
#
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 2041 👎 0
from typing import Optional

from 二叉树.gen_tree import generate_tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)
            not_robbed = max(left) + max(right)
            robbed = node.val + left[0] + right[0]
            return not_robbed, robbed

        return max(dfs(root))


sol = Solution()
root = [3, 4, 5, 1, 3, None, 1]
generate_tree(root)
print(sol.rob(generate_tree(root)))
