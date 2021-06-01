#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        min_len = len(str(low))
        max_len = len(str(high))

        res = set()
        for i in range(min_len, max_len + 1):
            right = 0
            while right < len(s):
                temp1 = s[right:i + right]
                if low <= int(temp1) <= high:
                    res.add(int(temp1))
                right += 1

        return sorted(list(res))


if __name__ == '__main__':
    s = Solution()
    # low = 100
    # high = 300
    low = 10
    high = 1000000000
    print(s.sequentialDigits(low, high))
