#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(set(s)) < k or len(s) < k:
            return 0

        right = 0
        n = len(s)
        ans = 0
        while right + k <= n:
            temp = s[right:right + k]
            if len(set(temp)) == k and len(temp) == k:
                ans += 1
            right += 1

        return ans


if __name__ == '__main__':
    sn = Solution()
    s = "havefunonleetcode"
    K = 5
    print(sn.numKLenSubstrNoRepeats(s, K))
