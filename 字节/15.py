#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        n = len(nums)
        for i in range(n):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 设置左右指针
            left = i + 1
            right = n - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur < 0:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == '__main__':
    sn = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sn.threeSum(nums))
