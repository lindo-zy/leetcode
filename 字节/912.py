#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        low = [x for x in arr[1:] if x <= pivot]
        high = [x for x in arr[1:] if x > pivot]
        return self.sortArray(low) + [pivot] + self.sortArray(high)


if __name__ == '__main__':
    sn = Solution()
    nums = [5, 2, 3, 1]
    print(sn.sortArray(nums))
