#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List

import numpy as np


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        right = 0
        ans = 0
        while right + k <= n:
            temp = np.average(arr[right:right + k])
            if temp >= threshold:
                ans += 1
            right += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    print(s.numOfSubarrays(arr, k, threshold))
