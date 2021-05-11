#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        leftMax = 0
        rightMax = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
