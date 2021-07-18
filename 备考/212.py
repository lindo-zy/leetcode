#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        root = {}
        # 构建字典树
        for w in words:
            p = root
            for c in w:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['finish'] = w
        ans = []

        def dfs(i, j, p):
            c = board[i][j]
            if c not in p:
                return
            last = p[c].pop('finish', False)

            if last:
                ans.append(last)
            board[i][j] = '#'

            for nx, ny in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '#':
                    dfs(nx, ny, p[c])
            board[i][j] = c

            if not p[c]:
                p.pop(c)

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, root)
        return ans


if __name__ == '__main__':
    s = Solution()
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]

    print(s.findWords(board, words))
