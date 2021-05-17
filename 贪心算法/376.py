#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return len(nums)
        cur_diff = 0
        pre_diff = 0
        result = 1
        for i in range(len(nums) - 1):
            cur_diff = nums[i + 1] - nums[i]
            if (cur_diff > 0 and pre_diff <= 0) or (pre_diff >= 0 and cur_diff < 0):
                result += 1
                pre_diff = cur_diff
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [1, 7, 4, 9, 2, 5]
    print(s.wiggleMaxLength(nums))
