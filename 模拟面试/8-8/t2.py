#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [0 for i in range(n)]

        def dfs(start):
            if visited[start] == 1:
                return False
            if arr[start] == 0 and visited[start] == 0:
                return True
            visited[start] = 1
            left, right = False, False
            if 0 <= start - arr[start] < n:
                left = dfs(start - arr[start])
            if 0 <= start + arr[start] < n:
                right = dfs(start + arr[start])
            return left or right

        return dfs(start)


if __name__ == '__main__':
    s = Solution()
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    print(s.canReach(arr, start))
