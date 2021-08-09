#!/usr/bin/python3
# -*- coding:utf-8 -*-
import bisect
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        stack = []
        # 查找当前数组中的最长上升子序列
        # 必须包含当前数
        for i, num in enumerate(obstacles):
            if not stack or stack[-1] <= num:
                stack.append(num)
                res.append(len(stack))
            else:
                idx = bisect.bisect_right(stack, num)
                stack[idx] = num
                res.append(idx + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    obstacles = [3, 1, 5, 6, 4, 2]
    print(s.longestObstacleCourseAtEachPosition(obstacles))
