#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        pre = []
        for i in range(len(s)):
            pre.append(abs(ord(s[i]) - ord(t[i])))
        left = 0
        right = 0
        cnt = 0
        ans = 0

        while right < len(pre):
            cnt += pre[right]
            while cnt > maxCost:
                cnt -= pre[left]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans


if __name__ == '__main__':
    sn = Solution()
    # s = "abcd"
    # t = "bcdf"
    # maxCost = 3

    # s = "abcd"
    # t = "cdef"
    # maxCost = 3

    # s = "abcd"
    # t = "acde"
    # maxCost = 0

    s = "krrgw"
    t = "zjxss"
    maxCost = 19  # 2
    print(sn.equalSubstring(s, t, maxCost))
