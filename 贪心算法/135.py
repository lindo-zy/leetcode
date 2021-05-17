#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)

        return sum(res)


if __name__ == '__main__':
    s = Solution()
    ratings = [1, 0, 2]
    # ratings = [1, 2, 2]
    ratings = [1, 3, 2, 2, 1]
    print(s.candy(ratings))
