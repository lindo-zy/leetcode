#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import groupby


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        def check(arr):
            ans = ''
            for item in arr:
                ans += item[0]
            if ans == 'aeiou':
                return True
            return False

        nums = []
        for i, item in groupby(word):
            nums.append([i, len(list(item))])

        right = 0
        n = len(nums)
        ans = 0
        while right + 5 <= n:
            cur = nums[right:right + 5]
            if check(cur):
                ans = max(ans, sum(item[1] for item in cur))
            right += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
    print(s.longestBeautifulSubstring(word))
