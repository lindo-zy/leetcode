#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(i) for i in range(1, n + 1)]
        nums.sort()
        return list(map(int, nums))


if __name__ == '__main__':
    s = Solution()
    n = 13
    print(s.lexicalOrder(n))
