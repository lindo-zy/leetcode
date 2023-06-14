#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        find = defaultdict(int)
        for i in t:
            find[i] += 1
        min_len = float('inf')
        res = ''

        n = len(s)
        counter = len(t)
        left = right = 0
        while right < n:
            if find[s[right]] > 0:
                counter -= 1
            find[s[right]] -= 1
            right += 1
            while counter == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = s[left:right]
                if find[s[left]] == 0:
                    counter += 1
                find[s[left]] += 1
                left += 1
        return res


if __name__ == '__main__':
    sn = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sn.minWindow(s, t))
