#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # 一轮答题需要消耗的粉笔数
        s = sum(chalk)
        left_chalk = k % s
        if left_chalk == 0:
            return 0
        for i, num in enumerate(chalk):
            left_chalk -= num
            if left_chalk < 0:
                return i


if __name__ == '__main__':
    s = Solution()
    chalk = [5, 1, 5]
    k = 22
    print(s.chalkReplacer(chalk, k))
