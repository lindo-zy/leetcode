#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        visited = set()
        dirs = [0, 1, 0, -1, 0]
        row, col = len(maze), len(maze[0])
        m, n = len(maze), len(maze[0])

        # DFS
        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            for k in range(4):
                move_i, move_j = i, j
                t1 = move_i + dirs[k]
                t2 = move_j + dirs[k + 1]
                while 0 <= t1 < row and 0 <= t2 < col and maze[t1][t2] != 1:
                    move_i, move_j = t1, t2
                if i == move_i and j == move_j:
                    continue
                if (move_i, move_j) not in visited:
                    visited.add((move_i, move_j))
                    if dfs(move_i, move_j):
                        return True
            return False

        return dfs(start[0], start[1])


if __name__ == '__main__':
    s = Solution()
    # maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    # start = [0, 4]
    # destination = [4, 4]

    # maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    # start = [0,4]
    # destination = [3,2]
    #
    # maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
    # start = [4, 3]
    # destination = [0, 1]

    maze = [[0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0]]
    start = [0, 0]
    destination = [8, 6]
    print(s.hasPath(maze, start, destination))
