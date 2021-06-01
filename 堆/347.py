#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import groupby
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        nums.sort()
        for i, j in groupby(nums):
            res.append([i, len(list(j))])
        res.sort(key=lambda x: -x[1])

        return [i[0] for i in res[:k]]


if __name__ == '__main__':
    s = Solution()
    # nums = [1, 1, 1, 2, 2, 3]
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    print(s.topKFrequent(nums, k))
