#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        print(costs)
        total = 0
        n = len(costs) // 2

        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total


if __name__ == '__main__':
    s = Solution()
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    # costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    print(s.twoCitySchedCost(costs))
