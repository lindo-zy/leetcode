#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import product
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums = list(product(nums1, nums2))
        nums.sort(key=lambda x: (x[0] + x[1]))
        return [list(item) for item in nums[:k]]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(s.kSmallestPairs(nums1, nums2, k))
