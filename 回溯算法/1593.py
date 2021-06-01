#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        self.res = float('-inf')
        if len(s) == 1:
            return 1

        def dfs(i, path):
            if i == n:
                print(path)
                self.res = max(self.res, len(path))
                return
            for j in range(i, n):
                if s[i:j + 1] not in path:
                    dfs(j + 1, path | {s[i:j + 1]})

        dfs(0, set())
        return self.res


if __name__ == '__main__':
    sn = Solution()
    # s = "ababccc"
    s = "wwwzfvedwfvhsww"
    # s = "aa"
    # s = "aba"
    print(sn.maxUniqueSplit(s))
