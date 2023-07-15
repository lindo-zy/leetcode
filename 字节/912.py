#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random
from typing import List


class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = random.choice(arr)
        low = [x for x in arr if x < pivot]
        high = [x for x in arr if x > pivot]
        mid = [x for x in arr if x == pivot]
        return self.sortArray(low) + mid + self.sortArray(high)


if __name__ == '__main__':
    sn = Solution()
    nums = [5, 2, 3, 1]
    print(sn.sortArray(nums))
