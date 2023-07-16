#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import defaultdict
        findout = defaultdict(int)
        for i in t:
            findout[i] += 1

        min_len, res = float('inf'), ""
        l, counter = len(s), len(t)
        left = right = 0

        while right < l:
            if findout[s[right]] > 0:
                counter -= 1
            findout[s[right]] -= 1  # 说明找到一个元素，right右移
            right += 1
            while counter == 0:  # 找不到元素
                if min_len > right - left:
                    min_len = right - left
                    res = s[left:right]
                if findout[s[left]] == 0:
                    counter += 1
                findout[s[left]] += 1
                left += 1
        return res
