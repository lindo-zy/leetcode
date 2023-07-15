#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        k = len(word)

        def dfs(i, j, start):
            tmp = board[i][j]
            board[i][j] = '#'
            if start == k:
                return True
            res = []
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[start]:
                    res.append(dfs(nx, ny, start + 1))
            board[i][j] = tmp
            return any(res)

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False


if __name__ == '__main__':
    sn = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(sn.exist(board, word))
