#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and 0 < stack[-1] < a * -1:  # 只有栈顶炸
                stack.pop()
            if not stack or stack[-1] < 0 or a > 0:  # 不发生爆炸
                stack.append(a)
            elif a * -1 == stack[-1]:  # 同时爆炸
                stack.pop()
        return stack


if __name__ == '__main__':
    s = Solution()
    asteroids = [-2, -1, 1, 2]
    asteroids = [5, 10, -5]
    print(s.asteroidCollision(asteroids))
