# 给你一个非负整数数组 nums 和一个整数 target 。
#
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
#
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
#
#
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
#
#  示例 2：
#
#
# 输入：nums = [1], target = 1
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 20
#  0 <= nums[i] <= 1000
#  0 <= sum(nums[i]) <= 1000
#  -1000 <= target <= 1000
#
#
#  Related Topics 数组 动态规划 回溯 👍 2062 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total or (total + target) % 2 != 0 or (target + total) < 0:
            return 0
        capacity = (target + total) // 2
        # 01背包，背包容量为capacity,装满容量为c的背包的次数
        dp = [0] * (capacity + 1)
        dp[0] = 1
        for num in nums:
            for i in range(capacity, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]


sol = Solution()
print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))
