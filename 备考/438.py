#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        right = 0
        ans = []
        p_count = Counter(p)
        while right + n <= len(s):
            temp = s[right:right + n]
            if p_count == Counter(temp):
                ans.append(right)
            right += 1
        return ans


if __name__ == '__main__':
    sn = Solution()
    # s = "cbaebabacd"
    # p = "abc"

    s = "abab"
    p = "ab"
    print(sn.findAnagrams(s, p))
