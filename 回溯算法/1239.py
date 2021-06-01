#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [set(s) for s in arr if len(s) == len(set(s))]

        self.res = 0

        def dfs(pth, idx):
            if len(pth) > self.res:
                self.res = len(pth)
            for i in range(idx, len(arr)):
                if len(pth & arr[i]) == 0:
                    dfs(pth | arr[i], i + 1)

        dfs(set(), 0)
        return self.res


if __name__ == '__main__':
    s = Solution()
    # arr = ["abcdefghijklmnopqrstuvwxyz"]
    arr = ["cha", "r", "act", "ers"]
    print(s.maxLength(arr))
    # print(len({1, 2} & {3, 4}))
