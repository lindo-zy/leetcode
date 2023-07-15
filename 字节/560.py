#!/usr/bin/python3
# -*- coding:utf-8 -*-
import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        pre = collections.defaultdict(int)
        pre[0] = 1

        s = 0
        for i in range(n):
            s += nums[i]
            cnt += pre[s - k]
            pre[s] += 1

        return cnt


if __name__ == '__main__':
    sn = Solution()
    nums = [1, 2, 3]
    k = 3
    print(sn.subarraySum(nums, k))
