#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List

import numpy as np


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        return [np.median(nums[i:i + k]) for i in range(len(nums) - k + 1)]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(s.medianSlidingWindow(nums, k))
