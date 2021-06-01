#!/usr/bin/python3
# -*- coding:utf-8 -*-
import collections
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        cnt, ans = 0, 0

        for num, occ in freq.most_common():
            cnt += occ
            ans += 1
            if cnt * 2 >= len(arr):
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    print(s.minSetSize(arr))
