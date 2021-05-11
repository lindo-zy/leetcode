#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List

from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # n = len(nums)
        # ans = 0
        # left = 0
        # right = 0
        # s = []
        # while right < n:
        #     s.append(nums[right])
        #     s.sort()
        #     if s[-1] - s[0] > limit:
        #         s.remove(nums[left])
        #         left += 1
        #     ans = max(ans, right - left + 1)
        #     right += 1
        #
        # return ans

        s = SortedList()
        n = len(nums)
        left = right = ret = 0

        while right < n:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)
            right += 1

        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [8, 4, 2, 7]  # 2
    limit = 4

    # nums = [10, 1, 2, 4, 7, 2]  # 4
    # limit = 5
    print(s.longestSubarray(nums, limit))
