#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # m = len(grid[0])
        # self.cnt = 0
        #
        # def dfs(i, j):
        #     grid[i][j] = 0
        #     for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        #         nx, ny = i + x, j + y
        #         if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
        #             dfs(nx, ny)
        #
        # for i in range(n):
        #     for j in range(m):
        #         if i in [0, n - 1] or j in [0, m - 1] and grid[i][j] == 1:
        #             dfs(i, j)

        if not grid:
            return 0
        len_x = len(grid)
        len_y = len(grid[0])

        def dfs(x, y):
            if x < 0 or x > len_x - 1 or y < 0 or y > len_y - 1 or grid[x][y] != 1:
                return
            grid[x][y] = 0
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for _x, _y in directions:
                dfs(x + _x, y + _y)

        for i in range(len_x):
            for j in range(len_y):
                if i in [0, len_x - 1] or j in [0, len_y - 1] and grid[i][j] == 1:
                    dfs(i, j)
        return sum([sum(grid[i]) for i in range(len_x)])


if __name__ == '__main__':
    s = Solution()
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(s.numEnclaves(grid))
