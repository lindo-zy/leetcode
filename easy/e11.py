#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    target = 2
    result = s.searchInsert(nums, target)
    print(result)
