#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        edges = []
        dsu = DSU()
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                if i < m - 1:
                    edges.append([abs(heights[i + 1][j] - heights[i][j]), pos, pos + n])
                if j < n - 1:
                    edges.append([abs(heights[i][j + 1] - heights[i][j]), pos, pos + 1])

        edges.sort()
        for edge in edges:
            dsu.union(edge[1], edge[2])
            if dsu.connected(0, m * n - 1):
                return edge[0]

        return 0


class DSU:
    def __init__(self):
        self.par = list(range(10001))

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    s = Solution()
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(s.minimumEffortPath(heights))
