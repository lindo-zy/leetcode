#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        while n > 1:
            n -= 1
            for i in range(1, 5):
                dp[i] += dp[i - 1]
        print(dp)
        return sum(dp)

        # return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24


if __name__ == '__main__':
    sn = Solution()
    n = 1  # 5
    n = 2  # 15
    n = 3  # 35
    n = 4  # 70
    n = 5  # 126
    n = 33  # 66045

    print(sn.countVowelStrings(n))
