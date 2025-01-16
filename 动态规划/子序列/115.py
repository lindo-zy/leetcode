# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 10⁹ + 7 取模。
#
#
#
#  示例 1：
#
#
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit
#
#  示例 2：
#
#
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
#
#
#
#  提示：
#
#
#  1 <= s.length, t.length <= 1000
#  s 和 t 由英文字母组成
#
#
#  Related Topics 字符串 动态规划 👍 1303 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 获取字符串t的长度
        n = len(t)
        # 创建一个一维数组dp，初始化为0
        dp = [0] * (n + 1)
        # 空字符串t是s的子序列的一种情况
        dp[0] = 1

        # 遍历字符串s中的每个字符
        for s_char in s:
            # 从后向前遍历字符串t，避免覆盖尚未使用的dp值
            for j in range(n, 0, -1):
                if s_char == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]


sol = Solution()
print(sol.numDistinct(s="babgbag", t="bag"))
