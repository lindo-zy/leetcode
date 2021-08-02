#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import combinations
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 剔除0
        nums.sort()
        arr = []
        for i in nums:
            if i != 0:
                arr.append(i)
        # 较小的2个边之和>第三边
        # 边长不能为0
        cnt = 0
        for item in list(combinations(arr, 3)):
            if item[0] + item[1] > item[2]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 3, 4]
    print(s.triangleNumber(nums))
