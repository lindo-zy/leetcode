# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
#
#  回文字符串 是正着读和倒过来读一样的字符串。
#
#  子字符串 是字符串中的由连续字符组成的一个序列。
#
#
#
#  示例 1：
#
#
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#
#
#  示例 2：
#
#
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 由小写英文字母组成
#
#
#  Related Topics 双指针 字符串 动态规划 👍 1404 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # 创建dp数组
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i < 3 or dp[i + 1][j - 1]:
                        # 当前可以构成回文，记录一次
                        dp[i][j] = True
                        count += 1

        return count


sol = Solution()
print(sol.countSubstrings("abba"))
