#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        # 第i次操作i次，相同的字母不操作
        dist = [0 for i in range(26)]
        for i in range(n):
            d = ord(t[i]) - ord(s[i])
            if d < 0:
                d += 26
            dist[d] += 1

        for d in range(1, 26):
            cur = d + 26 * (dist[d] - 1)
            if cur > k:
                return False
        return True


if __name__ == '__main__':
    sn = Solution()
    s = "abc"
    t = "bcd"
    k = 10
    print(sn.canConvertString(s, t, k))
