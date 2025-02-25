# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
#  问总共有多少条不同的路径？
#
#
#
#  示例 1：
#
#
# 输入：m = 3, n = 7
# 输出：28
#
#  示例 2：
#
#
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
#
#
#  示例 3：
#
#
# 输入：m = 7, n = 3
# 输出：28
#
#
#  示例 4：
#
#
# 输入：m = 3, n = 3
# 输出：6
#
#
#
#  提示：
#
#
#  1 <= m, n <= 100
#  题目数据保证答案小于等于 2 * 10⁹
#
#
#  Related Topics 数学 动态规划 组合数学 👍 2151 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp:到达当前点的路径个数
        dp = [[0] * n for _ in range(m)]
        # 向右和向下初始化
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


sol = Solution()
print(sol.uniquePaths(7, 3))
