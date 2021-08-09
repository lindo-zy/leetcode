#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def dfs(start, temp):
            if len(temp) >= 2 and temp not in ans:
                if sorted(temp) == temp:
                    ans.append(temp)
            for i in range(start, n):
                dfs(i + 1, temp + [nums[i]])

        dfs(0, [])

        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [4, 6, 7, 7]
    print(s.findSubsequences(nums))
