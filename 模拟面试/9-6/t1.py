#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1


if __name__ == '__main__':
    s = Solution()
    n = 14
    print(s.isUgly(n))
