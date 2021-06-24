#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1):  # bottom triangle
            p *= nums[i]
            res.append(p)
        for i in range(len(nums) - 1, 0, -1):  # top triangle
            q *= nums[i]
            res[i - 1] *= q
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.productExceptSelf(nums))
