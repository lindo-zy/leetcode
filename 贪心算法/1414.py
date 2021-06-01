#!/usr/bin/python3
# -*- coding:utf-8 -*-
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a = b = 1
        fibo = [a, b]
        while a + b <= k:
            fibo.append(a + b)
            a, b = b, a + b
        ans = 0

        for num in fibo[::-1]:
            if k >= num:
                ans += 1
                k -= num
            if k < 1:
                break

        return ans


if __name__ == '__main__':
    s = Solution()
    k = 7
    print(s.findMinFibonacciNumbers(k))
