#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        cnt = 0
        for i in range(n):
            cnt ^= start + 2 * i
        return cnt


if __name__ == '__main__':
    s = Solution()
    n = 5
    start = 0
    print(s.xorOperation(n, start))
