#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 1000000007  # 维护一个单调递增栈
        stack = [(float('-inf'), float('-inf'))]
        res = tmp = 0
        for i in range(len(A)):
            count = 1
            while stack and A[i] <= stack[-1][0]:
                cur = stack.pop()
                count += cur[1]
                tmp -= cur[0] * cur[1]
            stack.append((A[i], count))
            tmp += A[i] * count
            res += tmp
            res %= MOD
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [1, 7, 5, 2, 4, 3, 9]
    print(s.sumSubarrayMins(arr))
