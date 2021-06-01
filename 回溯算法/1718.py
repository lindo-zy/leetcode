#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        lens = 2 * n - 1
        ans = [0] * lens
        visited = set()

        def dfs(start):
            nonlocal n, lens
            if len(visited) == n:
                return ans
            # 当前位置已经填了，那就进行下一个吧
            if ans[start] > 0:
                return dfs(start + 1)
            # 贪心：数字从大到小填
            for i in range(n, 0, -1):
                if i in visited:
                    continue
                sec = start + i
                if i == 1 or (sec < lens and ans[sec] == 0):
                    visited.add(i)
                    ans[start] = i
                    if i > 1:
                        ans[sec] = i
                    if dfs(start + 1):
                        return ans
                    visited.remove(i)
                    ans[start] = 0
                    if i > 1:
                        ans[sec] = 0
            return None

        return dfs(0)


if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.constructDistancedSequence(n))
