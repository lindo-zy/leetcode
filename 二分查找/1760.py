#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)

        def can(mid):
            cnt = 0
            for x in nums:
                if x % mid == 0:
                    cnt += (x // mid - 1)
                else:
                    cnt += (x // mid)
                if cnt > maxOperations:
                    return False
            return cnt <= maxOperations

        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [9]
    maxOperations = 2

    nums = [7, 17]
    maxOperations = 2
    print(s.minimumSize(nums, maxOperations))
