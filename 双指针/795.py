#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        def notGreater(R):
            ans = cnt = 0
            for a in A:
                if a < R:
                    cnt += 1
                else:
                    cnt = 0
                ans += cnt
            return ans

        return notGreater(R) - notGreater(L - 1)


if __name__ == '__main__':
    s = Solution()
    A = [2, 1, 4, 3]
    L = 2
    R = 3  # 3
    print(s.numSubarrayBoundedMax(A, L, R))
