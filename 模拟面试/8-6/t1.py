#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for num in asteroids:
            while stack and 0 < stack[-1] < -num:
                stack.pop()
            if not stack or stack[-1] < 0 or num > 0:
                stack.append(num)
            elif stack[-1] == -num:
                stack.pop()
        return stack


if __name__ == '__main__':
    s = Solution()
    asteroids = [5, 10, -5]
    print(s.asteroidCollision(asteroids))
