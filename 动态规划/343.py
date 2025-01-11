# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
#
#  返回 你可以获得的最大乘积 。
#
#
#
#  示例 1:
#
#
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
#
#  示例 2:
#
#
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
#
#
#
#  提示:
#
#
#  2 <= n <= 58
#
#
#  Related Topics 数学 动态规划 👍 1438 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerBreak(self, n: int) -> int:
        # 拆分成k个乘数的最大值
        # 转换为长度为n的绳子的分为m断时的最大乘积
        dp = [0] * (n + 1)

        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):  # 只需要遍历一半即可
                left = max(j, dp[j])
                right = max(i - j, dp[i - j])
                dp[i] = max(dp[i], left * right)
        return dp[-1]


sol = Solution()
print(sol.integerBreak(10))
