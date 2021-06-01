#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp, cur, res = {0: -1}, 0, 0
        for idx, num in enumerate(nums):
            cur += num if num else -1
            res = max(res, idx - dp.setdefault(cur, idx))
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0]  # 2
    print(s.findMaxLength(nums))
