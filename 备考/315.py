#!/usr/bin/python3
# -*- coding:utf-8 -*-
import bisect
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortns = []
        res = []
        for n in reversed(nums):
            idx = bisect.bisect_left(sortns, n)
            res.append(idx)
            sortns.insert(idx, n)
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    nums = [5, 2, 6, 1]
    print(s.countSmaller(nums))
