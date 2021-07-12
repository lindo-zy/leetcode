#!/usr/bin/python3
# -*- coding:utf-8 -*-
import collections
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        n = len(nums)
        indices = collections.defaultdict(list)
        xMin, xMax = 10 ** 9, -10 ** 9
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)

        # 记录频次
        freq = [0] * n

        inside = 0
        left, right = xMin, xMin - 1
        bestLeft, bestRight = xMin, xMax

        while right < xMax:
            right += 1
            if right in indices:
                for x in indices[right]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]


if __name__ == '__main__':
    s = Solution()
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(s.smallestRange(nums))
