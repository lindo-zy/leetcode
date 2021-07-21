#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
1.图：深度优先、广度优先
2.排序：比较器容器
3.设计题
4.滑动窗口、双指针
5.前缀和
6.回溯
7.二分
8.贪心
"""

# 图
from typing import List


class Graph:
    def dfs(self, node):
        if not node:
            return
        visited = set(node)
        stack = [node]
        while stack:
            cur = stack.pop()
            for c in cur:
                if c not in visited:
                    stack.append(cur)
                    stack.append(c)
                    visited.add(c)

    def bfs(self, node):
        from queue import Queue
        if not node:
            return
        queue = Queue()
        visited = set()
        queue.put(node)
        visited.add(node)
        while queue:
            cur = queue.get()
            for c in cur:
                if c not in visited:
                    visited.add(c)
                    queue.put(c)


# 矩阵题
class BoardWithDfs:
    def solve(self, board: List[List[str]]):
        row, col = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            board[i][j] = '#'
            visited.add((i, j))
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = i + x, j + y
                if (nx, ny) not in visited and 0 <= nx < row and 0 <= ny < col and board[nx][ny] != '#':
                    dfs(nx, ny)
                    visited.add((nx, ny))

        def bfs(i, j):
            queue = []
            queue.append((i, j))
            visited.add((i, j))
            while queue:
                i, j = queue.pop(0)
                board[i][j] = '#'
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = i + x, j + y
                    if (nx, ny) not in visited and 0 <= nx < row and 0 <= ny < col and board[nx][ny] != '#':
                        queue.append((nx, ny))
                        visited.add((nx, ny))

        for i in range(row):
            for j in range(col):
                dfs(i, j)
                bfs(i, j)
