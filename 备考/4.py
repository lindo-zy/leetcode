#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List

import numpy as np
from sortedcontainers import SortedList


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sort_list = SortedList(nums1)
        sort_list.update(nums2)
        return np.median(sort_list)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1, nums2))
