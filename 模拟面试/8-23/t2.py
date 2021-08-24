#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        m = float('inf')

        for i in sorted(range(len(A)), key=A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans

        # N = len(A)
        #
        # ans = 0
        # candidates = [(A[N-1], N-1)]
        #
        # for i in range(N-2, -1, -1):
        #     jx = bisect(candidates, (A[i],))
        #     if jx < len(candidates):
        #         ans = max(ans, candidates[jx][1] - i)
        #     else:
        #         candidates.append((A[i], i))
        # return ans


if __name__ == '__main__':
    s = Solution()
    nums = [6, 0, 8, 2, 1, 5]
    print(s.maxWidthRamp(nums))
