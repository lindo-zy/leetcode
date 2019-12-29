#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for num in nums:
            if nums[i] != num:
                i += 1
                nums[i] = num
        return len(nums) and i + 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # nums = [1, 2]
    result = s.removeDuplicates(nums)
    print(result)
    print([0, 1, 2, 3, 4, 2, 2, 3, 3, 4] and 5)
