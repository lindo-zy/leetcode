#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(s)
        cnt = 0
        cur = ''
        for word in words:
            cnt += len(word)
            cur += word
            if cnt == n and cur == s:
                return True
        return False


if __name__ == '__main__':
    sn = Solution()
    s = "iloveleetcode"
    words = ["i", "love", "leetcode", "apples"]
    print(sn.isPrefixString(s, words))
