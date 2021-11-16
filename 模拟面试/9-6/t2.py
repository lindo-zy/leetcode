#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1, 1001):
            if n % i == 0:
                res.append(i)
        if k > len(res):
            return -1
        return res[k - 1]


if __name__ == '__main__':
    s = Solution()
    n = 1000
    k = 3
    print(s.kthFactor(n, k))
