#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return 1
        # 求子序列
        pre = 0
        result = 1
        for i in range(1, n):
            cur = nums[i] - nums[i - 1]
            if (cur > 0 and pre <= 0) or (cur < 0 and pre >= 0):
                result += 1
                pre = cur
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [1, 7, 4, 9, 2, 5]
    print(s.wiggleMaxLength(nums))
