#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != 'O':
                return

            board[i][j] = 'A'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 先遍上下
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        # 再遍左右
        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)
        # 修改图
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'


if __name__ == '__main__':
    s = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

    print(s.solve(board))
