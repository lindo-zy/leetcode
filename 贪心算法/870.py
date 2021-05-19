#!/usr/bin/python3
# -*- coding:utf-8 -*-
import bisect
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        ans = []
        for b in B:
            index = bisect.bisect_right(A, b)
            if index == len(A):
                ans.append(A.pop(0))
            else:
                ans.append(A.pop(index))

        return ans


if __name__ == '__main__':
    s = Solution()
    nums1 = [12, 24, 8, 32]
    nums2 = [13, 25, 32, 11]
    print(s.advantageCount(nums1, nums2))
