#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)  # 从头弹出
        return not stack


if __name__ == '__main__':
    s = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(s.validateStackSequences(pushed, popped))
