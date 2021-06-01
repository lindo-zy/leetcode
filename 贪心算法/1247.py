#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        counter1 = Counter(s1)
        counter2 = Counter(s2)
        if counter1 != counter2:
            return -1
        nums1 = [i for i in s1]
        nums2 = [i for i in s2]
        n = len(nums1)


if __name__ == '__main__':
    s = Solution()
    s1 = "xy"
    s2 = "yx"

    print(s.minimumSwap(s1, s2))
