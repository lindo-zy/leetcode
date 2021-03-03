class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # print(s[i-2:i])
            if 10 <= int(s[i - 2:i]) <= 25:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


if __name__ == '__main__':
    sn = Solution()
    num = 12258  # 5
    print(sn.translateNum(num))
