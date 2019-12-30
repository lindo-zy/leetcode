#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    nums = [3]
    val = 2
    result = s.removeElement(nums, val)
    print(result)
