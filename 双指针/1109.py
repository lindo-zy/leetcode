#!/usr/bin/python3
# -*- coding:utf-8 -*-
from itertools import accumulate
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        counter = [0] * n

        for i, j, k in bookings:
            counter[i - 1] += k
            if j < n:
                counter[j] -= k
        return list(accumulate(counter))


if __name__ == '__main__':
    s = Solution()
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(s.corpFlightBookings(bookings, n))
