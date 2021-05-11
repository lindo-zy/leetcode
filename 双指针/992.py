#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        counter = Counter()
        res = i = 0
        for j in range(len(A)):
            if counter[A[j]] == 0:
                K -= 1
            counter[A[j]] += 1
            while K < 0:
                counter[A[i]] -= 1
                if counter[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 1, 2, 3]  # 7
    K = 2
    print(s.subarraysWithKDistinct(A, K))
