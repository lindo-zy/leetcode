#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        arr = list(zip(difficulty, profit))
        # 按难度排序
        arr.sort(key=lambda x: x[0])
        res = 0
        cur = 0
        maxP = 0
        for w in worker:
            while cur < len(arr) and arr[cur][0] <= w:
                maxP = max(maxP, arr[cur][1])
                cur += 1
            res += maxP
        return res


if __name__ == '__main__':
    s = Solution()
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    print(s.maxProfitAssignment(difficulty, profit, worker))
