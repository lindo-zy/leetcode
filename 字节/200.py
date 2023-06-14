#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(x, y):
            grid[x][y] = '0'
            # 4个方向遍历
            for c in ([0, 1], [1, 0], [0, -1], [-1, 0]):
                nx, ny = x + c[0], y + c[1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1

        return ans


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    s = Solution()
    print(s.numIslands(grid))
