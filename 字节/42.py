#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_value = 0
        right_value = 0
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            left_value = max(left_value, height[left])
            right_value = max(right_value, height[right])
            if height[left] < height[right]:
                ans += left_value - height[left]
                left += 1
            else:
                ans += right_value - height[right]
                right -= 1

        return ans
