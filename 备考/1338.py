#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # n = len(arr)
        # k = n // 2
        # nums = []
        # for num, item in groupby(arr):
        #     nums.append([num, len(list(item))])
        # print(nums)

        frequents = list(map(lambda a: -1 * a, Counter(arr).values()))

        heapify(frequents)
        i = 0
        cnt = 0
        while i < len(arr) // 2:
            i -= heappop(frequents)
            cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    print(s.minSetSize(arr))
