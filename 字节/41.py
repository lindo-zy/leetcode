#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # 查看下标是否对应
        for i in range(n):
            cur = i + 1
            if cur != nums[i]:
                return cur
        # 当前数组如果没有缺失，则为数组长度的下一个数，如当前为[1,2,3],下一个为4
        return n + 1


if __name__ == '__main__':
    sn = Solution()
    nums = [3, 4, -1, 1]
    print(sn.firstMissingPositive(nums))
