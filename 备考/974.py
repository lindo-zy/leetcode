#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        dct, pre, res = defaultdict(int), 0, 0
        dct[0] = 1
        for n in nums:
            pre += n
            res += dct[pre % k]
            dct[pre % k] += 1
        return res


if __name__ == '__main__':
    s = Solution()
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    print(s.subarraysDivByK(A, K))
