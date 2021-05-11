#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == '__main__':
    sn = Solution()
    # s = "aaabb"
    # k = 3

    s = "bbaaacbd"
    k = 3  # 3

    # s = "ababbc"
    # k = 2
    print(sn.longestSubstring(s, k))
