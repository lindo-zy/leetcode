#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right = n - 1
        left = 0
        max_right = height[n - 1]
        max_left = height[0]
        ans = 0
        while left <= right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
