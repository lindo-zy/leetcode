#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(s.intersection(nums1, nums2))
