#!/usr/bin/python3
# -*- coding:utf-8 -*-
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        st = []
        for num in nums:
            idx = bisect.bisect_left(st, num)
            if idx == len(st):
                st.append(num)
            else:
                st[idx] = num

        return len(st)


if __name__ == '__main__':
    sn = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(sn.lengthOfLIS(nums))
