#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def findNthDigit(self, n: int) -> int:
        words = []
        for i in range(1, n + 1):
            words.extend([int(i) for i in str(i)])
        print(words)


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.findNthDigit(n))
