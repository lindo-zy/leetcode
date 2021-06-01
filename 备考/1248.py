#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre = [0] * (len(nums) + 1)
        pre[0] = 1
        odd, res = 0, 0
        for n in nums:
            odd += n & 1
            if odd >= k:
                res += pre[odd - k]
            pre[odd] += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 1, 1]  # 2
    k = 3
    # nums = [2,2,2,1,2,2,1,2,2,2]
    # k = 2
    print(s.numberOfSubarrays(nums, k))
