#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        left = 0
        right = k + 1  # 滑动窗口长度
        ds = {}
        while right <= n:
            # 当前元素
            # 判断当前窗口内元素是否存在 abs(num[i]-abs[j])<=t的元素
            for num in nums[left:right]:
                print(num)
            left += 1
            right += 1

        for i in range(n):
            pass


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(s.containsNearbyAlmostDuplicate(nums, k, t))
